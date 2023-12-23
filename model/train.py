from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['product_database']
collection = db['products']

data = collection.find()

df = pd.DataFrame(list(data))
print(df)
