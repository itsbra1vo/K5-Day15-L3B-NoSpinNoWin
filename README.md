# NoSpinNoWin — Trợ lý tra cứu lịch học & hạn nộp Discord (Track A2)

Thành viên, lớp và vai trò xem tại [TEAMS.md](TEAMS.md).

**Lát cắt sản phẩm:** Một học viên L3 · nhắn hỏi hạn nộp bài hoặc phòng học sắp tới trên Discord · trợ lý tra cứu kho thông báo và lịch chính thức rồi quyết định trả lời kèm mã trích dẫn thông báo mới nhất nếu khớp rõ ràng, hoặc từ chối đoán mò và tạo phiếu chuyển TA duyệt khi thiếu nguồn hay có thông báo mâu thuẫn · học viên nhận được thông tin chính xác để tự đối chiếu ngay (hoặc biết câu hỏi đã chuyển tới TA), không bị nhớ nhầm hạn hay đi nhầm phòng.

---

## Cài đặt & chạy thử

Hệ thống sử dụng Python 3.10 trở lên (mặc định dùng thư viện chuẩn của Python).

```bash
# Kiểm tra bộ câu thử, metric spec và định dạng TEAMS.md
python run.py check

# Chạy bản chạy thử tương tác (gọi AI thật qua .env; chưa có .env sẽ chạy chế độ giả)
python run.py

# Các lệnh đánh giá và mô phỏng chi phí (thêm --wait 4 nếu dùng gói miễn phí giới hạn lượt/phút)
python run.py eval --try --wait 4
python run.py eval --wait 4
python run.py score eval/run-1.csv
python run.py score eval/run-2.csv
python run.py simulate --try --wait 4
python run.py simulate --rate-from eval/run-2.csv --wait 4
```

Để chạy bản gọi AI thật: chép `.env.example` thành `.env` (`Copy-Item .env.example .env` trên Windows hoặc `cp .env.example .env` trên macOS/Linux) rồi điền 3 dòng (`MODEL_PROVIDER=gemini`, `MODEL_NAME=gemini-3.1-flash-lite`, `API_KEY=<key của nhóm>` — khuyến nghị thêm `THINKING_BUDGET=0`). File `.env` đã nằm trong `.gitignore`, tuyệt đối không commit.

## Cấu trúc mã nguồn của nhóm

- `codebase/agent.py`: Luồng xử lý chính `answer(text)` (Workflow 3 bước cố định + `guard()` hậu kiểm).
- `codebase/tools.py`: Các công cụ tra cứu thông báo/lịch/thread và tạo phiếu nháp chuyển TA (`@tool`).
- `codebase/ai.py`: Hàm gọi model duy nhất `call_model(system, user, json_mode)` dùng REST chuẩn của Gemini (`urllib`).
- `codebase/app.py`: Giao diện chạy thử qua dòng lệnh.

## Phần nào thật, phần nào giả

| Thành phần | Trạng thái | Ghi chú |
|---|---|---|
| Lời gọi AI ở quyết định trung tâm & mô phỏng chi phí | **Thật (CP3–CP4)** | Đã nối Gemini REST API thật trong `codebase/ai.py` (`x-goog-api-key`, `temperature=0`, `json_mode=True`). Chạy Lượt 1 trên `gemini-3.5-flash-lite` (`run-1@20261128-080232`: `17/20 = 85%`), cải tiến sang Lượt 2 trên `gemini-3.1-flash-lite` (`run-2@20261128-090447`: `19/20 = 95%`, **đạt chuẩn CP2**), và mô phỏng 50 phiên thật ở CP4 (`simulate-1@20261128-093336`: `$0.00090`/task thành công, `$2.28`/tháng cơ sở 700 người, **GO** trong `cost/cost-estimate.md`). Khi chưa điền `.env`, code tự lùi về chế độ giả (`MODEL_PROVIDER=fake`) chỉ để kiểm luồng. |
| Dữ liệu lịch & thông báo | Giả lập / mẫu | `data/schedules.json` (108 buổi từ `training-ops` giả lập BTC), `data/announcements.json` (18 thông báo mẫu) và `data/threads.json` (8 thread mẫu) — khai báo chi tiết ở `data/DATA_CARD.md`. |
| Bằng chứng pain & bộ câu thử | **Thật (2 nguồn)** / Khung chuẩn | Đủ 2 nguồn thật đối chiếu chéo: khảo sát `n = 27` (`evidence/survey/results.csv`) và đào kênh Discord công khai `#💬-chung` `N = 50` (`evidence/data-mining.md`, 12 trích dẫn ẩn danh); `20` câu thử (`eval/benchmark.csv`, `7/20 = 35%` `nguoi_dung`), `4` metric (`eval/metric_spec.yaml`), chấm chéo `4/5` (`eval/cham-thu.md`). |

## Dùng AI vào việc gì

Nhóm dùng trợ lý AI hỗ trợ chuẩn hoá dữ liệu mẫu từ bộ `training-ops`, viết script thống kê khảo sát `evidence/survey/analyze_survey.py` và tổng hợp kênh Discord `evidence/analyze_discord.py`, xây dựng khung `codebase/`, nối Gemini REST API (`codebase/ai.py`), chạy & cải tiến Lượt 1 → Lượt 2 (`eval/run-1.csv`, `eval/run-2.csv`), mô phỏng chi phí 50 phiên (`cost/simulate-1.csv`, `cost/cost-estimate.md`) và biên tập tài liệu CP1–CP4 (`spec.md` §8, `eval/report.md`). Toàn bộ dữ liệu khảo sát `n = 27` và `N = 50` câu hỏi trên `#💬-chung` đều thu từ người thật và ẩn danh sạch, mọi mã nguồn `TB-xx`/`SCH-xx`, câu thử, kết quả chấm và chi phí đều do thành viên trực tiếp kiểm chứng (chi tiết tại [docs/ai-usage.md](docs/ai-usage.md)).
