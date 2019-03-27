import csv
import json

json_data = []
with open('carlisle_products.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        json_data.append(row[0])

print(json.dumps(json_data))
