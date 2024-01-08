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
Trong bước này, nhóm tiến hành làm sạch và chuẩn hóa dữ liệu đã thu thập. Tiếp theo, nhóm tiến hành gán nhãn cho một phần các laptop dựa trên các tính năng và mục đích sử dụng. Sau đó, nhóm sử dụng ba mô hình học máy khác nhau - KNN, RandomForest và MLP - để huấn luyện và so sánh hiệu suất dựa trên thang đo F1-Score. Cuối cùng, nhóm đã chọn mô hình MLP (Multi-Layer Perceptron) như là mô hình tốt nhất để tự động gán nhãn cho các laptop còn lại.
- **Phân loại**: Mỗi laptop được gán đa nhãn dựa trên mục đích sử dụng (gaming, văn phòng, doanh nhân, lập trình, đồ họa, v.v.).
- **Machine Learning**: MLP với các tầng FullyConnected và lớp cuối cùng sử dụng activation sigmoid để phân loại. (Chi tiết trong model/train.ipynb), mô hình được lưu trong model/model.h5
- **Lưu trữ và xử lý**: Sử dụng MongoDB Atlas để lưu trữ dữ liệu và phân loại.


### **Bước 3: Tạo Web Local và Kết Nối MongoDB Atlas**
- **Framework**: Flask
- **Công nghệ**: HTML, CSS, Python
- **Chức năng**: Hiển thị danh sách laptop, tìm kiếm, lọc dữ liệu theo nhu cầu, hãng, giá, kích thước màn.
- **Triển khai**: Localhost

## **Cách Sử Dụng**
1. Clone repo, cài đặt dependencies.
2. Cấu hình kết nối MongoDB Atlas.
3. Chạy các script crawl dữ liệu (`link_crawler.py`, `data_crawler.py`, `cpu_crawler.py`).
4. Train/sửa lại mô hình trong phần model/train.ipynb
5. Khởi động Flask app, truy cập `localhost` qua browser.

## **Yêu Cầu Hệ Thống**
- Python 3.x, Flask
- MongoDB Atlas
- Thư viện Python: pip install -r requirements.txt
