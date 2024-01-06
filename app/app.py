from flask import Flask, render_template, request
from pymongo import MongoClient
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *

app = Flask(__name__)

client = MongoClient(DB_URI)
db = client[DB_NAME]
collection = db[DB_COLLECTION_NAME]
list_nhucau = ["gaming", "lapTrinh", "vanPhong", "doHoa", "doanhNhan"]
fields = {"Name":1, "Release date":1, "Amazon.com Lowest New Price":1, "_id":0}
record_limit = 10

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit-your-choice', methods=['POST'])
def submit_choice():
    nhu_cau = request.form.getlist('nhuCau') # list các nhu cầu
    hang = request.form.get('hang')
    gia = request.form.get('gia')
    size = request.form.get('windowsize')

    query = {
        x: 1 for x in list_nhucau if x in nhu_cau 
    }

    results = collection.find(query, fields).limit(record_limit)
    results_list = list(results)

    return render_template('results.html', results=results_list)

if __name__ == '__main__':
    app.run(debug=True)
