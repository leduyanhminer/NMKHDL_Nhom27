Bài Tập Lớn Nhóm 27: Nhập Môn Khoa Học Dữ Liệu
Mô Tả Dự Án
Dự án này tập trung vào việc crawl và lưu trữ dữ liệu laptop để tạo cơ sở dữ liệu phong phú, giúp người dùng có thể tìm kiếm và nhận gợi ý về các sản phẩm laptop phù hợp với nhu cầu của họ.

Bước 1: Crawl Dữ Liệu
Lấy Danh Sách Link Laptop
Sử dụng file link_crawler.py.
Trang web nguồn: Laptop vs Laptop
Công cụ: Selenium, Requests.
Thu Thập Thông Tin Laptop
Sử dụng file data_crawler.py.
Lưu trữ dữ liệu vào MongoDB.
Bước 2: Phân Loại và Gợi Ý
Mỗi laptop được gán đa nhãn dựa trên mục đích sử dụng: gaming, văn phòng, doanh nhân, lập trình, đồ họa, v.v.
Sử dụng mô hình Machine Learning để tự động gán nhãn cho các laptop còn lại.
