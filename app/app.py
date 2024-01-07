from flask import Flask, render_template, request, Response
from pymongo import MongoClient
from bson import ObjectId
import sys
import os
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *

app = Flask(__name__)

client = MongoClient(DB_URI)
db = client[DB_NAME]
collection = db[DB_COLLECTION_NAME]
list_nhucau = ["gaming", "lapTrinh", "vanPhong", "doHoa", "doanhNhan"]
fields = {"Name":1, "Release date":1, "Price":1, "Processor (CPU)":1, "Graphics card (GPU)":1, "Memory (RAM)":1, "Screen size":1, "Screen resolution":1, "Weight":1,"Hard drives":1,"Size (length x width x height)":1, "Operating system (OS)":1,"_id":0}
record_limit = 10

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit-your-choice', methods=['POST'])
def submit_choice():
    nhu_cau = request.form.getlist('nhuCau')
    hang = request.form.get('hang')
    gia = request.form.get('gia')
    size = request.form.get('windowsize')

    query = {x: 1 for x in nhu_cau}
    if hang:
        query['Name'] = re.compile(hang, re.IGNORECASE)

    if gia:
        gia_min, gia_max = [int(x) for x in gia.split(',')]
        query['Price'] = {'$gte': gia_min*1000000, '$lt': gia_max*1000000}

    if size:
        size_min, size_max = [float(x) for x in size.split(',')]
        query['Screen size'] = {'$gte': size_min, '$lt': size_max}

    count = collection.count_documents(query)

    results = collection.find(query, fields).limit(record_limit)
    results_list = list(results)

    return render_template('results.html', results=results_list, count=count)

if __name__ == '__main__':
    app.run(debug=True)
