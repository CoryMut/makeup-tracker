from models import db, connect_db, Product, Brand
from app import app
import sys

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
db.create_all()

products = Product.query.all()

# brand_names = db.session.query(Brand.name).all()

brands = Brand.query.all()
brand_names = []
new_brand_names = []

for brand in brands:
    if brand.name not in brand_names:
        brand_names.append(brand.name)

for product in products:
    if product.brand.name not in brand_names and product.brand.name not in new_brand_names:
        new_brand_names.append(product.brand.name)

for entry in new_brand_names:
    new_brand = Brand(name=entry)
    db.session.add(new_brand)
    db.session.commit()
