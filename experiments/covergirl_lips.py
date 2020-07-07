from bs4 import BeautifulSoup
import requests

covergirl_lips = requests.get(
    'https://www.ulta.com/brand/covergirl-makeup-lips?N=1z12dplZ26yq')


content = covergirl_lips.content
result = BeautifulSoup(content, 'html.parser')
products = result.find_all("ul", {"id": "foo16"})

f = open('covergirl_lips.html', "wb")

for product in products:
    f.write(product.encode())

f.close()

# print(products)
# print(result)
