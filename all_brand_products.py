from bs4 import BeautifulSoup
import requests
# from lips import get_covergirl_lips, get_covergirl_lipgloss, get_covergirl_lipstick, get_all_colors
from models import db, connect_db, Product, Brand, Type, Category
from flask import Flask
from utils import get_all_ids, get_all_colors, get_colors

import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///makeup3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

count = 0
color_count = 0
passed = 0

BASE_URL = 'https://www.ulta.com'
SITE = 'Ulta Beauty'

all_brands = db.session.query(Brand.name).all()

all_face = get_all_ids('all_face_ids')
all_eyes = get_all_ids('all_eyes_ids')
all_lips = get_all_ids('all_lips_ids')
all_bb_and_cc_creams = get_all_ids('all_bb_and_cc_creams')
all_blush = get_all_ids('all_blush')
all_bronzer = get_all_ids('all_bronzer')
all_color_correcting = get_all_ids('all_color_correcting')
all_concealer = get_all_ids('all_concealer')
all_contouring = get_all_ids('all_contouring')
all_eye_makeup_remover = get_all_ids('all_eye_makeup_remover')
all_eye_primer_and_base = get_all_ids('all_eye_primer_and_base')
all_eyebrows = get_all_ids('all_eyebrows')
all_eyelashes = get_all_ids('all_eyelashes')
all_eyeliner = get_all_ids('all_eyeliner')
all_eyeshadow = get_all_ids('all_eyeshadow')
all_eyeshadow_palettes = get_all_ids('all_eyeshadow_palettes')
all_face_powder = get_all_ids('all_face_powder')
all_face_primer = get_all_ids('all_face_primer')
all_foundation = get_all_ids('all_foundation')
all_highlighter = get_all_ids('all_highlighter')
all_lash_primer_and_serums = get_all_ids('all_lash_primer_and_serums')
all_lip_liner = get_all_ids('all_lip_liners')
all_lip_stains = get_all_ids('all_lip_stains')
all_lipgloss = get_all_ids('all_lipgloss')
all_lipsticks = get_all_ids('all_lipsticks')
all_makeup_remover = get_all_ids('all_makeup_remover')
all_mascara = get_all_ids('all_mascara')
all_sets_and_palettes = get_all_ids('all_sets_and_palettes')
all_setting_spray = get_all_ids('all_setting_spray')
all_shine_control = get_all_ids('all_shine_control')
all_treats_and_balms = get_all_ids('all_treats_and_balms')

f = open('auto_products.html', 'r')

result = BeautifulSoup(f, 'html.parser')

all_products = result.find_all("div", {"class": "productQvContainer"})

products = []


for product in all_products:
    product_dict = {}
    # print('product -------->', product)
    link_and_brand = product.find(
        'h4', {'class': 'prod-title'})

    brand = link_and_brand.find('a').get_text().strip()
    link = BASE_URL + link_and_brand.find('a')['href']
    name = product.find('p', {'class': 'prod-desc'}
                        ).find('a').get_text().strip().replace('-N/A', '')
    try:
        price = product.find('div', {'class': 'productPrice'}).find(
            'span').get_text().strip()
    except AttributeError:
        price = 'N/A'
    product_id = product.find('span', {'class': 'prod-id'}).get_text().strip()
    site = SITE
    # image = product.find('img', {'name': product_id})['src']
    image = product.find(
        'div', {'class': 'quick-view-prod'}).find('img')['src']
    more_colors = product.find(
        'span', {'class': 'product-fulldetails'})

    # print('more colors-------->', more_colors)

    if product_id in all_face:
        category = 'face'
        if product_id in all_foundation:
            _type = 'foundation'
        elif product_id in all_face_powder:
            _type = 'face powder'
        elif product_id in all_concealer:
            _type = 'concealer'
        elif product_id in all_color_correcting:
            _type = 'color correcting'
        elif product_id in all_face_primer:
            _type = 'face primer'
        elif product_id in all_bb_and_cc_creams:
            _type = 'bb & cc creams'
        elif product_id in all_blush:
            _type = 'blush'
        elif product_id in all_bronzer:
            _type = 'bronzor'
        elif product_id in all_highlighter:
            _type = 'highlighter'
        elif product_id in all_contouring:
            _type = 'countouring'
        elif product_id in all_setting_spray:
            _type = 'setting spray'
        elif product_id in all_shine_control:
            _type = 'shine control'
        elif product_id in all_makeup_remover:
            _type = 'makeup remover'

    elif product_id in all_eyes:
        category = 'eyes'
        if product_id in all_eyeshadow_palettes:
            _type = 'eyeshadow palettes'
        elif product_id in all_mascara:
            _type = 'mascara'
        elif product_id in all_eyeliner:
            _type = 'eyeliner'
        elif product_id in all_eyebrows:
            _type = 'eyebrows'
        elif product_id in all_eyeshadow:
            _type = 'eyeshadow'
        elif product_id in all_eye_primer_and_base:
            _type = 'eye primer & base'
        elif product_id in all_eyelashes:
            _type = 'eyelashes'
        elif product_id in all_eye_makeup_remover:
            _type = 'eye makeup remover'
        elif product_id in all_lash_primer_and_serums:
            _type = 'lash primer & serums'

    elif product_id in all_lips:
        category = 'lips'
        if product_id in all_lipsticks:
            _type = 'lipstick'
        elif product_id in all_lipgloss:
            _type = 'lip gloss'
        elif product_id in all_treats_and_balms:
            _type = 'treatments & balms'
        elif product_id in all_lip_liner:
            _type = 'lip liner'
        elif product_id in all_sets_and_palettes:
            _type = 'sets & palettes'
        elif product_id in all_lip_stains:
            _type = 'lip stain'

    if more_colors and 'Colors' in more_colors.get_text().strip():
        # print('in colors------------->', more_colors)
        # print('syntax------------->', more_colors.get_text().strip())
        # print('product----->', product)
        # colors = get_all_colors(link)
        colors = get_colors(name)
        # print('colors----->', colors)
        for color in colors:
            print('color----->', color)
            product_dict = {}
            product_dict['name'] = name
            product_dict['link'] = link
            product_dict['brand_name'] = brand
            product_dict['price'] = price
            product_dict['product_id'] = product_id
            product_dict['product_site'] = site
            product_dict['type'] = _type
            product_dict['category'] = category
            product_dict['image'] = image
            product_dict['color_image'] = color['image']
            # product_dict['image'] = image
            product_dict['color'] = color['color']
            # product_dict['color'] = color
            products.append(product_dict)
            count += 1
            color_count += 1
    else:
        # print('product----->', product)
        color = 'N/A'
        color_image = 'N/A'
        product_dict['name'] = name
        product_dict['link'] = link
        product_dict['brand_name'] = brand
        product_dict['price'] = price
        product_dict['product_id'] = product_id
        product_dict['product_site'] = site
        product_dict['type'] = _type
        product_dict['category'] = category
        product_dict['image'] = image
        product_dict['color'] = color
        product_dict['color_image'] = color_image
        products.append(product_dict)
        count += 1

for product in products:
    try:
        brand = Brand.query.filter_by(name=product['brand_name']).first()
        product['brand']= brand.id
        product_type = Type.query.filter_by(name=product['type']).first()
        product['type'] = product_type.id
        category = Category.query.filter_by(name=product['category']).first()
        product['category'] = category.id
    except:
        print('not in list------>', product, file=sys.stderr)
        print('brand------>', product['brand_name'], file=sys.stderr)
        print('type------>', product['type'], file=sys.stderr)
        print('category------>', product['category'], file=sys.stderr)

for product in products:
    if product['name'] == '':
        continue
    new_product = Product(name=product['name'], link=product['link'], brand_id=product['brand'], price=product['price'], external_product_id=product['product_id'],
                          product_site=product['product_site'], product_type_id=product['type'], category_id=product['category'], image=product['image'], color=product['color'], color_image=product['color_image'], search_terms=f"{product['name']} {product['brand_name']} {product['color']}")
    db.session.add(new_product)
    db.session.commit()

# print('count---------->', count)
# print('color_count---------->', color_count)
# print('passed---------->', passed)

# -------------------############################---------------------------------------------------
# -------------------############################---------------------------------------------------
# -------------------############################---------------------------------------------------

# covergirl_lips = get_covergirl_lips()
# covergirl_lipsticks = get_covergirl_lipstick()
# covergirl_lipgloss = get_covergirl_lipgloss()

# all_face = get_all_ids('all_face_ids')
# all_eyes = get_all_ids('all_eyes_ids')
# all_lips = get_all_ids('all_lips_ids')
# all_bb_and_cc_creams = get_all_ids('all_bb_and_cc_creams')
# all_blush = get_all_ids('all_blush')
# all_bronzer = get_all_ids('all_bronzer')
# all_color_correcting = get_all_ids('all_color_correcting')
# all_concealer = get_all_ids('all_concealer')
# all_contouring = get_all_ids('all_contouring')
# all_eye_makeup_remover = get_all_ids('all_eye_makeup_remover')
# all_eye_primer_and_base = get_all_ids('all_eye_primer_and_base')
# all_eyebrows = get_all_ids('all_eyebrows')
# all_eyelashes = get_all_ids('all_eyelashes')
# all_eyeliner = get_all_ids('all_eyeliner')
# all_eyeshadow = get_all_ids('all_eyeshadow')
# all_eyeshadow_palettes = get_all_ids('all_eyeshadow_palettes')
# all_face_powder = get_all_ids('all_face_powder')
# all_face_primer = get_all_ids('all_face_primer')
# all_foundation = get_all_ids('all_foundation')
# all_highlighter = get_all_ids('all_highlighter')
# all_lash_primer_and_serums = get_all_ids('all_lash_primer_and_serums')
# all_lip_liner = get_all_ids('all_lip_liner')
# all_lip_stains = get_all_ids('all_lip_stains')
# all_lipgloss = get_all_ids('all_lipgloss')
# all_lipsticks = get_all_ids('all_lipsticks')
# all_makeup_remover = get_all_ids('all_makeup_remover')
# all_mascara = get_all_ids('all_mascara')
# all_sets_and_palettes = get_all_ids('all_sets_and_palettes')
# all_setting_spray = get_all_ids('all_setting_spray')
# all_shine_control = get_all_ids('all_shine_control')
# all_treats_and_balms = get_all_ids('all_treats_and_balms')

# for product in products:
#     if product['product_id'] in covergirl_lips:
#         product['category'] = 'lips'

#     if product['product_id'] in covergirl_lipsticks:
#         product['type'] = 'lipstick'

#     elif product['product_id'] in covergirl_lipgloss:
#         product['type'] = 'lip gloss'

# for product in products:
#     if product['product_id'] in all_face:
#         product['category'] = 'face'
#         if product['product_id'] in all_foundation:
#             product['type'] = 'foundation'
#         elif product['product_id'] in all_face_powder:
#             product['type'] = 'face powder'
#         elif product['product_id'] in all_concealer:
#             product['type'] = 'concealer'
#         elif product['product_id'] in all_color_correcting:
#             product['type'] = 'color correcting'
#         elif product['product_id'] in all_face_primer:
#             product['type'] = 'face primer'
#         elif product['product_id'] in all_bb_and_cc_creams:
#             product['type'] = 'bb and cc creams'
#         elif product['product_id'] in all_blush:
#             product['type'] = 'blush'
#         elif product['product_id'] in all_bronzer:
#             product['type'] = 'bronzor'
#         elif product['product_id'] in all_highlighter:
#             product['type'] = 'highlighter'
#         elif product['product_id'] in all_contouring:
#             product['type'] = 'countouring'
#         elif product['product_id'] in all_setting_spray:
#             product['type'] = 'setting spray'
#         elif product['product_id'] in all_shine_control:
#             product['type'] = 'shine control'
#         elif product['product_id'] in all_makeup_remover:
#             product['type'] = 'maekup remover'

#     elif product['product_id'] in all_eyes:
#         product['category'] = 'eyes'
#         if product['product_id'] in all_eyeshadow_palettes:
#             product['type'] = 'eyeshadow palettes'
#         elif product['product_id'] in all_mascara:
#             product['type'] = 'mascara'
#         elif product['product_id'] in all_eyeliner:
#             product['type'] = 'eyeliner'
#         elif product['product_id'] in all_eyebrows:
#             product['type'] = 'eyebrows'
#         elif product['product_id'] in all_eyeshadow:
#             product['type'] = 'eyeshadow'
#         elif product['product_id'] in all_eye_primer_and_base:
#             product['type'] = 'eye primer and base'
#         elif product['product_id'] in all_eyelashes:
#             product['type'] = 'eyelashes'
#         elif product['product_id'] in all_eye_makeup_remover:
#             product['type'] = 'eye makeup remover'
#         elif product['product_id'] in all_lash_primer_and_serums:
#             product['type'] = 'lash primer and serums'

#     elif product['product_id'] in all_lips:
#         product['category'] = 'lips'
#         if product['product_id'] in all_lipsticks:
#             product['type'] = 'lipstick'
#         elif product['product_id'] in all_lipgloss:
#             product['type'] = 'lip gloss'
#         elif product['product_id'] in all_treats_and_balms:
#             product['type'] = 'treatments and balms'
#         elif product['product_id'] in all_lip_liner:
#             product['type'] = 'lip liner'
#         elif product['product_id'] in all_sets_and_palettes:
#             product['type'] = 'sets and palettes'
#         elif product['product_id'] in all_lip_stains:
#             product['type'] = 'lip stain'


# for product in products:
#     # print('color------------->', product['color'])
#     new_product = Product(name=product['name'], link=product['link'], brand=product['brand'], price=product['price'], product_id=product['product_id'],
#                           product_site=product['product_site'], product_type=product['type'], category=product['category'], image=product['image'], color=product['color'])
#     db.session.add(new_product)
#     db.session.commit()

# for product in products:
# print('Name: ', product['name'])
# print('Brand: ', product['brand'])
# print('Link: ', product['link'])
# print('Price: ', product['price'])
# print('product_id: ', product['product_id'])
# print('site: ', product['product_site'])
# print('type: ', product['type'])
# print('category: ', product['category'])
# print('image: ', product['image'])
# print('color:', product['color'])
# print('---------------------------')
