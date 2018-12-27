# NODEJS - FLASK -> REST API
NodeJS gửi dữ liệu sau khi bắt đầu hành động, Dữ liệu truyền REALTIME với MQTT Protocol.
Flask Server nhận giá trị và trả về giá trị PREDICT (dự đoán) với MODEL đã training.

# RUN FLASK SERVER
Chạy với ENV -> Python3
python3 app.py

### Request

`GET /get-file?filename=abc.txt`

Tham số yêu cầu

| Thuộc tính   | Mô tả    | Kiểu   | Ví Dụ         |
| ------------ | -------------- | ------ | --------------- |
| filename        | file_send   | file   | test.txt |
