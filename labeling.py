from pymongo import MongoClient
import pandas as pd
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *
from bson import ObjectId

client = MongoClient(DB_URI) 
db = client[DB_NAME] 
collection = db[DB_COLLECTION_NAME]

df = pd.read_csv('model/laptop_final.csv')

# collection.update_many(
#     {},
#     {'$set': {
#         'gaming': None, 
#         'lapTrinh': None, 
#         'vanPhong': None, 
#         'doHoa': None, 
#         'doanhNhan': None
#     }}
# )

for index, row in df.iterrows():
    collection.update_one(
        {'_id': ObjectId(row['_id'])},
        {'$set': {
            'gaming': row['Game'], 
            'lapTrinh': row['Lap Trinh'], 
            'vanPhong': row['Van Phong'], 
            'doHoa': row['Do Hoa'], 
            'doanhNhan': row['Doanh Nhan']
        }}
    )