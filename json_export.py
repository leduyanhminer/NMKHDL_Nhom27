from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['laptop_database_new']
collection = db['products']
documents = collection.find()
data_to_export = []
for document in documents:
    document.pop('Image', None)
    data_to_export.append(document)

# Xuất dữ liệu ra file JSON
with open('laptop_data.json', 'w', encoding='utf-8') as file:
    json.dump(data_to_export, file, default=str)
