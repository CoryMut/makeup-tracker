from bs4 import BeautifulSoup
import requests
from models import db, connect_db, Product
from flask import Flask
import os
import shutil

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

CWD = os.getcwd()


def get_product_html(product):
    product_page = requests.get(product.link)
    content = product_page.content
    result = BeautifulSoup(content, 'html.parser')

    product_html = result.find("div", {"class": "ProductSwatches"})
    # product_html = result.find("div", {"class": "BaseLayout"})

    try:
        f = open(f'{product.name}.html', "wb+")
        f.write(product_html.encode())
        f.close()
        shutil.move(f'{product.name}.html', CWD + '/covergirl_products2')
    except:
        pass
    # f.write(result.encode())


products = Product.query.all()

for product in products:
    get_product_html(product)
