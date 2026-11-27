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
| Lời gọi AI ở quyết định trung tâm | Chế độ giả (CP2) | Đã chạy thông toàn bộ luồng `codebase/agent.py` + `tools.py` qua `python run.py` và `eval --try 20` với `MODEL_PROVIDER=fake` (fallback bằng luật); sẽ nối model thật trong `codebase/ai.py` trước CP3 |
| Dữ liệu lịch & thông báo | Giả lập / mẫu | `data/schedules.json` (108 buổi từ `training-ops` giả lập BTC), `data/announcements.json` (18 thông báo mẫu) và `data/threads.json` (8 thread mẫu) — khai báo ở `data/DATA_CARD.md` |
| Bằng chứng pain & bộ câu thử | Thật (`n = 27`) / Khung chuẩn | Khảo sát `n = 27` người ngoài nhóm (`evidence/survey/results.csv`), `20` câu thử (`eval/benchmark.csv`) & `4` metric (`eval/metric_spec.yaml`), đã chấm thử chéo `4/5` (`eval/cham-thu.md`) |

## Dùng AI vào việc gì

Nhóm dùng trợ lý AI hỗ trợ chuẩn hoá dữ liệu mẫu từ bộ `training-ops`, viết script thống kê khảo sát `analyze_survey.py`, soạn nháp `spec.md` §3–§6/§9, khung code `codebase/tools.py`–`agent.py` và biên tập tài liệu CP1–CP2. Toàn bộ dữ liệu khảo sát `n = 27` đều thu từ người dùng thật ngoài nhóm, mọi mã nguồn `TB-xx`/`SCH-xx`, câu thử và chấm chéo đều do các thành viên trực tiếp kiểm chứng (chi tiết tại [docs/ai-usage.md](docs/ai-usage.md)).
