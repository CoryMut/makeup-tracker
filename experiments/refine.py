from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.ulta.com'
SITE = 'Ulta Beauty'

f = open('covergirl_products.html', 'r')

result = BeautifulSoup(f, 'html.parser')

all_products = result.find("div", {"class": "productQvContainer"})
# print(all_products)

# get link to product
products = []
product_dict = {}
# a = all_products.find('a')
# link = BASE_URL + a['href']
# # print(a)
# print('link ----->', link)

# get brand of product and link
link_and_brand = all_products.find(
    'h4', {'class': 'prod-title'})
brand = link_and_brand.find('a').get_text().strip()
link = BASE_URL + link_and_brand.find('a')['href']
print('link ----->', link)
brand = all_products.find(
    'h4', {'class': 'prod-title'}).find('a').get_text().strip()
print('brand ----->', brand)

# get Name of product
name = all_products.find(
    'p', {'class': 'prod-desc'}).find('a').get_text().strip()
print('name ----->', name)

# get product price
price = all_products.find('div', {'class': 'productPrice'}).find(
    'span').get_text().strip()
print('price ----->', price)

product_id = all_products.find('span', {'class': 'prod-id'}).get_text().strip()
print('product_id ----->', product_id)
site = SITE
print('site ----->', site)

product_dict['name'] = name
product_dict['link'] = link
product_dict['brand'] = brand
product_dict['price'] = price
product_dict['product_id'] = product_id
product_dict['product_site'] = site
products.append(product_dict)


# for product in all_products:
#     print(product)
#     product_dict = {}
#     a = product.find_all("a", limit=1)
#     link = a.get('href')
#     product_dict['link'] = link
#     products.append(product_dict)

print(products)
# print(all_products)
