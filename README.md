# NoSpinNoWin — Trợ lý tra cứu lịch học & hạn nộp Discord (Track A2)

Thành viên, lớp và vai trò xem tại [TEAMS.md](TEAMS.md).

**Lát cắt sản phẩm:** Một học viên L3 · nhắn hỏi hạn nộp bài hoặc phòng học sắp tới trên Discord · trợ lý tra cứu kho thông báo và lịch chính thức rồi quyết định trả lời kèm mã trích dẫn thông báo mới nhất nếu khớp rõ ràng, hoặc từ chối đoán mò và tạo phiếu chuyển TA duyệt khi thiếu nguồn hay có thông báo mâu thuẫn · học viên nhận được thông tin chính xác để tự đối chiếu ngay (hoặc biết câu hỏi đã chuyển tới TA), không bị nhớ nhầm hạn hay đi nhầm phòng.

---

## Cài đặt & chạy thử

Hệ thống sử dụng Python 3.10 trở lên (mặc định dùng thư viện chuẩn của Python).

```bash
# Kiểm tra bộ câu thử, metric spec và định dạng TEAMS.md
python run.py check

# Chạy bản chạy thử tương tác (hiện đang ở chế độ giả lập cho CP1)
python run.py

# Các lệnh đánh giá và mô phỏng chi phí (dùng từ CP2–CP4)
python run.py eval --try
python run.py eval
python run.py score eval/run-1.csv
python run.py simulate --try
python run.py simulate
```

Nếu nối model thật qua API, tạo file `.env` từ `.env.example` và điền thông tin nhà cung cấp trước khi chạy `eval`.

## Cấu trúc mã nguồn của nhóm

- `codebase/agent.py`: Luồng xử lý chính `answer(text)`.
- `codebase/tools.py`: Các công cụ tra cứu thông báo/lịch và tạo phiếu chuyển TA (`@tool`).
- `codebase/ai.py`: Hàm gọi model duy nhất `call_model(system, user)`.
- `codebase/app.py`: Giao diện chạy thử qua dòng lệnh.

## Phần nào thật, phần nào giả

| Thành phần | Trạng thái | Ghi chú |
|---|---|---|
| Lời gọi AI ở quyết định trung tâm | Chế độ giả (CP1) | Đang giữ khung chạy giả cho CP1–CP2, sẽ nối model thật trước CP3 |
| Dữ liệu lịch & thông báo | Giả lập / mẫu | Dự kiến dùng bộ lịch `training-ops` giả lập kèm thông báo mẫu tự dựng (khai báo ở `data/DATA_CARD.md`) |

## Dùng AI vào việc gì

Ở giai đoạn CP1, nhóm sử dụng trợ lý AI để rà lại cấu trúc thư mục nộp bài đúng yêu cầu của đề và biên tập lại diễn đạt trong `canvas.md`, `spec.md` §0–§2 cho gọn rõ. Toàn bộ hướng bài toán, giả thuyết pain, lát cắt và phân công đều do 4 thành viên tự thống nhất và kiểm tra lại (chi tiết cập nhật tại [docs/ai-usage.md](docs/ai-usage.md)).
