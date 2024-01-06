from pymongo import MongoClient
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *

client = MongoClient(DB_URI) 
db = client[DB_NAME] 
collection = db[DB_COLLECTION_NAME]

def random_binary():
    return random.randint(0, 1)

for document in collection.find():
    collection.update_one(
        {'_id': document['_id']},
        {'$set': {
            'gaming': random_binary(), 
            'lapTrinh': random_binary(), 
            'vanPhong': random_binary(), 
            'doHoa': random_binary(), 
            'doanhNhan': random_binary()
        }}
    )


# result = collection.update_many(
#     {},
#     { '$unset': {
#         'gaming': "", 
#         'lapTrinh': "", 
#         'vanPhong': "", 
#         'doHoa': "", 
#         'doanhNhan': ""
#     }}
# )
