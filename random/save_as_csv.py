import json
import requests
import csv


company = input("Company? (carlisle or etcetera) -> ")
season = input("Season? (ACS) -> ")

api_url_base = f"https://api.carlisleny.com/v1/product/{company}/{season}"


response = requests.get(api_url_base)

products = json.loads(response.content.decode('utf-8'))


# open a file for writing

file_name = f"./{company}_products.csv"
product_data = open(file_name, 'w')

# create the csv writer object

csvwriter = csv.writer(product_data)


def format_for_csv(product):
    data_to_write = [
        product['style'],
        product['name'],
        product['category'],
        round(float(product['price']), 2),
        get_size_range(product['size_scale']),
        get_config_size(product['sample_set_configs'], 'a'),
        get_config_size(product['sample_set_configs'], 'b'),
        get_config_size(product['sample_set_configs'], 'c'),
        get_config_size(product['sample_set_configs'], 'd'),
        get_config_size(product['sample_set_configs'], 'e'),
        get_config_size(product['sample_set_configs'], 'f'),
    ]

    return data_to_write


def get_size_range(sizes):
    if len(sizes) == 0:
        return ""
    elif len(sizes) == 1:
        return sizes.pop()

    return f"{sizes[0]}-{sizes[-1]}"


def get_config_size(config, letter):

    if type(config) is dict:
        return config.get(letter)


# open current order
json_file = f"{company}.json"
with open('./random/' + json_file) as f:
    data = dict(json.load(f))

headers = ['style','name', 'category', 'price', 'size_scale', 'A', 'B', 'C', 'D', 'E', 'F']
csvwriter.writerow(headers)
for style in data['style']:

    if products.get(style):
        csvwriter.writerow(format_for_csv(products[style]))
    else:
        csvwriter.writerow([style, 'missing'])

product_data.close()
