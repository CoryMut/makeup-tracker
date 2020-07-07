from bs4 import BeautifulSoup
import requests
import os


CWD = os.getcwd()
path = CWD + '/individual_html'


def get_all_ids(file):
    with open(f'product_txt_lists/{file}.txt', 'r') as f:
        # f = open('covergirl_lips.html', 'r')

        my_list = [l.rstrip("\n") for l in f]

        return my_list


def get_all_colors(product_link):
    try:
        product_page = requests.get(product_link)
    except:
        pass
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


# print(get_all_ids('all_concealer'))
# print(get_all_colors(
#       "https://www.ulta.com/face-flour-baking-powder?productId=pimprod2001359"))


def make_color_html(product_name, product_link):
    if '/' in product_name:
        product_name = product_name.replace('/', '')
    if '?' in product_name:
        product_name = product_name.replace('?', '')
    if '\\' in product_name:
        product_name = product_name.replace('\\', '')

    if os.path.exists(f'{path}/{product_name}.html'):
        pass
    else:
        f = open(f'individual_html/{product_name}.html', "wb+")
        try:
            product_page = requests.get(product_link)
        except:
            print('name--------->', product_name)
            print('link--------->', product_link)
            return
        content = product_page.content
        result = BeautifulSoup(content, 'html.parser')

        colors = result.find_all('div', {'class': 'ProductSwatches__Cell'})
        for color in colors:
            f.write(color.encode())

        f.close()

    # try:
    #     f = open(f'individual_html/{product_name}.html', "r")
    # except:
    #     print('name--------->', product_name)
    #     print('link--------->', product_link)
    #     f = open(f'individual_html/{product_name}.html', "wb+")
    #     product_page = requests.get(product_link)
    #     content = product_page.content
    #     result = BeautifulSoup(content, 'html.parser')

    #     colors = result.find_all('div', {'class': 'ProductSwatches__Cell'})
    #     for color in colors:
    #         f.write(color.encode())

    # f.close()


# make_color_html('Face Flour Baking Powder',
#                 'https://www.ulta.com/face-flour-baking-powder?productId=pimprod2001359')

def dummy_func(name):
    CWD = os.getcwd()
    path = CWD + '/individual_html'
    if os.path.exists(f'{path}/{name}.html'):
        print('it is a file')
    else:
        print('is not a file')


# dummy_func('Wonder Stick')


# def get_colors(product_name):
#     color_options = []
#     if '/' in product_name:
#         product_name = product_name.replace('/', '')
#     if '?' in product_name:
#         product_name = product_name.replace('?', '')
#     if '\\' in product_name:
#         product_name = product_name.replace('\\', '')

#     with open(f'individual_html/{product_name}.html', 'r') as f:
#         # content = f.content
#         result = BeautifulSoup(f, 'html.parser')
#         colors = result.find_all('div', {'class': 'ProductSwatches__Cell'})
#         # print(colors)
#         color_options = []
#         for color in colors:
#             color_name = color.find('img')['alt']
#             if 'selected' in color_name:
#                 color_name = color_name.replace('selected', '')
#             if 'OUT OF STOCK' in color_name:
#                 color_name = color_name.replace('OUT OF STOCK', '')
#             color_name = color_name.strip()
#             color_options.append(color_name)
#         # print(color_options)
#         return color_options

def get_colors(product_name):
    color_options = []
    if '/' in product_name:
        product_name = product_name.replace('/', '')
    if '?' in product_name:
        product_name = product_name.replace('?', '')
    if '\\' in product_name:
        product_name = product_name.replace('\\', '')

    with open(f'individual_html/{product_name}.html', 'r') as f:
        # content = f.content
        result = BeautifulSoup(f, 'html.parser')
        colors = result.find_all('div', {'class': 'ProductSwatches__Cell'})
        # print(colors)
        color_options = []
        for color in colors:
            color_combo = {}
            color_name = color.find('img')['alt']
            color_image = color.find('img')['src']
            if 'selected' in color_name:
                color_name = color_name.replace('selected', '')
            if 'OUT OF STOCK' in color_name:
                color_name = color_name.replace('OUT OF STOCK', '')
            color_name = color_name.strip()
            color_combo['color'] = color_name
            color_combo['image'] = color_image
            color_options.append(color_combo)
        # print(color_options)
        return color_options


# print(get_colors('X Thalia Brow Contour'))
