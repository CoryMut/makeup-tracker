from bs4 import BeautifulSoup
import requests
import shutil
from pathlib import Path
from all_brand_products import populate_product_database
from every_product import individual_html
import os
import sys

from flask import Flask

sys.path.append('../')
from models import db, connect_db, Product, Brand, Type, Category
from utils import get_all_ids, get_all_colors, get_colors

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///makeup4')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


def check_new_products(file_main_txt, file_new_txt, file_main_html, file_new_html, skip=True):
    main = set()
    new = set()

    filename_main = Path(file_main_txt)

    filename_new = Path(file_new_txt)

    print(f'-------preparing {file_main_txt} to {file_new_txt}--------', file=sys.stderr)
    
    with open(filename_main, 'r') as f: 
        for line in f:
            main.add(line)

    with open(filename_new, 'r') as f:
        for line in f:
            new.add(line)

    to_be_added = new.difference(main)
    
    print('TO BE ADDED---------------------->', to_be_added, file=sys.stderr)
    print('------------------------------------------------------------', file=sys.stderr)

    add_new_products_to_txt(file_main_txt, to_be_added) 

    add_new_products_to_html(file_main_html, file_new_html, to_be_added, skip)
    
    print(f'-------FINISHED {file_main_txt} to {file_new_txt}--------', file=sys.stderr)
    
    if skip == False:
        individual_html()
        populate_product_database('new_products.html')


def add_new_products_to_txt(file_main, new_products):

    filename = Path(file_main)
    print(filename, file=sys.stderr)
    
    with open(filename, 'a') as f:
        for _id in new_products:
            f.write(f"{_id}")


def add_new_products_to_html(file_main, file_new, new_products, skip):

    filename_source = Path(file_new)
    filename_to_be_written_to = Path(file_main)
    new_file = Path(f"new_products.html")

    with open(filename_source, 'r') as f_source:
        result = BeautifulSoup(f_source, 'html.parser')
        for _id in new_products:
            _id = _id.strip('\n')
            new_product = result.find("div", {"class": "productQvContainer", "id" : f"{_id}"})

            with open(filename_to_be_written_to, 'ab+') as f_add:
                f_add.write(new_product.encode())

            if skip == False:
                with open(new_file, "ab+") as f_new:
                    f_new.write(new_product.encode())


directory = 'auto_product_html'
for filename in os.listdir(directory):
    name = filename.replace('.html', '')
    check_new_products(f'product_txt_lists/{name}.txt', f'auto_product_txt_2/{name}.txt', f'auto_product_html/{name}.html', f'auto_product_html_2/{name}.html')

check_new_products('auto_products.txt', 'auto_products2.txt', 'auto_products.html', 'auto_products2.html', skip=False)
