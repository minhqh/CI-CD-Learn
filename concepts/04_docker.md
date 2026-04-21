## DOCKER

# 1. Docker là gì? Tại sao cần docker?

- Docker để đóng gói tất cả toàn bộ code, thư viện và cả hệ điều hành thành một khối duy nhất. Khôi này khi đem đi sử dụng thì sử dụng được như nhau.

-  Lý do, Docker cần thiết được sử dụng là bởi vì đề đống nhất code chạy được như nhau tại mọi nơi.

## 2. Các khái niệm cần phải nhớ

-  `Dockerfile` : Là file chứa các lệnh để hướng dẫn đóng gói các ứng dụng. 

- `Image` : Là một bản tĩnh, được tạo ra dựa trên Dockerfile để build ra một bản không chạy mà chia sẻ và lưu trữ.

- `Container` : Là lúc đem image ra chạy, một image có thể tạo hàng trăm Container chạy song song độc lập.

- `Registry` : Nơi chưa các image (giống github chưa code). Ví dụ điên hình Docker Hub hoặc Github Container Registry (GHCR).

## 3. Cấu trúc một file Dockerfile chuẩn 

- File này không có đuôi, thường có tên là `Docketfile` và đặt cùng ở thư mục gốc của dự án.

- Vi dụ một cấu trúc:

``` docker
# 1. Chọn hệ điều hành nền (Base Image) - Dùng bản slim cho nhẹ
FROM python:3.10-slim

# 2. Tạo thư mục làm việc bên trong Container
WORKDIR /app

# 3. Copy file cấu hình thư viện vào trước (để tận dụng cache của Docker)
COPY requirements.txt .

# 4. Cài đặt thư viện
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ mã nguồn của cậu vào Container
COPY . .

# 6. Mở cổng mạng (Ví dụ FastAPI hay chạy cổng 8000)
EXPOSE 8000

# 7. Lệnh khởi chạy ứng dụng khi Container bắt đầu
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

```


## 4. Cách kết nối Docker với pipeline(Github Action)
- Trong file cấu hình YAML (`.github/workflows/...`), cậu sẽ thêm một Job mới chạy sau khi Job Test đã Pass (màu xanh). Nhiệm vụ của Job này là gõ lệnh build cái Dockerfile kia thành Image, rồi đẩy nó lên siêu thị Docker Hub.

```YAML
build_and_push:
    needs: [test_api] # Chỉ chạy khi test đã pass
    runs-on: ubuntu-latest
    steps:
      - name: Lấy mã nguồn
        uses: actions/checkout@v3

      - name: Đăng nhập vào Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKER_USERNAME }} # Lấy từ bí mật
          password: ${{ secrets.DOCKER_PASSWORD }} # Lấy từ bí mật

      - name: Build và Đẩy Image lên Docker Hub
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ten_tai_khoan_cua_cau/ten_project:latest
```