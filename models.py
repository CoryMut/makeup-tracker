from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()


def connect_db(app):
    db.app = app
    db.init_app(app)


class Brand(db.Model):

    __tablename__ = "brands"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)


class Type(db.Model):

    __tablename__ = "product_types"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)


class Category(db.Model):

    __tablename__ = "product_categories"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)


class UserProduct(db.Model):

    __tablename__ = "users_products"

    user_id = db.Column (db.Integer, db.ForeignKey('users.id'), primary_key=True)

    product_id = db.Column (db.Integer, db.ForeignKey('products.id'), primary_key=True)


class Product(db.Model):
    """Creates pets table with id, name, species, photo_url, age, notes, and availability."""
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    price = db.Column(db.Text, nullable=False)
    external_product_id = db.Column(db.Text, nullable=False)
    product_site = db.Column(db.Text, nullable=False, default='N/A')
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_types.id'), nullable=False, default='N/A')
    category_id = db.Column(db.Integer, db.ForeignKey('product_categories.id'), nullable=False, default='N/A')
    image = db.Column(db.Text, nullable=False)
    color = db.Column(db.Text, nullable=False, default='N/A')
    color_image = db.Column(db.Text, nullable=True)
    search_terms = db.Column(db.Text, nullable=False)

    brand = db.relationship("Brand")
    product_type = db.relationship("Type")
    category = db.relationship("Category")

    # users = db.relationship(
    #             "User",
    #             secondary="users_products",
    #             cascade="all, delete")


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)

    products = db.relationship("Product",secondary="users_products",cascade="all, delete", backref="users", passive_deletes=True)

    @classmethod
    def signup(cls, email, password):
        """Sign up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            email=email,
            password=hashed_pwd
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, email, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """
       
        user = cls.query.filter_by(email=email).first()

        if user:
            try:
                is_auth = bcrypt.check_password_hash(user.password, password)
            except:
                return False
            if is_auth:
                return user


        return False


