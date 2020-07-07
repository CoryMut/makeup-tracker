from bs4 import BeautifulSoup
import requests
import shutil
import os
import sys
from pathlib import Path

print('starting...')

CWD = os.getcwd()

links = {
    'face': 'https://www.ulta.com/makeup-face?N=26y3&Nrpp=1000',
    'eyes': 'https://www.ulta.com/makeup-eyes?N=26yd&Nrpp=1000',
    'lips': 'https://www.ulta.com/makeup-lips?N=26yq&Nrpp=1000',
    'eyeshadow_palettes': 'https://www.ulta.com/makeup-eyes-eyeshadow-palettes?N=26ye&Nrpp=1000',
    'mascara': 'https://www.ulta.com/makeup-eyes-mascara?N=26yg&Nrpp=1000',
    'eyeliner': 'https://www.ulta.com/makeup-eyes-eyeliner?N=26yh&Nrpp=1000',
    'eyebrows': 'https://www.ulta.com/makeup-eyes-eyebrows?N=26yi&Nrpp=1000',
    'eyeshadow': 'https://www.ulta.com/makeup-eyes-eyeshadow?N=26yf&Nrpp=1000',
    'eye_primer_and_base': 'https://www.ulta.com/makeup-eye-primer-base?N=26yl&Nrpp=1000',
    'eyelashes': 'https://www.ulta.com/makeup-eyes-eyelashes?N=26yj&Nrpp=1000',
    'eye_makeup_remover': 'https://www.ulta.com/makeup-eye-makeup-remover?N=26yk&Nrpp=1000',
    'lash_primer_and_serums': 'https://www.ulta.com/makeup-eyes-lash-primer-serums?N=jllzia&Nrpp=1000',
    'foundation': 'https://www.ulta.com/makeup-face-foundation?N=26y5&Nrpp=1000',
    'face_powder': 'https://www.ulta.com/makeup-face-powder?N=26y8&Nrpp=1000',
    'concealer': 'https://www.ulta.com/makeup-face-concealer?N=26y6&Nrpp=1000',
    'color_correcting': 'https://www.ulta.com/makeup-face-color-correcting?N=uo37yr&Nrpp=1000',
    'face_primer': 'https://www.ulta.com/makeup-face-primer?N=26y4&Nrpp=1000',
    'bb_and_cc_creams': 'https://www.ulta.com/makeup-face-bb-cc-creams?N=277u&Nrpp=1000',
    'blush': 'https://www.ulta.com/makeup-face-blush?N=277v&Nrpp=1000',
    'bronzer': 'https://www.ulta.com/makeup-face-bronzer?N=26y9&Nrpp=1000',
    'highlighter': 'https://www.ulta.com/makeup-face-highlighter?N=27i0&Nrpp=1000',
    'contouring': 'https://www.ulta.com/makeup-face-contouring?N=27eh&Nrpp=1000',
    'setting_spray': 'https://www.ulta.com/makeup-face-setting-spray?N=10wj5jk&Nrpp=1000',
    'shine_control': 'https://www.ulta.com/makeup-face-shine-control?N=26yc&Nrpp=1000',
    'makeup_remover': 'https://www.ulta.com/makeup-face-makeup-remover?N=26yb&Nrpp=1000',
    'lipsticks': 'https://www.ulta.com/makeup-lips-lipstick?N=26ys&Nrpp=1000',
    'lip_gloss': 'https://www.ulta.com/makeup-lip-gloss?N=26yt&Nrpp=1000',
    'treats_and_balms': 'https://www.ulta.com/makeup-lips-treatments-balms?N=26yw&Nrpp=1000',
    'lip_liners': 'https://www.ulta.com/makeup-lip-liner?N=26yv&Nrpp=1000',
    'sets_and_palettes': 'https://www.ulta.com/makeup-lips-sets-palettes?N=26yr&Nrpp=1000',
    'lip_stains': 'https://www.ulta.com/makeup-lip-stain?N=26yu&Nrpp=1000'
}


def additional_request(value):
    value = value.split('&')
    value = value[0] + '&No=1000&' + value[1]

    return value


def make_text(file, name, operation='w+'):

    filename = Path(f"auto_product_html_2/{file}")

    # with open(f'auto_product_html_2/{file}', 'r') as f:
    with open(filename, 'r') as f:

        output = f.read()

        result = BeautifulSoup(output, 'html.parser')

        all_ids = result.find_all('span', {'class': 'prod-id'})
        print('operation for txt file------>', operation, file=sys.stderr)
        file = open(f"auto_product_txt_2/{name}.txt", operation)

        for _id in all_ids:
            product_id = _id.get_text().strip()
            file.write(f"{product_id}\n")

    file.close()
    print('finished writing', file=sys.stderr)
    # shutil.move(f'{file}', CWD + '/auto_product_txt')


def make_html_and_txt(name, operation='wb+'):

    filename = Path(f"auto_product_html_2/all_{name}.html")

    if not filename.exists() or operation != 'wb+':
        print("Oops, file doesn't exist!", file=sys.stderr)
        print(operation, file=sys.stderr)
        f = open(filename, operation)
        
        print('opened file', file=sys.stderr)
        
        for product in products:
            print('writing', file=sys.stderr)
            f.write(product.encode())
                
        f.close()
        
        make_text(f'all_{name}.html', f'all_{name}')

    else:
        print("Yay, the file exists!", file=sys.stderr)



def make_html_and_txt_over_1000(name, value, operation='wb+'):

    filename = Path(f"auto_product_html_2/all_{name}.html")

    if not filename.exists():
        print("Oops, file doesn't exist!", file=sys.stderr)
        print(operation, file=sys.stderr)
        f = open(filename, operation)
        
        print('opened file', file=sys.stderr)
        
        value = additional_request(value)
        print('value---------->', value, file=sys.stderr)
        request = requests.get(value)
        content = request.content
        result = BeautifulSoup(content, 'html.parser')
        products2 = result.find_all("ul", {"id": "foo16"})

        for product in products:
            print('writing', file=sys.stderr)
            f.write(product.encode())
        
        for product in products2:
            print('writing', file=sys.stderr)
            f.write(product.encode()) 

        f.close()
        
        make_text(f'all_{name}.html', f'all_{name}')

    else:
        print("Yay, the file exists!", file=sys.stderr)



    # if os.path.exists(f'auto_product_html_2/all_{name}.html'):
    #     print('File already exists')
    #     pass
    # else:
    #     f = open(f'auto_product_html/all_{name}.html', operation)
    #     print('opened file')
    #     for product in products:
    #         print('writing')
    #         print(product)
    #         f.write(product.encode())
                
    #         # # f.write(result.encode())

    #     f.close()

    #         # # shutil.move(f'{f}', CWD + '/auto_product_html')
    #     make_text(f'all_{name}.html', f'all_{name}')


# def additional_request(value):
#     value = value.split('&')
#     value = value[0] + '&No=1000&' + value[1]

#     return value


# print('about to start looping over links...')
# for key, value in links.items():
#     print(key, file=sys.stderr)
#     print(value, file=sys.stderr)
#     request = requests.get(value)
#     content = request.content
#     result = BeautifulSoup(content, 'html.parser')
#     # print('result-------------->', result)
#     products = result.find_all("ul", {"id": "foo16"})
#     num_products = result.find(
#         "span", {"class": "search-res-number"}).get_text()
#     print('num_products-------------->', num_products, file=sys.stderr)
#     if int(num_products) < 1000:
#         print('number less than 1000', file=sys.stderr)
#         make_html_and_txt(key)
#     elif int(num_products) > 1000:
#         print('number greater than 1000', file=sys.stderr)
#         make_html_and_txt(key)
#         value = additional_request(value)
#         print('value---------->', file=sys.stderr)
#         request = requests.get(value)
#         content = request.content
#         result = BeautifulSoup(content, 'html.parser')
#         products = result.find_all("ul", {"id": "foo16"})
#         make_html_and_txt(key, 'ab+')

# make_html_and_txt('dumb name')

# path = Path("auto_product_html_2")

# file_to_open = path / "dumby.txt"

# f = open(file_to_open)

# print(f.read())

for key, value in links.items():
    print(key, file=sys.stderr)
    print(value, file=sys.stderr)
    request = requests.get(value)
    content = request.content
    result = BeautifulSoup(content, 'html.parser')
    products = result.find_all("ul", {"id": "foo16"})
    num_products = result.find(
            "span", {"class": "search-res-number"}).get_text()
    print('num_products-------------->', num_products, file=sys.stderr)
    if int(num_products) < 1000:
        print('number less than 1000', file=sys.stderr)
        make_html_and_txt(key)
    elif int(num_products) > 1000:
        print('number greater than 1000', file=sys.stderr)
        make_html_and_txt_over_1000(key, value=value)

    # make_html_and_txt(key)
    # value = additional_request(value)
    # print('value---------->', value, file=sys.stderr)
    # request = requests.get(value)
    # content = request.content
    # result = BeautifulSoup(content, 'html.parser')
    # products = result.find_all("ul", {"id": "foo16"})
    # make_html_and_txt(key, 'ab+')