# Ước tính chi phí vận hành thực tế (CP4)

- **Lượt mô phỏng chính thức:** `simulate-1@20261128-093336` ([simulate-1.csv](simulate-1.csv), [simulate-1-summary.md](simulate-1-summary.md), [traces/simulate-1.jsonl](../traces/simulate-1.jsonl))
- **Model chạy đo token:** `gemini-3.1-flash-lite` (`THINKING_BUDGET=0`)
- **Tỉ lệ đạt đầu vào:** `19/20 (95%)` lấy từ Lượt 2 `run-2@20261128-090447` ([eval/run-2.csv](../eval/run-2.csv)) trên cùng model `gemini-3.1-flash-lite`
- **Cấu hình mô phỏng:** `50` phiên theo [personas.yaml](personas.yaml) (`seed=42`, tỷ trọng persona `59% / 26% / 15%`, tần suất `1.2 / 4 / 7` lần/tháng, quy mô `350 / 700 / 1.000` người dùng)
- **Tình trạng thực thi:** `49/50` phiên hoàn tất sạch (`77` lượt, trung bình `1.6` lượt/phiên, `112.778` token vào, `8.985` token ra, độ trễ trung bình `3.973s`/phiên); `1/50` phiên lỗi kỹ thuật (`S047`, nhóm `hoc_vien_hoi_vua`, lượt `T2`: `TimeoutError: The read operation timed out`) đã được `simulate.py` loại khỏi trung bình.

> **Lưu ý phương pháp đo:** Đo token trực tiếp trên model `gemini-3.1-flash-lite`, tính giá theo từng model trong bảng bên dưới. Với `gpt-4o-mini` và `gemini-4-hydrogen`, bộ tách token khác nhau nên số token thật có thể lệch.

---

## 1. Mức tiêu thụ theo Persona (`gemini-3.1-flash-lite`)

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| `hoc_vien_hoi_it` | 26 | 1 | 1465 | 112 | 1.0 | 2.9 |
| `hoc_vien_hoi_vua` | 18 | 2 | 2910 | 234 | 2.0 | 5.9 |
| `hoc_vien_hoi_nhieu_va_ta` | 5 | 3 | 4461 | 371 | 3.0 | 8.6 |

- Phiên 1 lượt hỏi ít tốn trung bình `1.465` token vào (`~3` lần gọi công cụ đọc JSON/Markdown), trong khi phiên 3 lượt tăng gần tuyến tính lên `4.461` token vào và `8.6` lần gọi công cụ do giữ ngữ cảnh hội thoại và gọi lại công cụ tra cứu theo từng lượt.

---

## 2. So sánh chi phí giữa 3 model và 3 kịch bản quy mô

| Model (giá $/1M token) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Tháng — thấp (350 người) | Tháng — cơ sở (700 người) | Tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `gpt-4o-mini` (vào 0.15 · ra 0.6) | $0.00046 | $0.00048 | $0.00030 | $0.6089 | $1.22 | $1.74 | $0.0017 |
| `gemini-3.1-flash-lite` (vào 0.25 · ra 1.5) | $0.00085 | $0.00090 | $0.00057 | $1.14 | $2.28 | $3.26 | $0.0033 |
| `gemini-4-hydrogen` (vào 1.5 · ra 7.5) | $0.0048 | $0.0051 | $0.0032 | $6.46 | $12.92 | $18.46 | $0.0185 |

- Công thức quy đổi: `Chi phí / task thành công = chi phí / phiên ÷ 0.95`; `Chi phí / câu hỏi đạt = chi phí / phiên ÷ 1.6 ÷ 0.95` (theo từng câu thử).
- Chọn vận hành chính trên **`gemini-3.1-flash-lite`**: giữ nguyên chất lượng đã kiểm định `19/20 (95%)` ở Lượt 2, tiết kiệm khoảng `5.67x` so với `gemini-4-hydrogen` (`$2.28` so với `$12.92/tháng` ở mức cơ sở), và theo bảng giá K5 còn có Free tier cùng context caching (`$0.025/1M`, chưa bật trong lượt đo).
- **Nguồn bảng giá model (ngày xem: `25/11/2026`, đơn vị `USD/1M` token, gói Standard):**
  - `gpt-4o-mini` (vào `$0.15/1M` · ra `$0.60/1M` · cache `$0.075/1M`): [OpenAI API Pricing](https://developers.openai.com/api/docs/pricing) (ngày xem `25/11/2026`, đối chiếu bảng giá K5).
  - `gemini-3.1-flash-lite` (vào `$0.25/1M` · ra `$1.50/1M` · cache `$0.025/1M` · Free tier: Có): [Google Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing) (ngày xem `25/11/2026`, đối chiếu bảng giá K5).
  - `gemini-4-hydrogen` (vào `$1.50/1M` · ra `$7.50/1M` · cache `$0.075/1M` · Free tier: Có): [Google Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing) (ngày xem `25/11/2026`, đối chiếu bảng giá K5).

---

## 3. Phân tích độ nhạy (Sensitivity Analysis)

1. **Cơ cấu input vs output token (`gemini-3.1-flash-lite`):** Trên 49 phiên hợp lệ, trung bình một phiên dùng `2.301,59` token vào (`$0.0005754`, chiếm **67.7%**) và `183,37` token ra (`$0.0002751`, chiếm **32.3%**), tổng `$0.0008505`/phiên. Phần lớn chi phí đến từ việc đưa nội dung thông báo/lịch học tìm được vào prompt; nếu nạp thêm nhiều tài liệu thô chưa lọc (hoặc bật `THINKING_BUDGET > 0`), chi phí sẽ tăng theo token vào.
2. **Tác động của tỉ lệ đạt (`85%` -> `95%`):** Nếu dùng kết quả Lượt 1 (`17/20 = 85%`), `chi phí / task thành công` là `$0.00085 ÷ 0.85 = $0.00100`. Khi Lượt 2 đạt `19/20 (95%)`, chỉ số này giảm **-10.5%** xuống còn **`$0.00090`/task thành công**.
3. **Độ nhạy theo lưu lượng và độ dài phiên:** Do phiên 3 lượt tốn gấp `~3.05x` token vào so với phiên 1 lượt (`4.461` vs `1.465`), nếu tỷ lệ người dùng hỏi nối tiếp 3 lượt tăng mạnh (ví dụ đầu khóa hoặc trước deadline CP), chi phí tháng cơ sở có thể tiến gần kịch bản cao (`$3.26/tháng`), vẫn ở mức rất thấp.

---

## 4. Chi phí ngoài model (triển khai Discord 24/7)

- **Hạ tầng chạy bot 24/7:** Khoảng **`$5–$7/tháng`** *(tự ước tính)* cho 1 VPS/container nhỏ chạy tiến trình Discord bot nối vào `codebase/agent.py`.
- **Lưu trữ & chỉ mục dữ liệu:** **$0/tháng** vì dữ liệu MVP (`schedules.json`, `announcements.json`, `threads.json`) ở dạng file cục bộ gọn nhẹ, chưa cần vector database hay GPU riêng.
- **Tổng chi phí vận hành thực tế (API + hạ tầng):** Ước tính **`$7.28–$9.28/tháng`** ở kịch bản cơ sở `700` người dùng (tương đương **`~$0.010–$0.013/người/tháng`**).

---

## 5. Kết luận Go / No-Go

- **So với tác động kỳ vọng:** Chi phí API model `gemini-3.1-flash-lite` chỉ **`$0.0033/người/tháng`** (`$2.28/tháng` cho 700 người dùng), và ngay cả khi gộp VPS 24/7 cũng chỉ khoảng **`$0.01/người/tháng`**, đổi lại tiết kiệm trung bình **`15.95 phút/người/tháng`** (`2.65 lần/tháng × 6.02 phút/lần` từ khảo sát `n = 27`, tổng `~11.167 phút/tháng` cho `700` học viên L3 — xem [spec.md §2](../spec.md#2-impact--quyết-định-chọn) và [personas.yaml](personas.yaml)).
- **Quyết định: GO** — Đủ điều kiện triển khai với `gemini-3.1-flash-lite` (`THINKING_BUDGET=0`). Lưu ý kỹ thuật khi đưa ra chạy thật: bổ sung cơ chế retry/fallback khi gặp timeout API như phiên `S047` (`1/50`).
