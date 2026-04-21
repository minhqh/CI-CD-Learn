# Cách triển khai lên Server 

## 1. Github Action giao tiếp với Server như thế nào?
- Server (VPS) nằm ở nơi, Github ở một nơi. Để Github có thể ra lệnh cho Server, nó cần "key". Giao thức chuẩn là SSH (Secure Shell).

- - Public Key(Ổ khóa ) : Để trên server 
- - Private Key(Chìa khóa) : Để ở trong Github Secrets 

- Khi pipeline chạy tới bước Deploy , Github sẽ dùng Private Key để đăng nhập vào server từ xa , y hết cá nhận đăng nhập bằng terminal `ssh user@ip_adress`.

## 2. Các Secrets cần thiết phải có trên Github
Trước khi viết file YAML, hãy nhắc nhở bản thân (ghi chú vào markdown) là phải vào mục `Settings > Secrets and variables > Actions` của repository để thêm 3 biến sau:

- `SERVER_HOST`: Địa chỉ IP của con VPS (Ví dụ: 192.168.1.100).

- `SERVER_USER`: Tên đăng nhập VPS (Ví dụ: root hoặc ubuntu).

- `SSH_PRIVATE_KEY`: Đoạn mã Private Key để đăng nhập.

## 3.Cấu trúc Job Deployment trong file YAML
Dưới đây là phần code YAML cậu sẽ nối tiếp vào bên dưới Job `build_and_push` (ở tệp số 04 hôm trước). Để thực thi SSH dễ dàng nhất, cộng đồng thường dùng một Action có sẵn tên là `appleboy/ssh-action`.

```YAML
deploy_to_server:
    needs: [build_and_push] # Bắt buộc phải build xong và có image mới được deploy
    runs-on: ubuntu-latest
    steps:
      - name: SSH vào Server và Triển khai
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          # Bên dưới là các lệnh Bash sẽ chạy TRỰC TIẾP trên Server của cậu
          script: |
            # 1. Kéo Image mới nhất từ Docker Hub về server
            docker pull ten_tai_khoan_cua_cau/ten_project:latest
            
            # 2. Dừng Container cũ đang chạy (nếu có)
            docker stop my_backend_app || true
            docker rm my_backend_app || true
            
            # 3. Chạy Container mới với Image vừa kéo về
            docker run -d --name my_backend_app -p 8000:8000 ten_tai_khoan_cua_cau/ten_project:latest
            
            # 4. Dọn dẹp các Image cũ để tránh đầy ổ cứng server
            docker image prune -f
```

## 4. Tổng kết luồng chạy thực tế
Hãy tưởng tượng cậu đang fix một bug cho backend của hệ thống chỉ cần làm thao tác duy nhất:
- 1.Gõ `git push origin main`.
- 2.Pha một cốc cà phê.
- 3.GitHub Actions sẽ tự động: Chạy pytest -> Pass -> Build Docker Image mới -> Đẩy lên Docker Hub -> SSH vào con VPS -> Dừng bản cũ -> Kéo bản mới về chạy.
- 4.Quay lại bàn làm việc, F5 trình duyệt và thấy backend đã được cập nhật bản mới nhất. Đó chính là sức mạnh tối thượng của CI/CD!