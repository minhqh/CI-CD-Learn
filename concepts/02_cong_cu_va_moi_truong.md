# Công cụ và Môi trường

## 1. File cấu hình CI/CD nằm ở đâu?
CI/CD hiện đại không cần click chuột trên web mà được viết thẳng bằng code và lưu trong cùng với repository chữa project luôn.

- Với Github Action : File cấu hình nằm trong thư mục ẩn `.github/workflows/`

- Với GitLab CI/CD : Sẽ là 1 file tên là   `.gitlab-ci.yml`

## 2. Ngôn ngữ được dùng:

- YAML (Yet Another Markup Language) : Ngôn ngữ chính. Dùng để viết định nghĩa các bước , công việc, khi nào chạy trigger. Làm theo cơ chế thụt dòng (giống Python).

- Bash/Shell Scripts : Khi chạy pipeline, để ra lệnh clone code, cài đặt thự viên hay build Docker  thì cần viết các lệnh terminal (Linux) bên trọng file YAML.

- Ngôn ngữ của Project:Không biết tự test cần gọi qua các thư mục test do mình tạo.

## 3. Cách hoạt động

- Runner : Khi có code mới được push lên, GitHub/GitLab sẽ cấp cho cậu một máy ảo (thường là Ubuntu Linux) hoàn toàn mới, sạch sẽ và trống rỗng. Máy ảo này gọi là Runner. Tuổi thọ của nó chỉ kéo dài từ lúc pipeline bắt đầu đến khi kết thúc. Xong việc là nó tự hủy.

- Containers (Docker):
Vì Runner là một máy trống, cậu sẽ phải cài lại từ đầu (Python, PyTorch, Django...). Thay vì cài thủ công, người ta thường dùng Docker để gói sẵn môi trường, sau đó bảo Runner kéo (pull) Docker image đó về và chạy. Điều này đảm bảo môi trường trên CI/CD giống hệt môi trường trên máy tính của cậu và server thực tế.

Ví dụ 1 mẫu  YAML cơ bản:
``` YAML
# Tên của Pipeline
name: Backend CI

# 1. Khi nào thì chạy? (Triggers)
on:
  push:
    branches: [ "main" ] # Chạy khi có code push lên nhánh main

# 2. Làm những việc gì? (Jobs)
jobs:
  test_model_and_api:
    # 3. Môi trường nào? (Runners)
    runs-on: ubuntu-latest

    # 4. Các bước thực hiện (Steps)
    steps:
    - name: Lấy code từ repository về máy Runner
      uses: actions/checkout@v3

    - name: Cài đặt Python 3.10
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Cài đặt thư viện
      run: |
        pip install -r requirements.txt
        pip install pytest

    - name: Chạy bài test kiểm tra API
      run: |
        pytest tests/
```