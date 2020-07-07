from bs4 import BeautifulSoup
import requests
from txt_ids import get_text
import shutil

# all_face = requests.get(
#     'https://www.ulta.com/makeup-face?N=26y3&No=1000&Nrpp=1000')
# all_eyes = requests.get(
#     'https://www.ulta.com/makeup-eyes?N=26yd&No=1000&Nrpp=1000')
# all_lips = requests.get(
#     'https://www.ulta.com/makeup-lips?N=26yq&Nrpp=1000')

# <-------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->
# <-------------------------------LIPS--------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->

# lipsticks
# lipsticks = requests.get(
#     'https://www.ulta.com/makeup-lips-lipstick?N=26ys&Nrpp=1000')

# lipgloss
# lipgloss = requests.get(
#     'https://www.ulta.com/makeup-lip-gloss?N=26yt&Nrpp=1000')

# treatments and balms
# treatments_and_balms = requests.get(
#     'https://www.ulta.com/makeup-lips-treatments-balms?N=26yw&Nrpp=1000')

# lip liners
# lip_liners = requests.get(
#     'https://www.ulta.com/makeup-lip-liner?N=26yv&Nrpp=1000')

# sets and palettes
# sets_and_palettes = requests.get(
#     'https://www.ulta.com/makeup-lips-sets-palettes?N=26yr')

# lip stains
# lip_stains = requests.get(
#     'https://www.ulta.com/makeup-lip-stain?N=26yu')

# <-------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->
# <------------------------------EYES---------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->

# eyeshadow palettes
# request = requests.get(
#     'https://www.ulta.com/makeup-eyes-eyeshadow-palettes?N=26ye&Nrpp=1000')

# mascara
# request = requests.get(
#     'https://www.ulta.com/makeup-eyes-mascara?N=26yg&Nrpp=1000')

# eyeliner
# request = requests.get(
#     'https://www.ulta.com/makeup-eyes-eyeliner?N=26yh&Nrpp=1000')

# eyebrows
# request = requests.get(
#     'https://www.ulta.com/makeup-eyes-eyebrows?N=26yi&Nrpp=1000')

# eyeshadow
# request = requests.get(
#     'https://www.ulta.com/makeup-eyes-eyeshadow?N=26yf&Nrpp=1000')

# Eye Primer & Base
# request = requests.get(
#     'https://www.ulta.com/makeup-eye-primer-base?N=26yl')

# Eyelashes
# request = requests.get(
#     'https://www.ulta.com/makeup-eyes-eyelashes?N=26yj&Nrpp=1000')

# Eye Makeup Remover
# request = requests.get(
#     'https://www.ulta.com/makeup-eye-makeup-remover?N=26yk')

# Lash Primer & Serums
# request = requests.get(
#     'https://www.ulta.com/makeup-eyes-lash-primer-serums?N=jllzia')

# <-------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->
# <-------------------------------FACE--------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->
# <-------------------------------------------------------------------------------------------->

# Foundation
# request = requests.get(
#     'https://www.ulta.com/makeup-face-foundation?N=26y5&Nrpp=1000')

# Face Powder
# request = requests.get(
#     'https://www.ulta.com/makeup-face-powder?N=26y8&Nrpp=1000')

# Concealer
# request = requests.get(
#     'https://www.ulta.com/makeup-face-concealer?N=26y6&Nrpp=1000')

# Color Correcting
# request = requests.get(
#     'https://www.ulta.com/makeup-face-color-correcting?N=uo37yr')

# Face Primer
# request = requests.get(
#     'https://www.ulta.com/makeup-face-primer?N=26y4&Nrpp=1000')

# BB and CC Creams
# request = requests.get(
#     'https://www.ulta.com/makeup-face-bb-cc-creams?N=277u')

# Blush
# request = requests.get(
#     'https://www.ulta.com/makeup-face-blush?N=277v&Nrpp=1000')

# Bronzer
# request = requests.get(
#     'https://www.ulta.com/makeup-face-bronzer?N=26y9&Nrpp=1000')

# Highlighter
# request = requests.get(
#     'https://www.ulta.com/makeup-face-highlighter?N=27i0&Nrpp=1000')

# Contouring
# request = requests.get(
#     'https://www.ulta.com/makeup-face-contouring?N=27eh&Nrpp=1000')

# Setting Spray
# request = requests.get(
#     'https://www.ulta.com/makeup-face-setting-spray?N=10wj5jk&Nrpp=1000')

# Shine Control
# request = requests.get(
#     'https://www.ulta.com/makeup-face-shine-control?N=26yc&Nrpp=1000')

# Makeup Remover
request = requests.get(
    'https://www.ulta.com/makeup-face-makeup-remover?N=26yb&Nrpp=1000')


content = request.content
result = BeautifulSoup(content, 'html.parser')
products = result.find_all("ul", {"id": "foo16"})
# products = result.find_all("div", {"class": "ProductSwatches"})
# products = result.find("section", {"class": "ProductDetail__content"})


def make_html_and_txt(name):

    f = open(f'all_{name}.html', "ab+")

    for product in products:
        f.write(product.encode())
    # f.write(result.encode())
    f.close()

    get_text(f'all_{name}.html', f'all_{name}')

# print(products)
# print(result)


make_html_and_txt('all_products')
