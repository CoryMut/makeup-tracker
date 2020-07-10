from bs4 import BeautifulSoup


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