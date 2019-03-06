import json
import requests
from pprint import pprint
import csv



api_url_base = "https://api.carlisleny.com/v1/product/carlisle/k"


response = requests.get(api_url_base)

products = json.loads(response.content.decode('utf-8'))


# open a file for writing

product_data = open('./products.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(product_data)


def format_for_csv(product):
    data_to_write = [
        product['style'],
        product['name'],
        product['category'],
        product['price'],
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

    return f"{product['size_scale'][0]}-{product['size_scale'][-1]}"


def get_config_size(config, letter):

    if type(config) is dict:
        return config.get(letter)


for product in products.values():

      csvwriter.writerow(format_for_csv(product))

product_data.close()
