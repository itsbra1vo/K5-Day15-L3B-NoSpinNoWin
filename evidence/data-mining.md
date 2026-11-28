# Đào dữ liệu kênh Discord công khai — Nhóm NoSpinNoWin (Track A2)

Báo cáo tổng hợp số liệu đếm thực tế trên kênh hỏi đáp công khai của khoá (đã ẩn danh toàn bộ tên tài khoản, ID và link mời), dùng làm **nguồn bằng chứng thật thứ hai** đối chiếu chéo với khảo sát `n = 27`.

---

## 1. Quy tắc chọn mẫu & cách đếm

- **Nguồn dữ liệu:** Kênh hỏi đáp công khai `#💬-chung` trong server Discord của khoá (`[L34] AI20K Build Phase - Cohort 5`).
- **Khoảng thời gian quan sát:** **14/11/2026 – 27/11/2026** (14 ngày), rà liên tục ngược từ tin nhắn lúc `27/11/2026 23:57` tới `14/11/2026 21:14`, không bỏ sót khoảng giữa.
- **Mẫu số (`N = 50`):** `50` câu hỏi gốc liên tiếp của học viên trên kênh. Loại trừ tin nhắn chào hỏi/chat xã giao, biểu tượng reaction, tin nhắn trả lời, `+1`/hùa theo, tin tự đẩy bài (bump), bài kêu gọi điền form khảo sát/tìm đồng đội hackathon và tin hỏi đồ thất lạc/mượn sạc.
- **Định nghĩa 2 chỉ số đếm:**
  - `x1` (**Câu hỏi logistics**): Câu hỏi về thời khóa biểu/lịch học/trùng buổi, link Zoom/học Online/breakout/bản ghi, hạn nộp/quy chế nộp checkpoint, link nộp bài/link repo/đăng ký team, phòng học/đổi phòng, chia nhóm/danh sách lớp.
  - `x2` (**Bị trôi / không phản hồi / trả lời sau >15 phút**): Tập con của `x1` gồm các câu không nhận được bất kỳ câu trả lời nào trên kênh hoặc có phản hồi đầu tiên trễ hơn 15 phút.
- **Script tái lập số liệu:** Lưu bảng tổng hợp ẩn danh tại `evidence/discord_summary.csv`, chạy lại bằng `python evidence/analyze_discord.py`.

---

## 2. Kết quả đếm (`python evidence/analyze_discord.py`)

### Tổng hợp chính

| Chỉ số đếm | x / N | % | Ghi chú |
|---|---:|---:|---|
| Câu hỏi thuộc nhóm logistics (`x1 / N`) | **35 / 50** | **70.0%** | 15 câu còn lại là chính sách điểm danh/trợ cấp (8) và thẻ SV/Git/slide/khác (7) |
| Câu logistics không phản hồi hoặc chờ >15 phút (`x2 / x1`) | **20 / 35** | **57.1%** | Tương đương **20 / 50 (40.0%)** toàn bộ câu hỏi trên kênh *(12 không phản hồi · 8 chờ 23p–6h37p; bỏ 2 câu lúc ~01:06–01:15 sáng vẫn là **18/35 = 51.4%**)* |
| Trong đó không có phản hồi trên kênh | **12 / 35** | **34.3%** | Có nhiều câu lặp lại qua nhiều ngày (TKB tuần sau hỏi lại 14/11 & 22/11; link bản ghi 15/11 hỏi 3 lần) |

### Phân rã 6 nhóm trong 35 câu hỏi logistics

| Nhóm nội dung | Số câu | Tỉ lệ / 35 câu logistics | Chi tiết quan sát được |
|---|---:|---:|---|
| Lịch học, TKB & trùng buổi | 10 | 28.6% | Hỏi TKB tuần sau (lặp ngày 14/11 và 22/11), trùng lịch buổi học |
| Link học Online, Zoom, breakout & bản ghi | 10 | 28.6% | Hỏi link học Online buổi sáng, phòng breakout, xin lại bản ghi buổi định hướng |
| Hạn nộp & quy định nộp checkpoint | 6 | 17.1% | Hỏi nộp muộn/nộp lại CP1–CP2, Gate 2/3 |
| Link nộp bài, link repo & đăng ký team | 4 | 11.4% | Phân vân nộp link LMS hay submission, link đăng ký team bị trôi giữa tin tuyển thành viên |
| Phòng học & đổi phòng | 3 | 8.6% | Đổi phòng sát buổi do vướng lịch khám sức khỏe (có 3 bạn khác nhắn `+1` chờ 23 phút) |
| Chia nhóm & phân lớp | 2 | 5.7% | Đổi nhóm rồi vẫn bị mời nhầm vào nhóm cũ trên Mentor Duty |

---

## 3. Ví dụ nguyên văn đã ẩn danh (8 ví dụ, ≤2 câu mỗi ví dụ)

1. `[27/11/2026 — Hạn nộp · tự bump, trả lời sau 23 phút]` *"Các anh chị lab coach cho em hỏi là CP1 và CP2 nhóm em phát hiện ra sai sót trong câu trả lời rồi thì giờ còn kịp để có thể nộp lại 2 checkpoint đó không ạ?"*
2. `[27/11/2026 — Hạn nộp · không có phản hồi]` *"cho em hỏi phần CP2 nếu nộp trễ hơn một xíu thì có mất điểm nhiều k ạ"*
3. `[27/11/2026 — Link đăng ký · bị trôi, không có phản hồi]` *"đăng ký team đã có link chưa ạ"*
4. `[22/11/2026 — Lịch học · không phản hồi, lặp lại câu ngày 14/11]` *"cac anh oi, co TKB cho tuan sau chua a?"*
5. `[21/11/2026 — Đổi phòng · 3 bạn +1, trả lời sau 23 phút]` *"Cho e hỏi là phòng C303 đang khám sức khỏe thì lab 3b sáng nay hc ở đâu ạ"*
6. `[19/11/2026 — Link nộp · không có phản hồi]` *"cho tôi hỏi phát là link repo theo lms hay submission đây =))"*
7. `[19/11/2026 — Link Online · bạn cùng lớp trả lời sau 2 phút]` *"sáng nay lấy link học onl ở đâu thế mng"*
8. `[18/11/2026 — Chia nhóm · bạn khác đồng tình, chưa có staff trả lời]` *"Sao đổi nhóm rồi mà lại mời vào nhóm cũ nhỉ mọi người, có ai giống mình không ạ? Mentor Duty ấy."*

---

## 4. Giới hạn & đối chiếu với khảo sát (`n = 27`)

- **Giới hạn của dữ liệu đào trên kênh:** Quan sát một kênh chung `#💬-chung` trong 14 ngày chỉ thấy phần nổi là các câu học viên chủ động nhắn công khai (không đo được các câu hỏi nằm ở kênh riêng từng lớp, tin nhắn hỏi trực tiếp TA/bạn bè hoặc người tự cuộn/tìm lại trong im lặng).
- **Khớp & bổ trợ với khảo sát `n = 27`:**
  - *Điểm khớp:* Cả hai nguồn đều xác nhận nhu cầu hỏi đáp xoay quanh đúng các nhóm việc logistics cốt lõi (lịch học, link Zoom/Online, hạn/link nộp, phòng học, chia nhóm), và tình trạng tin bị trôi hoặc phải chờ đợi là rất rõ ràng (**20/35 = 57.1%** câu logistics trên kênh chung không có phản hồi hoặc chậm >15 phút; bên khảo sát có **25.9%** tự nhận từng bị trôi tin chưa ai trả lời ngay và **44.4%** mất 5–15 phút tìm/chờ).
  - *Điểm bổ trợ giải thích:* Trong khảo sát có tới **55.6%** chọn dùng Search/Pinned và **48.1%** từng đọc nhầm tin cũ, **40.7%** gặp hai kênh ghi lệch — đào kênh Discord giải thích luôn nguyên nhân thực tế: tin quan trọng nằm xen giữa dòng chat chung, câu hỏi bị lặp lại nhiều ngày (`14/11` → `22/11`), cùng câu hỏi link repo LMS hay link submission (`19/11`) và đổi phòng C303 sáng `21/11`.
