from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def cpu_crawler():
    service = Service('D:\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    driver.get('https://laptopmedia.com/top-laptop-cpu-ranking/')
    time.sleep(3)
    cpu_data = {}
    rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
    for i in range(1, len(rows), 2):
        tds = rows[i].find_elements(By.TAG_NAME, 'td')
        name = tds[1].text
        value = tds[2].text
        cpu_data[name] = value

    driver.quit()
    return cpu_data
