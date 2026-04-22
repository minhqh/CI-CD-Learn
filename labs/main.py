from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Tại sao m lại kêu là ghê? M phán xét t đúng không"}

@app.get("/process/{data_id}")
def process_data(data_id: int):
    # Giả lập logic xử lý: nếu ID chẵn thì hợp lệ, lẻ thì báo lỗi
    if data_id % 2 == 0:
        return {"status": "success", "data_id": data_id}
    return {"status": "error", "message": "Invalid ID"}
