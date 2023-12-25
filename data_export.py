from pymongo import MongoClient
import json
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['laptop_database_25_12']
collection = db['products']
documents = collection.find()
data_to_export = []

for document in documents:
    document.pop('Image', None)  # Loại bỏ trường Image nếu có
    data_to_export.append(document)

# Xuất dữ liệu ra file JSON
with open('laptop_data.json', 'w', encoding='utf-8') as file:
    json.dump(data_to_export, file, default=str)

# Chuyển đổi dữ liệu sang DataFrame để xuất ra CSV
df = pd.DataFrame(data_to_export)

# Xuất dữ liệu ra file CSV
df.to_csv('laptop_data.csv', index=False, encoding='utf-8')
