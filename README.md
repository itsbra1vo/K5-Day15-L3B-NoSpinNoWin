# NoSpinNoWin — Trợ lý tra cứu lịch học & hạn nộp Discord (Track A2)

**Thành viên, lớp, track:** xem [TEAMS.md](TEAMS.md).

*Lát cắt dự kiến: Một học viên L3 · nhắn hỏi hạn nộp bài hoặc phòng học sắp tới trên Discord · trợ lý tra cứu thông báo và lịch chính thức rồi trả lời kèm trích dẫn thông báo mới nhất hoặc tạo phiếu chuyển TA duyệt nếu thiếu nguồn/mâu thuẫn · học viên nhận thông tin chính xác mà không bị nhớ nhầm hạn hay đi nhầm phòng.*

---

## Nhóm làm gì, khung làm gì

| Nhóm quyết định và viết | Khung làm sẵn (không cần sửa) |
|---|---|
| Người dùng, pain, bằng chứng, impact (`evidence/`, `spec.md` §1–§2) | — |
| Hình dạng giải pháp, công cụ, prompt, luồng (`spec.md` §4, `codebase/agent.py`, `tools.py`, `ai.py`) | Ghi mọi lần gọi model / công cụ vào trace, cộng token (`codebase/tracing.py`) |
| Bộ câu thử, metric, chuẩn "đạt" (`eval/benchmark.csv`, `eval/metric_spec.yaml`, `spec.md` §7) | Kiểm đủ cột, đủ câu `kho` / `tu_choi`, đủ ≥1/3 câu từ người dùng / data thật (`run.py check`) |
| Chấm cột `pass` theo metric spec | Chạy cả bộ một lệnh, có run ID, model, token từng câu (`run.py eval`) · tính % đạt (`run.py score`) |
| Persona, số người dùng thật, giá model (`cost/personas.yaml`) | Sinh ≥50 phiên, chạy thật qua bản chạy thử, tính chi phí / phiên, / task thành công, / tháng 3 kịch bản (`run.py simulate`) |

## Chạy trong 3 phút

Bộ khung cần **Python 3.10 trở lên** (Python 3.9 vẫn chạy được, chỉ in một dòng nhắc). **Không cần `pip install`** ở bản khung cơ bản.

| Việc | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Kiểm Python | `python --version` (hoặc `py --version`) | `python3 --version` |
| Chạy bản chạy thử (hiện tại là chế độ giả) | `python run.py` | `python3 run.py` |
| Kiểm bộ câu thử & `TEAMS.md` | `python run.py check` | `python3 run.py check` |
| Tạo file `.env` khi nối model | `copy .env.example .env` | `cp .env.example .env` |

## Lệnh

| Lệnh | Làm gì |
|---|---|
| `python run.py` | Chạy bản chạy thử (gõ đầu vào, nhận kết quả, kèm số lần gọi model / token) |
| `python run.py check` | Kiểm `eval/benchmark.csv`, `eval/metric_spec.yaml` và `TEAMS.md` |
| `python run.py eval --try` | Thử nối model với 3 câu đầu → `eval/run-try.csv` |
| `python run.py eval` | Chạy cả bộ qua `codebase/agent.py` → `eval/run-N.csv` + `traces/run-N.jsonl` |
| `python run.py score eval/run-1.csv` | Tính % đạt tổng và theo `type` sau khi điền cột `pass` (1 / 0) |
| `python run.py simulate --try` | Thử mô phỏng chi phí 10 phiên → `cost/simulate-try.csv` |
| `python run.py simulate` | Mô phỏng chi phí khi dùng thật theo `cost/personas.yaml` (≥50 phiên) → `cost/simulate-N.csv` + `cost/simulate-N-summary.md` |

## Bản chạy thử — viết ở đâu

| File | Viết gì | Bước guide |
|---|---|---|
| `codebase/agent.py` | `answer(text)` — luồng chính, đúng hình dạng ở `spec.md` §4 | 3.2 |
| `codebase/tools.py` | Công cụ của bài toán, mỗi công cụ một hàm có `@tool` | 2.2, 3.2 |
| `codebase/ai.py` | `call_model(system, user)` — chỗ duy nhất gọi model | 3.3 |

## Phần nào thật, phần nào giả

| Thành phần | Thật / Giả | Ghi chú |
|---|---|---|
| Lời gọi AI ở quyết định trung tâm | **Chưa nối** (chế độ giả cho khung CP1) | Sẽ dựng khung chạy giả ở CP2 và nối model thật trước CP3 |
| Dữ liệu lịch / thông báo | **Giả lập / mẫu** | Dự kiến dùng bộ `training-ops` giả lập kết hợp thông báo mẫu tự dựng (sẽ khai báo chi tiết ở `data/DATA_CARD.md`) |

## Dùng AI vào việc gì

Ở giai đoạn CP1, nhóm dùng trợ lý AI hỗ trợ rà soát lại cấu trúc repo đúng chuẩn khung nộp bài và chỉnh sửa diễn đạt trong `canvas.md`, `spec.md` §0–§2 cho mạch lạc. Toàn bộ phần chọn bài toán, giả thuyết pain, lát cắt và phân công đều do cả 4 thành viên tự chốt và kiểm tra lại (chi tiết cập nhật liên tục ở [docs/ai-usage.md](docs/ai-usage.md)).

## File mẫu — trạng thái theo từng mốc

| File | Điền ở bước guide | Mốc |
|---|---|---|
| `TEAMS.md` | 1.0 | CP1 · Đã điền đủ 4 thành viên |
| `canvas.md` | 1.4 | CP1 · Đã điền 7 dòng, cập nhật ở CP2 |
| `evidence/hypothesis.md` | 1.1 | CP1 · Đã chốt giả thuyết trước khi khảo sát |
| `evidence/data-mining.md` · `evidence/interviews/` · `evidence/survey/` | 1.2 | Triển khai sau 17:00 → CP3 |
| `evidence/summary.md` | 1.2 | CP3 (đã có lịch hẹn tại CP1) |
| `spec.md` | §0–§2: 1.1–1.3 · §3–§5: 2.1–2.3 · §7: 2.4 · §8: 4.2 · §10: suốt | CP1 đã có §0–§2 & §10; §7 chốt CP2 |
| `data/DATA_CARD.md` | 2.4 | Bản đầu CP2 |
| `eval/benchmark.csv` · `eval/metric_spec.yaml` | 2.4 | ≥10 câu + metric chốt CP2 · 20–30 câu CP3 |
| `codebase/` | 3.2, 3.3 | Khung CP2 · AI thật CP3 |
| `eval/report.md` · `eval/README.md` | 4.1 | CP4 |
| `cost/personas.yaml` · `cost/cost-estimate.md` | 4.2 | Thử 10 phiên CP3 · đủ CP4 |
| `validation/log.md` *(bonus)* | 4.3 | CP4 |
| `slides/outline.md` → `demo-slides.pdf` | 5.1 | CP4 |
| `reflection/<ten-khong-dau>.md` | 5.3 | 23:59 Thứ Bảy 28/11 |

## Bảy hạng mục bắt buộc — nằm ở file nào

| # | Hạng mục | File |
|---|---|---|
| 1 | Bằng chứng pain | `evidence/` (tổng hợp ở `evidence/summary.md`) |
| 2 | Impact có số | `spec.md` §2 |
| 3 | Thiết kế giải pháp | `spec.md` §4 |
| 4 | Bản chạy thử làm trọn lát cắt | `codebase/` |
| 5 | Định nghĩa "tốt" + bộ câu thử | `data/DATA_CARD.md` · `eval/` |
| 6 | Mô phỏng chi phí khi dùng thật | `cost/` |
| 7 | Slide + demo + video dự phòng | `demo-slides.pdf` ở thư mục gốc *(CP4)* |
| + | *Bonus:* người dùng thử | `validation/log.md` |
