# Định nghĩa

## 1. CI / CD là gì ?

CI (Continuous Integration) : Là việc tự động hóa khâu kiểm tra mỗi khi đắp thêm code mới.

CD (Continuous Delivery/Deployment) :  Là việc tự động hóa đưa sản phầm ra ngoài thị trường.

## 2. Tại sao lại cần CI/CD?

Mỗi khi cần cập nhật code lên thì sẽ tự động kiểm tra chạy được không và cập nhật trực tiếp lên sản phẩm mà không cân tự đồng build lại không cần trực tiếp phải chỉnh sửa.

## 3. Các trụ cột chính

- CI : Build -> Unit Test -> Integration Test

- CD1 (Continuous Delevry) : Code sẵn sàng deploy nhưng vẫn cần xác thực 1 nút bấm của người

-- CD2 (Continuous Deployment) : Code tự động deploy lên server sau khi pass hết các bài test.