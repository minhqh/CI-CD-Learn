# Cấu trúc file

## 1. Workflow (Quy trình tổng thể)
Đây là tầng cao nhất, đại diện cho toàn bộ file YAML của cậu. Một project có thể có nhiều Workflow chạy song song.

Ví dụ: Cậu có thể có một file test_code.yml (chỉ chạy test khi code đang phát triển) và một file deploy_production.yml (chỉ chạy khi đẩy code lên nhánh chính).

## 2. Triggers (Bộ kích hoạt)
Nằm ở ngay đầu file với từ khóa `on`:, đây là bộ phận "nghe ngóng" xem khi nào thì Workflow được phép chạy.

- Push/Pull Request: Kích hoạt khi có thay đổi mã nguồn.

- Schedule (Cron): Chạy theo giờ định sẵn. Rất hữu ích cho hệ thống AI nếu cậu muốn pipeline tự động lấy dữ liệu mới và huấn luyện lại mô hình vào lúc 2 giờ sáng mỗi Chủ nhật.

- Workflow_dispatch: Tạo một nút bấm trên giao diện GitHub để cậu kích hoạt thủ công khi cần.

## 3. Jobs (Các chuỗi nhiệm vụ)
Một Workflow bao gồm một hoặc nhiều Jobs. Mặc định, các Jobs sẽ chạy song song cùng lúc trên các Runner (máy ảo) khác nhau. Điều này giúp tiết kiệm thời gian cực kỳ hiệu quả.

Tuy nhiên, cậu có thể thiết lập tính phụ thuộc bằng từ khóa needs:.

- Job 1 (test_api): Chạy unit test cho các endpoint của FastAPI.

- Job 2 (test_model): Chạy test độ chính xác cho mô hình AI nhận diện (hai job này chạy song song).

- Job 3 (deploy_backend): Triển khai mã nguồn Django lên server. Job này phải được cấu hình needs: [test_api, test_model]. Nếu 1 trong 2 job đầu thất bại, Job 3 sẽ bị hủy ngay lập tức.

## 4. Steps & Actions (Các bước thực thi)
Bên trong mỗi Job là các Steps chạy tuần tự từ trên xuống dưới trên cùng một máy ảo.

- Run: Cho phép cậu gõ các lệnh terminal y như trên máy tính thật (ví dụ: pip install r-base, python manage.py makemigrations).

- Uses (Actions): Đây là "tinh hoa" của GitHub Actions. Thay vì tự viết lệnh cài đặt Python phức tạp, cậu gọi các đoạn mã đã được cộng đồng viết sẵn. Ví dụ uses: actions/setup-python@v4 sẽ tự động cài Python hoàn hảo vào máy ảo chỉ trong 1 giây.

## 5. Secrets và Artifacts (Bảo mật và Chia sẻ dữ liệu)
Đây là hai vũ khí bí mật khi làm việc thực tế:

- Secrets: Không bao giờ gõ thẳng mật khẩu database, API key hay SSH key vào file YAML (vì ai cũng đọc được code của cậu). Cậu sẽ lưu chúng trong phần Cài đặt (Settings) của GitHub, sau đó gọi ra bằng biến môi trường: ${{ secrets.DB_PASSWORD }}.

- Artifacts: Nhớ rằng mỗi Job chạy trên một máy ảo khác nhau. Nếu Job 1 huấn luyện xong mô hình và tạo ra file weights.pt, làm sao Job 2 có file đó để đóng gói? Cậu dùng lệnh upload-artifact ở Job 1 để tải file đó lên bộ nhớ tạm của GitHub, rồi dùng download-artifact ở Job 2 để lấy về dùng tiếp.