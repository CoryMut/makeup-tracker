from bs4 import BeautifulSoup
import requests
import shutil
from pathlib import Path

def get_text(file, name):
    with open(f'{file}', 'r') as f:
        # f = open('covergirl_lips.html', 'r')

        output = f.read()

        result = BeautifulSoup(output, 'html.parser')

        all_ids = result.find_all('span', {'class': 'prod-id'})

        # all_face_ids = []

        file = open(f"{name}.txt", 'w+')

        for _id in all_ids:
            product_id = _id.get_text().strip()
            # all_face_ids.append(product_id)
            file.write(f"{product_id}\n")

    file.close()


# def combine_product_file():
#     with open('auto_products.txt', 'wb') as wfd:
#         for f in ['auto_product_txt/all_face.txt', 'auto_product_txt/all_eyes.txt', 'auto_product_txt/all_lips.txt']:
#             with open(f, 'rb') as fd:
#                 shutil.copyfileobj(fd, wfd)
#                 wfd.write(b"\n")

def combine_product_file(file_name, file_type, *args):
    with open(f'{file_name}.{file_type}', 'wb') as wfd:
        for f in args:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
                wfd.write(b"\n")


# combine_product_file('auto_product_txt_2/all_face.txt', 'auto_product_txt_2/all_eyes.txt', 'auto_product_txt_2/all_lips.txt')
# combine_product_file('all_products2','html','auto_product_html_2/all_face.html', 'auto_product_html_2/all_eyes.html', 'auto_product_html_2/all_lips.html')


def check_new_products():
    main = set()
    new = set()

    filename_main = Path('auto_products.txt')

    filename_new = Path('auto_products2.txt')

    with open(filename_main, 'r') as f: 
        for line in f:
            main.add(line)

    with open(filename_new, 'r') as f:
        for line in f:
            new.add(line)

    to_be_added = new.difference(main)
    dropped_products = main.difference(new)
    print(to_be_added)


check_new_products()
# def get_all_face_text():
#     with open('all_face_makeup.html', 'r') as f:
#         # f = open('covergirl_lips.html', 'r')

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_ids = result.find_all('span', {'class': 'prod-id'})

#         all_face_ids = []

#         file = open("all_face_ids.txt", 'w+')

#         for _id in all_ids:
#             product_id = _id.get_text().strip()
#             # all_face_ids.append(product_id)
#             file.write(f"{product_id}\n")

#     file.close()


# def get_all_eyes_text():
#     with open('all_eye_makeup.html', 'r') as f:
#         # f = open('covergirl_lips.html', 'r')

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_ids = result.find_all('span', {'class': 'prod-id'})

#         all_face_ids = []

#         file = open("all_eyes_ids.txt", 'w+')

#         for _id in all_ids:
#             product_id = _id.get_text().strip()
#             # all_face_ids.append(product_id)
#             file.write(f"{product_id}\n")

#     file.close()


# def get_all_lips_text():
#     with open('all_lip_makeup.html', 'r') as f:
#         # f = open('covergirl_lips.html', 'r')

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_ids = result.find_all('span', {'class': 'prod-id'})

#         all_face_ids = []

#         file = open("all_lips_ids.txt", 'w+')

#         for _id in all_ids:
#             product_id = _id.get_text().strip()
#             # all_face_ids.append(product_id)
#             file.write(f"{product_id}\n")

#     file.close()


# def get_lipsticks_text():
#     with open('all_lipsticks.html', 'r') as f:
#         # f = open('covergirl_lips.html', 'r')

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_ids = result.find_all('span', {'class': 'prod-id'})

#         all_face_ids = []

#         file = open("all_lipsticks.txt", 'w+')

#         for _id in all_ids:
#             product_id = _id.get_text().strip()
#             # all_face_ids.append(product_id)
#             file.write(f"{product_id}\n")

#     file.close()


# def get_lipgloss_text():
#     with open('all_lipgloss.html', 'r') as f:
#         # f = open('covergirl_lips.html', 'r')

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_ids = result.find_all('span', {'class': 'prod-id'})

#         all_face_ids = []

#         file = open("all_lipgloss.txt", 'w+')

#         for _id in all_ids:
#             product_id = _id.get_text().strip()
#             # all_face_ids.append(product_id)
#             file.write(f"{product_id}\n")

#     file.close()


# def get_balms_text():
#     with open('all_treatments_and_balms.html', 'r') as f:
#         # f = open('covergirl_lips.html', 'r')

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_ids = result.find_all('span', {'class': 'prod-id'})

#         all_face_ids = []

#         file = open("all_treats_and_balms.txt", 'w+')

#         for _id in all_ids:
#             product_id = _id.get_text().strip()
#             # all_face_ids.append(product_id)
#             file.write(f"{product_id}\n")

#     file.close()


# def get_lip_liners_text():
#     with open('all_lip_liners.html', 'r') as f:
#         # f = open('covergirl_lips.html', 'r')

#         output = f.read()

#         result = BeautifulSoup(output, 'html.parser')

#         all_ids = result.find_all('span', {'class': 'prod-id'})

#         all_face_ids = []

#         file = open("all_lip_liners.txt", 'w+')

#         for _id in all_ids:
#             product_id = _id.get_text().strip()
#             # all_face_ids.append(product_id)
#             file.write(f"{product_id}\n")

#     file.close()
