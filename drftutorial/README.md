# Django REST Framework Tutorial

##  Giới thiệu

Dự án này là một API đơn giản được xây dựng bằng Django REST Framework, cho phép người dùng quản lý các đoạn mã (snippets) với các tính năng như tạo, xem, cập nhật và xóa.

##  Cài đặt

1. **Clone dự án:**
   ```bash
   git clone -b drftutorial  https://github.com/thaovothu/ChuyenDeCongNghe.git
   cd drftutorial

2. **Cài môi trường ảo:**
    ```bash
    python3 -m venv env
    source env/bin/activate

3. **Cài đặt các gói phụ thuộc**
    ```bash
    pip install -r requirements.txt

4. **Áp dụng các migrations**
    ```bash
    python manage.py migrate

5. **Tạo người dùng siêu quản trị**
    ```bash
    python manage.py createsuperuser

6. **Chạy máy chủ phát triển**
    ```bash
    python manage.py runserver


##  Kiểm tra API
1. **Danh sách các đoạn mã:**
    ```bash
    GET /snippets/

2. **Chi tiết một đoạn mã:**
    ```bash
    GET /snippets/{id}/

3. **Tạo một đoạn mã mới:**
    ```bash
    POST /snippets/

4. **Cập nhật một đoạn mã:**
    ```bash
    PUT /snippets/{id}/

5. ** Xóa một đoạn mã:**
    ```bash
    DELETE /snippets/{id}/

Để kiểm tra API của, có thể sử dụng các công cụ như:

- **Django REST Framework Browsable API:** Truy cập `http://127.0.0.1:8000/` trong trình duyệt của bạn để sử dụng giao diện người dùng web của DRF.

- **Postman:** Một công cụ mạnh mẽ để kiểm tra các API RESTful.

- **curl:** Một công cụ dòng lệnh để gửi các yêu cầu HTTP.

Ví dụ, để lấy danh sách các đoạn mã:

```bash
curl -X GET http://127.0.0.1:8000/snippets/