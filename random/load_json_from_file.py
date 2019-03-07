import json

from pprint import pprint


with open('./random/etcetera.json') as f:
    data = dict(json.load(f))


pprint(len(data["style"]))
