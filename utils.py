from bs4 import BeautifulSoup
import requests
import os


CWD = os.getcwd()
path = CWD + '/individual_html'


def get_all_ids(file):
    with open(f'product_txt_lists/{file}.txt', 'r') as f:

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
    color_options = []

    for color in colors:
        color_name = color.find('img')['alt']
        if 'selected' in color_name:
            color_name = color_name.replace('selected', '')
        if 'OUT OF STOCK' in color_name:
            color_name = color_name.replace('OUT OF STOCK', '')
        color_name = color_name.strip()
        color_options.append(color_name)

    return color_options


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
        with open(f'individual_html/{product_name}.html', "w+", encoding='utf-8') as f:
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
                # f.write(color.encode())
                f.write(str(color))

        # f.close()


def get_colors(product_name):
    color_options = []
    if '/' in product_name:
        product_name = product_name.replace('/', '')
    if '?' in product_name:
        product_name = product_name.replace('?', '')
    if '\\' in product_name:
        product_name = product_name.replace('\\', '')

    with open(f'individual_html/{product_name}.html', 'r') as f:
        result = BeautifulSoup(f, 'html.parser')
        colors = result.find_all('div', {'class': 'ProductSwatches__Cell'})
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

        return color_options