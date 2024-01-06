# Bài Tập Lớn Nhóm 27: Nhập Môn Khoa Học Dữ Liệu

## **Mô Tả Dự Án**
Dự án này tập trung vào việc crawl và lưu trữ dữ liệu laptop trên MongoDB Atlas, tạo cơ sở dữ liệu để hỗ trợ người dùng trong việc tìm kiếm và nhận gợi ý về các sản phẩm laptop phù hợp.

## **Các Bước Thực Hiện**

### **Bước 1: Crawl Dữ Liệu**
**Công cụ**: Selenium, Requests
#### **1.1 Lấy Danh Sách Link Laptop**
- **File**: `link_crawler.py`
- **Nguồn**: [Laptop vs Laptop](https://laptopvslaptop.com/laptop-finder)

#### **1.2 Thu Thập Thông Tin Laptop**
- **File**: `data_crawler.py`
- **Lưu trữ**: MongoDB Atlas

#### **1.3 Thu Thập Thông Tin CPU**
- **File**: `cpu_crawler.py`
- **Nguồn**: [Top CPU Ranking](https://laptopmedia.com/top-laptop-cpu-ranking)

### **Bước 2: Phân Loại và Gợi Ý**
- **Phân loại**: Mỗi laptop được gán đa nhãn dựa trên mục đích sử dụng (gaming, văn phòng, doanh nhân, lập trình, đồ họa, v.v.).
- **Machine Learning**: Sử dụng mô hình học máy để tự động gán nhãn cho các sản phẩm.
- **Lưu trữ và xử lý**: Sử dụng MongoDB Atlas để lưu trữ dữ liệu và phân loại.

### **Bước 3: Tạo Web Local và Kết Nối MongoDB Atlas**
- **Framework**: Flask
- **Công nghệ**: HTML, CSS, Python
- **Chức năng**: Hiển thị danh sách laptop, tìm kiếm, lọc dữ liệu
- **Triển khai**: Localhost

## **Cách Sử Dụng**
1. Clone repo, cài đặt dependencies.
2. Cấu hình kết nối MongoDB Atlas.
3. Chạy các script crawl dữ liệu (`link_crawler.py`, `data_crawler.py`, `cpu_crawler.py`).
4. Khởi động Flask app, truy cập `localhost` qua browser.

## **Yêu Cầu Hệ Thống**
- Python 3.x, Flask
- MongoDB Atlas
- Thư viện Python: `pymongo`, `requests`, `selenium`, v.v.
