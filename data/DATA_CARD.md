# Data card — Dữ liệu bản chạy thử Track A2 (NoSpinNoWin)

Các tập dữ liệu trong thư mục `data/` chỉ dùng làm nguồn tra cứu cho bản chạy thử (`codebase/tools.py`) và đối chiếu bộ câu thử (`eval/benchmark.csv`), **không dùng làm bằng chứng pain**.

---

## Dataset 1 · Lịch học & phòng học (`data/schedules.json`)

| Mục | Mô tả |
|---|---|
| **Mục đích** | Nguồn tra cứu lịch học, giờ học, hình thức (offline/online), phòng học chính/thêm, giảng viên và trạng thái xác nhận phòng cho công cụ `get_schedule()`. |
| **Nguồn gốc** | Rút trích từ bộ `data/training-ops/` giả lập do BTC cấp (`teaching-schedule.xlsx` snapshot `27/04/2027 21:00` và `lab-coach-schedule.xlsx`). |
| **Các bước xử lý** | Chạy script `data/extract_schedules.py`: (1) bỏ dòng tiêu đề/trống/nghỉ lễ; (2) tách lớp (`L3A`, `L3B`, `L3AB`, `L2A`, `L2B`, `L2AB`), mã buổi (`LEC/LAB/HACKATHON`), giờ riêng, danh sách phòng chính/phòng thêm, giảng viên; (3) gộp hai phòng song song D & E cùng một buổi LEC thành một bản ghi chuẩn; (4) chuẩn hoá 4 trạng thái phòng (`confirmed`, `tentative`, `pending`, `online`); (5) đối chiếu chéo cột phòng của `lab-coach-schedule.xlsx` để gắn cảnh báo `cross_sheet_note` khi hai bảng lệch trạng thái/phòng. |
| **Số lượng bản ghi** | **108 buổi học** (trong đó: 80 `confirmed`, 11 `tentative` dự kiến chờ xác nhận, 9 `pending` chờ xác nhận, 8 `online`; có 19 buổi ghi nhận lệch trạng thái/phòng giữa hai bảng tính). |
| **Phiên bản / ngày tạo** | Rút trích ngày 27/11/2026 từ bản snapshot giả lập `27/04/2027 21:00` của BTC. |
| **Nhãn dữ liệu** | `giả lập BTC (extracted)` — không chứa tên thật, email thật hay số điện thoại thật (`Lecturer A–N`, `Lab Coach A–Z`). |
| **Giới hạn** | Chỉ phản ánh lịch học tại thời điểm xuất file (`27/04/2027 21:00`), không chứa nội dung text về hạn nộp bài hay link nộp bài trên Discord. |

---

## Dataset 2 · Kho thông báo Discord mẫu (`data/announcements.json`)

| Mục | Mô tả |
|---|---|
| **Mục đích** | Nguồn tra cứu hạn nộp lab, link nộp, quy định điểm danh/xin nghỉ và thông báo cập nhật/đính chính cho công cụ `search_announcements()`. |
| **Nguồn gốc** | Nhóm tự dựng (`synthetic`) dựa trên các mốc buổi học trong `schedules.json` và danh sách tình huống khó của Track A2. |
| **Quy cách & xử lý** | Xây dựng cố định 18 thông báo (`TB-01` .. `TB-18`) bằng tên miền giả `.example` và vai trò chung (`Ban đào tạo`, `TA`), không chứa tên thật. Có gán rõ 3 trạng thái: `active` (13 tin), `superseded` (3 tin cũ `TB-03`, `TB-06`, `TB-09` bị thay thế bởi tin mới `TB-04`, `TB-07`, `TB-10`), `conflict` (2 tin `TB-11` và `TB-12` cố tình ghi lệch giờ nộp `LAB 13`: `23:59` vs `18:00`). Kiểm tra thủ công 18/18 bản ghi khớp lịch Khoá 9. |
| **Số lượng bản ghi** | **18 thông báo** (`TB-01` đến `TB-18`). |
| **Phiên bản / ngày tạo** | Phiên bản v1 — tạo ngày 27/11/2026. |
| **Nhãn dữ liệu** | `synthetic` |
| **Giới hạn** | Bộ mẫu nhỏ gọn phục vụ kiểm thử các quyết định chính của lát cắt (trích đúng bản mới nhất, phát hiện tin cũ bị đè, cảnh báo mâu thuẫn, từ chối ngoài phạm vi), chưa phủ hết hội thoại tự nhiên ngoài luồng trên Discord thật. |

---

## Dataset 3 · Thread hỏi đáp Discord mẫu (`data/threads.json`)

| Mục | Mô tả |
|---|---|
| **Mục đích** | Nguồn tra cứu các câu hỏi đã được TA trả lời ở thread khác hoặc đang chờ TA xử lý cho công cụ `search_threads()`. |
| **Nguồn gốc** | Nhóm tự dựng (`synthetic`) gắn nối với mã thông báo `TB-01` .. `TB-15`. |
| **Số lượng bản ghi** | **8 thread** (`TH-01` đến `TH-08`, gồm 7 thread `resolved` đã có câu trả lời của TA và 1 thread `pending_ta` đang chờ chốt tin mâu thuẫn `LAB 13`). Kiểm tra thủ công 8/8 bản ghi. |
| **Phiên bản / ngày tạo** | Phiên bản v1 — tạo ngày 27/11/2026. |
| **Nhãn dữ liệu** | `synthetic` |
| **Giới hạn** | Chỉ dùng cho kịch bản đối chiếu thread đã trả lời, không chứa lịch sử người dùng thật. |
