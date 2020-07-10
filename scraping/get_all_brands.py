from bs4 import BeautifulSoup
import requests
import shutil
import os
import sys
from txt_ids import get_text
sys.path.append('../')
from models import db, connect_db, Product, Brand, Type, Category
from flask import Flask

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///makeup4')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

brands = Brand.query.all()
already_have_brand_names = [brand.name for brand in brands]
newly_added_brand_names = []


def make_from_existing():

    with open(f"brand_names.txt", 'r', encoding='utf-8') as file:
        output = file.readlines()
    
        brands = set(brand.strip() for brand in output)
        brands=(list(brands))
        
        brands.sort(key=str.lower)
        print(brands)

        for brand in brands:
            if brand in already_have_brand_names or brand in newly_added_brand_names:
                print('----------------ALREADY HAVE THIS BRAND------------------------')
                continue
            else:
                new_brand = Brand(name=brand)
                print(new_brand.name)
                newly_added_brand_names.append(new_brand)
                db.session.add(new_brand)
                db.session.commit()

def make_html_and_txt(name):

    with open(f'all_{name}.html', "a+", encoding='utf-8') as f:
        for product in products:
            print(product)
            f.write(str(product))
    
    with open(f'all_{name}.html', "r", encoding='utf-8') as f:
        output = f.read()

        result = BeautifulSoup(output, features='html.parser', from_encoding='utf-8')

        all_names = result.find_all('a')

        with open(f"{name}.txt", 'w+', encoding='utf-8') as file:
            for name in all_names:
                brand_name = name.get_text().strip()
                if brand_name == 'Home' or brand_name == '':
                    pass
                else:
                    file.write(f"{brand_name}\n")


if os.path.exists(f'all_brand_names.html'):
    make_from_existing()
else:
    request = requests.get(
        'https://www.ulta.com/global/nav/allbrands.jsp')

    content = request.content
    result = BeautifulSoup(content, 'html.parser')
    products = result.find_all("ul")
    make_html_and_txt('brand_names')


