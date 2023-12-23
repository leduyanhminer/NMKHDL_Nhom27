# Bài Tập Lớn Nhóm 27: Nhập Môn Khoa Học Dữ Liệu

## **Mô Tả Dự Án**
Dự án này tập trung vào việc **crawl và lưu trữ dữ liệu laptop**, tạo cơ sở dữ liệu đa dạng để hỗ trợ người dùng trong việc tìm kiếm và nhận gợi ý về các sản phẩm laptop phù hợp.

## **Các Bước Thực Hiện**

### **Bước 1: Crawl Dữ Liệu**

#### **1.1 Lấy Danh Sách Link Laptop**
- **File**: `link_crawler.py`
- **Nguồn**: [Laptop vs Laptop](https://laptopvslaptop.com/laptop-finder)
- **Công cụ**: Selenium, Requests

#### **1.2 Thu Thập Thông Tin Laptop**
- **File**: `data_crawler.py`
- **Lưu trữ**: MongoDB

### **Bước 2: Phân Loại và Gợi Ý**

- **Phân loại**: Mỗi laptop được gán đa nhãn dựa trên mục đích sử dụng (gaming, văn phòng, doanh nhân, lập trình, đồ họa, v.v.).
- **Machine Learning**: Sử dụng mô hình học máy để tự động gán nhãn cho các sản phẩm.
