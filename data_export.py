from pymongo import MongoClient
import json
import pandas as pd

client = MongoClient('mongodb+srv://leduyanh:1@cluster0.z0bblpv.mongodb.net/')
db = client['laptop_database_final']
collection = db['products']
documents = collection.find()
data_to_export = []

for document in documents:
    document.pop('Image', None)
    data_to_export.append(document)

with open('laptop_data.json', 'w', encoding='utf-8') as file:
    json.dump(data_to_export, file, default=str)

df = pd.DataFrame(data_to_export)

df.to_csv('laptop_data_raw.csv', index=False, encoding='utf-8')
