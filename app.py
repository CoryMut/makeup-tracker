from flask import Flask, request, render_template,  redirect, flash, session, jsonify, g, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Product, User, UserProduct, Brand, Type, Category
from decorators import login_required
from forms import LoginForm, UserForm
from wtforms.validators import ValidationError

from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import func

from os import environ
from dotenv import load_dotenv
import sys
from werkzeug.utils import secure_filename
import os
from os.path import join, dirname, realpath

import math
from functools import reduce

app = Flask(__name__)

load_dotenv()


# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = (
#     os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS") == 'True')
# app.config['SQLALCHEMY_ECHO'] = (os.getenv("SQLALCHEMY_ECHO") == 'True')
# app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
# app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = (os.getenv("DEBUG_TB_INTERCEPT_REDIRECTS") == 'True')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///makeup3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY","b'x8cDxd2xb8xcbx03xxe8x89x87x07xb9x0cx0b'")
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False


connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

CURR_USER_KEY = "curr_user"


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])
    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.errorhandler(404)
def page_not_found(e):
    """Redirects 404 to home page with error message"""
    return redirect(url_for('collection'))


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = UserForm()

    if form.validate_on_submit():
        # try:
        #     user = User.signup(
        #         password=form.password.data,
        #         email=form.email.data
        #     )
        #     db.session.commit()

        # except IntegrityError:
        #     flash("Username already taken", 'danger')
        #     return render_template('signup.html', form=form)

        user = User.signup(password=form.password.data,email=form.email.data)
        
        db.session.commit()

        do_login(user)
        add_user_to_g()

        return redirect(url_for('collection'))

    else:
        return render_template('signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    if 'curr_user' in session:
        return redirect(url_for('collection'))

    form = LoginForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.authenticate(form.email.data,
                                    form.password.data)

            if user:
                do_login(user)
                return redirect(url_for('collection'))

            else:
                form.password.errors.append('Incorrect password')
                return render_template('login.html', form=form)

    return render_template('login.html', form=form)


@app.route('/')
def home_page():
    """Renders homepage prompting user to go to their collection"""

    return render_template('homepage.html')


@app.route('/collection')
@login_required
def collection():
    """Renders page showing all products in user's collection"""

    brands = set()
    for product in g.user.products:
        brands.add(product.brand.name)

    brands=(list(brands))
    
    brands.sort(key=str.lower)

    types = Type.query.order_by(Type.name).all()

    return render_template('collection.html', products=g.user.products, brands=brands, types=types)


@app.route('/search', methods=["GET"])
@login_required
def search():

    search_term = request.args['search-term']

    if search_term == '' or search_term == ' ':
        return redirect(url_for('collection'))

    offset = request.args.get('offset', 0)
    
    # page_num = math.ceil(Product.query.filter( (func.lower(Product.name).contains(search_term.lower())) | Product.brand.has(name=search_term) | (Product.product_type.has(name=search_term))).count() / 28)

    # results = Product.query.filter( (func.lower(Product.name).contains(search_term.lower())) | Product.brand.has(name=search_term) | (Product.product_type.has(name=search_term))).limit(28).offset(offset).all()

    search_terms = search_term.split(' ')

    if len(search_terms) == 1:
        search_results = Product.query.filter(Product.search_terms.ilike(f"%{search_terms[0]}%")).all()
    else:
        results = {}
        for term in search_terms:
            results_per_term = Product.query.filter(Product.search_terms.ilike(f"%{term}%")).all()
            for product in results_per_term:
                if not product.id in results:
                    results[product.id] = {'score' : 1}
                else:
                    results[product.id]['score'] += 1
        
        results = sorted(results.items(), key=lambda x: ['score'], reverse=True)

        def has_high_score(key):
            if key[1]['score'] >= 2:
                return key
        
        results = list(filter(has_high_score, results))

        search_results = []
        for result in results:
            product = Product.query.get_or_404(result[0])
            search_results.append(product)

    brands = set()
    for result in search_results:
        brands.add(result.brand.name)

    types = Type.query.order_by(Type.name).all()

    # return render_template('results.html', products=search_results, page_num=page_num, search_term=search_term, types=types, brands=brands)
    return render_template('results.html', products=search_results, search_term=search_term, types=types, brands=brands)


@app.route('/add/<int:product_id>', methods=["POST"])
@login_required
def add_to_collection(product_id):

    new_collection = UserProduct(user_id=g.user.id, product_id=product_id)
    db.session.add(new_collection)
    db.session.commit()

    return jsonify(result='Product added successfully')


@app.route('/remove/<int:product_id>', methods=["POST"])
@login_required
def remove_from_collection(product_id):

    remove_product = UserProduct.query.filter(UserProduct.user_id==g.user.id, UserProduct.product_id==product_id).first()
    db.session.delete(remove_product)
    db.session.commit()

    return jsonify(result='Product removed successfully')


@app.route('/logout', methods=["POST"])
@login_required
def logout():
    """Handle logout of user."""

    do_logout()
    flash('Log out successful.', 'success')
    return redirect(url_for('login'))