from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# Cấu hình cho webdriver
service = Service('D:\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Mở trang web
driver.get('https://laptopmedia.com/top-laptop-cpu-ranking/')
time.sleep(3)  # Đợi để trang web tải xong

# Thu thập dữ liệu CPU
cpu_data = {}
rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
for i in range(1, len(rows), 2):
    tds = rows[i].find_elements(By.TAG_NAME, 'td')
    name = tds[1].text
    value = tds[2].text
    cpu_data[name] = value

# Đóng trình duyệt
driver.quit()

# Chuyển dữ liệu thành DataFrame và xuất ra CSV
df = pd.DataFrame(list(cpu_data.items()), columns=['CPU Name', 'Value'])
df.to_csv('cpu_data.csv', index=False, encoding='utf-8')
