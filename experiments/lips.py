from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://www.ulta.com'


def get_covergirl_lips():
    with open('covergirl_lips.html', 'r') as f:
        # f = open('covergirl_lips.html', 'r')

        output = f.read()

        result = BeautifulSoup(output, 'html.parser')

        all_products = result.find_all("div", {"class": "productQvContainer"})

        covergirl_lip_products = []

        for product in all_products:
            product_id = product.find(
                'span', {'class': 'prod-id'}).get_text().strip()
            covergirl_lip_products.append(product_id)

        return covergirl_lip_products


def get_covergirl_lipstick():
    with open('covergirl_lipsticks.html', 'r') as f:

        output = f.read()

        result = BeautifulSoup(output, 'html.parser')

        all_products = result.find_all("div", {"class": "productQvContainer"})

        covergirl_lipsticks = []

        for product in all_products:
            product_id = product.find(
                'span', {'class': 'prod-id'}).get_text().strip()
            covergirl_lipsticks.append(product_id)

        return covergirl_lipsticks


def get_covergirl_lipgloss():
    with open('covergirl_lipgloss.html', 'r') as f:

        output = f.read()

        result = BeautifulSoup(output, 'html.parser')

        all_products = result.find_all("div", {"class": "productQvContainer"})

        covergirl_lipgloss = []

        for product in all_products:
            product_id = product.find(
                'span', {'class': 'prod-id'}).get_text().strip()
            covergirl_lipgloss.append(product_id)

        return covergirl_lipgloss


# def get_lip_color():
#     with open('example_lip.html', 'r') as f:

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_products = result.find_all("img")['alt']

#         covergirl_lipgloss = []

#         for product in all_products:
#             product_id = product.find(
#                 'span', {'class': 'prod-id'}).get_text().strip()
#             covergirl_lipgloss.append(product_id)

#         return covergirl_lipgloss


# def get_all_colors():
#     with open('covergirl_lips.html', 'r') as f:

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         more_colors = result.find(
#             'span', {'class': 'product-fulldetails'})
#         # print(more_colors)
#         if more_colors:

#             product_link = result.find(
#                 'span', {'class': 'product-fulldetails'}).find('a')['href']

#             product_page = requests.get(BASE_URL + product_link)
#             # print(product_page)
#             # print(BASE_URL + product_link)

#             content = product_page.content
#             result = BeautifulSoup(content, 'html.parser')
#             # print(result)
#             colors = result.find_all('div', {'class': 'ProductSwatches__Cell'})
#             # print(colors)
#             color_options = []
#             for color in colors:
#                 color_name = color.find('img')['alt']
#                 # print(color_name)
#                 if 'selected' in color_name:
#                     color_name = color_name.replace('selected', '')
#                     # print(color_name)
#                 color_name = color_name.strip()
#                 color_options.append(color_name)

#             # print(color_options)

#             return color_options

#         return 'N/A'


# get_all_colors()

def get_all_colors(product_link):
    product_page = requests.get(product_link)

    content = product_page.content
    result = BeautifulSoup(content, 'html.parser')

    colors = result.find_all('div', {'class': 'ProductSwatches__Cell'})
    # print(colors)
    color_options = []
    for color in colors:
        color_name = color.find('img')['alt']
        if 'selected' in color_name:
            color_name = color_name.replace('selected', '')
        if 'OUT OF STOCK' in color_name:
            color_name = color_name.replace('OUT OF STOCK', '')
        color_name = color_name.strip()
        color_options.append(color_name)
    # print(color_options)
    return color_options


# get_all_colors(
#     'https://www.ulta.com/trunaked-queenship-shadow-sticks?productId=pimprod2006257')
