from bs4 import BeautifulSoup
import requests
from txt_ids import get_text
import shutil
import os
import sys

from models import db, connect_db, Product, Brand, Type, Category
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

brands = Brand.query.all()
already_have_brand_names = [brand.name for brand in brands]
newly_added_brand_names = []

def make_from_existing(name):
    print('make from existing', file=sys.stderr)
    f = open(f'all_brand_names.html', "r")

    result = BeautifulSoup(f, 'html.parser')
    all_names = result.find_all('a')

    file = open(f"{name}.txt", 'w+')

    for name in all_names:
        brand_name = name.get_text().strip()
        if brand_name == 'Home' or brand_name == '':
            continue
        elif brand_name in already_have_brand_names or brand_name in newly_added_brand_names:
            print('----------------ALREADY HAVE THIS BRAND------------------------')
            continue
        else:
            file.write(f"{brand_name}\n")
            new_brand = Brand(name=brand_name)
            newly_added_brand_names.append(new_brand)
            db.session.add(new_brand)
            db.session.commit()
    file.close()
    f.close()

def make_html_and_txt(name):

    f = open(f'all_{name}.html', "ab+")

    for product in products:
        f.write(product.encode())
    # f.write(result.encode())

    output = f.read()

    result = BeautifulSoup(output, 'html.parser')

    all_names = result.find_all('a')
        # all_face_ids = []

    file = open(f"{name}.txt", 'w+')

    for name in all_names:
        brand_name = name.get_text().strip()
        if brand_name == 'Home' or brand_name == '':
            pass
        else:
            file.write(f"{brand_name}\n")

    file.close()
    f.close()


if os.path.exists(f'all_brand_names.html'):
    make_from_existing('brand_names')
else:
    request = requests.get(
        'https://www.ulta.com/global/nav/allbrands.jsp')

    content = request.content
    result = BeautifulSoup(content, 'html.parser')
    products = result.find_all("ul")
    make_html_and_txt('brand_names')


