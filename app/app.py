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

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit-your-choice', methods=['POST'])
def submit_choice():
    nhu_cau = request.form.getlist('nhuCau') # list các nhu cầu
    hang = request.form.get('hang')
    gia = request.form.get('gia')

    return f'''
    <h1>Kết quả lựa chọn:</h1>
    <p>Nhu cầu: {nhu_cau}</p>
    <p>Hãng: {hang}</p>
    <p>Khoảng giá: {gia}</p>
    <a href="/">Quay lại</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
