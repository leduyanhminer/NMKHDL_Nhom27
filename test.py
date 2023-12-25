from pymongo import MongoClient

# Kết nối đến cơ sở dữ liệu nguồn
source_client = MongoClient('mongodb+srv://leduyanh:1@cluster0.z0bblpv.mongodb.net/')
source_db = source_client['laptop_database']
source_collection = source_db['products']

# Kết nối đến cơ sở dữ liệu đích
target_client = MongoClient('mongodb+srv://leduyanh:1@cluster0.z0bblpv.mongodb.net/')
target_db = target_client['laptop_database']
target_collection = target_db['products']

# Sao chép dữ liệu
for document in source_collection.find():
    # Bạn có thể thêm logic để chỉnh sửa dữ liệu tại đây nếu cần
    target_collection.insert_one(document)
