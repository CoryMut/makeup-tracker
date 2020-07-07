from models import db, connect_db, Product, Type
from app import app
import sys

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
db.create_all()

products = Product.query.all()

types = Type.query.all()
type_names = []
new_types = []

for type in types:
    if type.name not in type_names:
        type_names.append(type.name)

for product in products:
    if product.product_type.name not in type_names and product.product_type.name not in new_types:
        new_types.append(product.product_type.name)

for entry in new_types:
    new_type = Type(name=entry)
    db.session.add(new_type)
    db.session.commit()
