from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import *

def link_crawler():
    list_checkbox = ['12 inches or less', '13 inches', '14 inches', '15 inches', '16 inches', '17 inches or more']
    # list_checkbox = ['macOS']
    list_product_links = set()
    for checkbox in list_checkbox:
        links = crawl_with_checkbox(checkbox)
        list_product_links = list_product_links | links
    return list(list_product_links)

def crawl_with_checkbox(checkbox):
    # Khởi tạo WebDriver
    webdriver_service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=webdriver_service)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)

    # Truy cập trang
    driver.get(LAPTOP_WEB)

    # Chọn checkbox
    checkbox = wait.until(EC.element_to_be_clickable((By.ID, checkbox)))
    checkbox.click()

    while True:
        try:
            # Kéo xuống cuối trang
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Thêm thời gian chờ để trang tải
            # Tìm nút "Show more"
            show_more_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Show more')]")
            driver.execute_script("arguments[0].click();", show_more_button)
            time.sleep(2)
        except NoSuchElementException:    # Khi không tìm thấy nút "Show more"
            break                     

    # Lưu các link sản phẩm
    product_links = set()
    product_divs = driver.find_elements(By.CLASS_NAME, 'box-item')
    for div in product_divs:
        view_button = div.find_element(By.CSS_SELECTOR, 'a.button.button-minor')
        product_links.add(view_button.get_attribute('href'))

    driver.quit()
    return product_links

product_links = link_crawler()
with open('product_links.txt', 'w', encoding='utf-8') as file:
    for link in product_links:
        file.write(link + '\n')
