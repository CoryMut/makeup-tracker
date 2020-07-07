from models import db, connect_db, Product, Category
from app import app
import sys

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
db.create_all()

products = Product.query.all()

categories = Category.query.all()
category_names = []
new_categories = []

for category in categories:
    if category.name not in category_names:
        category_names.append(category.name)

for product in products:
    if product.category.name not in category_names and product.category.name not in new_categories:
        new_categories.append(product.category.name)

for entry in new_categories:
    new_category = Category(name=entry)
    db.session.add(new_category)
    db.session.commit()
