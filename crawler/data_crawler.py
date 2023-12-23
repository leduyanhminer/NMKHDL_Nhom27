import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import sys
from link_crawler import link_crawler

client = MongoClient('mongodb://localhost:27017/')  # Thiết lập kết nối với MongoDB
db = client['laptop_database']
collection = db['products']

def data_crawler(url):
    data = {}
    required_info = ['Image', 'Processor (CPU)', 'Memory (RAM)', 'Screen size', 'Screen resolution', 'Weight', 'Size (length x width x height)', 'Operating system (OS)', 'Release date', 'Amazon.com Lowest New Price']
    for info in required_info:
        data[info] = None
    response = requests.get(url)
    if response.status_code != 200:
        print('Không thể truy cập trang!')
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    img_tag = soup.find('picture').find('img')
    if img_tag:
        img_url = img_tag['src']
        image_data = download_image(img_url)
        if image_data:
            data['Image'] = image_data
    
    name = soup.find('thead').find('th').get_text(strip=True)
    data['Name'] = name
    rows = soup.find('tbody').find_all('tr')

    for i in range(0, len(rows), 2):
        td = rows[i].find('td', class_='table-title')
        if td:
            title = td.get_text(strip=True).split('?')[0]
            if title in required_info:  # Kiểm tra xem tiêu đề có trong required_info không
                value = rows[i+1].find('td').get_text(strip=True)
                data[title] = value
    collection.insert_one(data)

def download_image(img_url):
    response = requests.get(img_url, stream=True)
    if response.status_code == 200:
        return response.content
    else:
        return None
    
#Crawl từ đây
product_links = link_crawler()

process = 0
total = len(product_links)
for link in product_links:
    data_crawler(link)
    process += 1
    progress = (process / total) * 100
    sys.stdout.write(f'\rTiến độ: {progress:.2f}%')
    sys.stdout.flush()
