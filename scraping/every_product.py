from bs4 import BeautifulSoup
import requests
import sys
sys.path.append('../')
from models import db, connect_db, Product
from flask import Flask
from utils import get_all_ids, get_all_colors, make_color_html

BASE_URL = 'https://www.ulta.com'
SITE = 'Ulta Beauty'

def individual_html():

    with open('auto_products.html', 'r', encoding='utf-8') as f:
        print('THIS IS HAPPENING', file=sys.stderr)
        result = BeautifulSoup(f, features='html.parser', from_encoding='utf-8')

        all_products = result.find_all("div", {"class": "productQvContainer"})

        for product in all_products:
            link_and_brand = product.find(
                'h4', {'class': 'prod-title'})

            brand = link_and_brand.find('a').get_text().strip()
            link = BASE_URL + link_and_brand.find('a')['href']
            name = product.find('p', {'class': 'prod-desc'}
                                ).find('a').get_text().strip()
            more_colors = product.find(
                'span', {'class': 'product-fulldetails'})
            if more_colors and 'Colors' in more_colors.get_text().strip():
                print('link------->', link)
                make_color_html(name, link)

individual_html()
