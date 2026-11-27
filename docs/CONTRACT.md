# Hợp đồng giao tiếp chung — Nhóm NoSpinNoWin (Track A2)

Tài liệu này là **"xương sống" chung để cả 4 thành viên làm việc song song trên nhánh riêng** mà không làm lệch tên hàm, định dạng dữ liệu hay giẫm lên file của nhau lúc ghép lại vào `main`.

---

## 1. Quy tắc Git & phân quyền file (tránh xung đột hoàn toàn)

1. **Không push trực tiếp lên `main` khi đang làm dở.** Mỗi thành viên dùng nhánh riêng theo đúng mã học viên của mình (luôn `git pull origin main` vào nhánh trước mỗi chặng mới):
   - Đàm Hồng Thái: `2A202603927_DamHongThai`
   - Lê Quý Toàn: `2A202603941_LeQuyToan` *(chuyển từ `feat/toan-data` / `feat/toan-cp2` sang chuẩn tên chung)*
   - Lê Danh Giang: `2A202603912_LeDanhGiang`
   - Nguyễn Bảo Duy: `2A202603890_NguyenBaoDuy`
2. **Ai giữ file nào chỉ sửa đúng file đó** trước khi gộp nhánh:
   - **Thái:** `canvas.md`, `evidence/interviews/*`, `evidence/survey/*`, `evidence/summary.md`, quay video 30s CP3, sau này là `validation/log.md` & slide CP4.
   - **Toàn:** `data/*`, `data/DATA_CARD.md`, `evidence/data-mining.md`, `cost/personas.yaml`, chạy `simulate --try` / `simulate` & `cost/cost-estimate.md`.
   - **Giang:** `spec.md` (§3–§7, §9–§10), tinh chỉnh `SYSTEM` prompt / `guard()` trong `codebase/agent.py`, mở rộng `eval/benchmark.csv`, chạy `eval` & cập nhật `eval/README.md` / `eval/report.md`.
   - **Duy:** `codebase/ai.py` (nối model thật, đo token, sửa lỗi API), `codebase/tools.py` & `codebase/agent.py` (lỗi kỹ thuật/cải tiến code Run 2), đồng chấm `eval/run-1.csv` & `eval/run-2.csv`.
3. Khi xong chặng (trước giờ chốt CP2 / CP3 / CP4), mở Pull Request từ nhánh riêng về `main` để đội trưởng merge, rồi các máy khác chạy `git pull origin main` về nhánh của mình trước khi làm tiếp.

---

## 2. Cấu trúc dữ liệu chuẩn trong `data/` (Toàn bàn giao → Duy & Giang dùng)

### `data/schedules.json` (108 buổi từ `training-ops`)
Mỗi phần tử trong `data["records"]` là một object gồm các trường:
- `schedule_id` (`str`, vd `"SCH-L3B-LAB-10"`)
- `date` (`str`, `"DD/MM/YYYY"`), `weekday` (`str`), `period_short` (`"Sáng"` | `"Chiều"`), `time_range` (`str`, vd `"14:00–18:00"` hoặc `"16:30–20:00"`)
- `class_name` (`"L3A"` | `"L3B"` | `"L3AB"` | `"L2A"` | `"L2B"` | `"L2AB"`)
- `session` (`str`, vd `"LEC 13"`, `"LAB 10"`, `"HACKATHON"`)
- `topic` (`str`), `delivery_mode` (`"offline"` | `"online"`)
- `rooms` (`list[str]`), `extra_rooms` (`list[str]`)
- `room_status` (`"confirmed"` | `"tentative"` | `"pending"` | `"online"`):
  - Nếu là `"tentative"` hoặc `"pending"` → **không được báo là phòng đã chốt**, phải ghi rõ là phòng dự kiến / chờ xác nhận.
- `cross_sheet_note` (`str`): Nếu khác rỗng nghĩa là hai bảng `teaching-schedule` và `lab-coach-schedule` đang ghi lệch phòng/trạng thái → **cần cảnh báo hoặc chuyển TA**.
- `source_refs` (`list[str]`): Mã ô nguồn trong bảng tính.

### `data/announcements.json` (18 thông báo mẫu `TB-01`..`TB-18`)
Mỗi phần tử trong `data["records"]`:
- `ann_id` (`"TB-01"`..`"TB-18"`), `channel`, `posted_at`, `author_role`, `class_scope` (`list[str]`), `topic_tags` (`list[str]`), `title`, `content`, `link`
- `status`: `"active"` | `"superseded"` | `"conflict"`
- `supersedes` / `superseded_by` (`str | null`): Nếu thông báo là `"superseded"`, trợ lý **không dùng** thông tin cũ mà phải lấy bản ở `superseded_by`.
- `conflict_with` (`str | null`): Nếu là `"conflict"`, có hai thông báo đang mâu thuẫn (`TB-11` vs `TB-12`) → **cấm tự chọn 1 bên**, phải nêu cả hai nguồn và gọi `escalate_to_ta()`.

### `data/threads.json` (8 thread mẫu `TH-01`..`TH-08`)
Mỗi phần tử trong `data["records"]`:
- `thread_id` (`"TH-01"`..`"TH-08"`), `channel`, `created_at`, `topic_tags`, `question`, `answer_summary`, `related_announcements` (`list[str]`), `status` (`"resolved"` | `"pending_ta"`), `link`.

---

## 3. Hợp đồng Tool & Agent (Giang viết `spec.md` §4 · Duy code `codebase/`)

Các hàm trong `codebase/tools.py` gắn `@tool` giữ đúng tên và kiểu trả về sau:

1. **`search_announcements(query: str, class_name: str = "") -> list[dict]`**
   - *Tác động ra ngoài:* Không (chỉ đọc `data/announcements.json`).
   - *Trả về:* Danh sách bản ghi khớp (`ann_id`, `title`, `content`, `posted_at`, `status`, `superseded_by`, `conflict_with`, `link`). Trả `[]` nếu không có nguồn khớp.
2. **`get_schedule(query: str, class_name: str = "") -> list[dict]`**
   - *Tác động ra ngoài:* Không (chỉ đọc `data/schedules.json`).
   - *Trả về:* Danh sách buổi học khớp lớp/buổi/ngày kèm `room_status`, `rooms`, `cross_sheet_note`, `source_refs`.
3. **`search_threads(query: str) -> list[dict]`**
   - *Tác động ra ngoài:* Không (chỉ đọc `data/threads.json`).
   - *Trả về:* Danh sách thread liên quan để dẫn lại câu đã được TA giải đáp (nếu có).
4. **`escalate_to_ta(question: str, reason: str, related_ids: list[str] | None = None) -> dict`**
   - *Tác động ra ngoài:* Có tiềm ẩn (nhắn/gắn thẻ TA) — **KHÔNG tự gửi ra kênh công khai**, chỉ trả về phiếu chuyển nháp `{"status": "draft_pending_approval", "ticket_id": ..., "reason": ..., "related_ids": ...}` chờ TA/người phụ trách duyệt.

### Hợp đồng đầu ra `answer(text: str) -> dict` trong `codebase/agent.py`
- Bắt buộc trả `{"output": str}` để tương thích `python run.py`, `run.py eval`, `run.py simulate`.
- Quy ước hành vi chung (khớp HAX **G10** & luật an toàn A2):
  1. **Có nguồn `active` khớp rõ & không mâu thuẫn:** Trả lời ngắn gọn kèm `[mã nguồn: TB-xx / SCH-xx]` và link.
  2. **Có tin `superseded`:** Nói theo bản mới nhất (`superseded_by`), có thể chú thích ngắn là bản cũ đã được cập nhật.
  3. **Mâu thuẫn (`conflict` hoặc `cross_sheet_note`) hoặc `room_status` là `pending`/`tentative`:** Nêu rõ thông tin chưa chốt / đang lệch giữa các nguồn, **không đoán chắc**, kèm phiếu chuyển TA nháp (`escalate_to_ta`).
  4. **Không có trong dữ liệu / câu hỏi mơ hồ thiếu lớp hoặc tên bài:** Hỏi lại tối đa 1 ý còn thiếu hoặc nói rõ chưa có thông báo chính thức + chuyển TA.
  5. **Ngoài thẩm quyền (điểm cá nhân, điểm danh, làm hộ lab) hoặc Prompt Injection:** Từ chối lịch sự, hướng dẫn kênh đúng (`TB-17` / LMS / liên hệ trực tiếp TA) và không làm theo chỉ dẫn chèn trong input.
