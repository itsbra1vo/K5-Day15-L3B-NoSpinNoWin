# Tổng hợp bằng chứng pain

Nhóm đã hoàn thành đủ **2 nguồn bằng chứng thật độc lập đạt ngưỡng** để đối chiếu chéo: **(1) Khảo sát ẩn danh (`n = 27`)** và **(2) Đào dữ liệu kênh Discord công khai `#💬-chung` (`N = 50`)**.

---

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ Đạt (`n = 27`) | `evidence/survey/questions.md`, `evidence/survey/results.csv`, `evidence/survey/analyze_survey.py` |
| Đào data kênh Discord công khai `#💬-chung` (14/11–27/11/2026) | ☑ Đạt (`N = 50`) | `evidence/data-mining.md`, `evidence/discord_summary.csv`, `evidence/analyze_discord.py` |
| Phỏng vấn bổ trợ (`P1–P3`) | ☐ *(phiếu mẫu sẵn sàng nếu làm thêm trước CP4)* | `evidence/interviews/` |

---

## 2. Số liệu chính

### Nguồn 1 · Khảo sát ẩn danh (`n = 27`, tái lập bằng `python evidence/survey/analyze_survey.py`)
- **Thành phần mẫu:** 18/27 (66.7%) học viên lớp L3B · 8/27 (29.6%) học viên lớp L3A · 1/27 (3.7%) TA / Lab Coach / Key Coach.
- **Tần suất & thời gian mất:** **24/27 (88.9%)** phải tìm lại/hỏi lại tin ≥1 lần/tháng (`13/27` 1–2 lần · `7/27` 3–5 lần · `4/27` >5 lần · `3/27` 0 lần); **20/27 (74.1%)** vừa phải tìm trong tuần này hoặc hôm nay. Trung bình có trọng số: **2.65 lần/người/tháng** · **6.02 phút/lần** (`12/27` mất 5–15 phút).
- **Cách xoay xở:** 15/27 (55.6%) Search/Pinned · 14/27 (51.9%) đối chiếu LMS/Calendar · 12/27 (44.4%) cuộn kênh · 12/27 (44.4%) hỏi kênh chung · 10/27 (37.0%) nhắn riêng bạn/TA.
- **Sự cố & hậu quả (`22/27 = 81.5%` gặp ≥1 sự cố):** 13/27 (48.1%) đọc nhầm thông báo cũ · 11/27 (40.7%) thấy hai kênh/tin ghi lệch nhau · 7/27 (25.9%) hỏi kênh chung bị trôi tin · 6/27 (22.2%) sát giờ mới biết đổi phòng/Online. Hệ quả: 17/27 (63.0%) tốn công lội nhiều kênh, **16/27 (59.3%) suýt trễ/trễ hạn nộp hoặc đi nhầm phòng**, 6/27 (22.2%) phải hỏi lại TA.

### Nguồn 2 · Đào kênh Discord `#💬-chung` (`N = 50` câu hỏi gốc, `14/11–27/11/2026`, tái lập bằng `python evidence/analyze_discord.py`)
- **35/50 (70.0%)** câu hỏi gốc trên kênh hỏi trực tiếp về **logistics khoá học**: lịch học/TKB (`10`), link Online/Zoom/bản ghi (`10`), hạn nộp/checkpoint (`6`), link nộp/link repo/đăng ký team (`4`), phòng học/đổi phòng (`3`), chia nhóm (`2`).
- **20/35 (57.1%)** câu hỏi logistics (tương đương **40.0%** toàn mẫu `50` câu) **không có phản hồi (`12/35`) hoặc phải chờ >15 phút mới có người trả lời (`8/35`, lâu nhất tới 6h37p)**; ngay cả khi loại 2 câu hỏi đêm khuya (~01:06–01:15 sáng), tỉ lệ chậm/mất phản hồi vẫn là **18/35 (51.4%)**.

---

## 3. Trích dẫn nguyên văn đã ẩn danh (`12` trích dẫn từ 2 nguồn thật)

**Từ khảo sát (`results.csv`):**
1. *"Thông thường, mỗi phòng lab có một thông báo trên lớp mà không có thông báo trên các kênh nên việc đấy có thể khiến học viên rơi vào tình huống hỏi lại thông tin nộp bài thông qua lab coach hoặc TA"* — **Phiếu S06** *(Học viên L3B)*
2. *"thông tin lộn xộn, rời rạc ở nhiều nơi, các thông báo nếu không được ghim thì sẽ bị tin nhắn khác làm trôi"* — **Phiếu S15** *(Học viên L3B)*
3. *"sát giờ học mà chưa biết nội dung, học phòng nào"* — **Phiếu S13** *(Học viên L3B)*
4. *"Quá nhiều kênh thông tin và phải nhận biết được vấn đề mình nằm ở phần kênh thông tin nào để hỏi"* — **Phiếu S26** *(Học viên L3A)*
5. *"search engine không quá mơ hồ, không match nội dung cần tìm"* — **Phiếu S18** *(Học viên L3B)*
6. *"Quá nhiều kênh gây nhiễu trong khi User bình thường chỉ cần tham gia đọc trong một vài kênh nhất định"* — **Phiếu S19** *(Học viên L3B)*
7. *"là khiến tôi đến muộn mà mất thời gian di chuyển"* — **Phiếu S08** *(Học viên L3A)*

**Từ kênh Discord công khai `#💬-chung` (`evidence/data-mining.md`):**
8. *"Cho e hỏi là phòng C303 đang khám sức khỏe thì lab 3b sáng nay hc ở đâu ạ"* *(21/11/2026 — 3 bạn khác nhắn `+1`, chờ 23 phút)*
9. *"cho tôi hỏi phát là link repo theo lms hay submission đây =))"* *(19/11/2026 — không có phản hồi)*
10. *"cac anh oi, co TKB cho tuan sau chua a?"* *(22/11/2026 — lặp lại câu ngày 14/11, không phản hồi)*
11. *"đăng ký team đã có link chưa ạ"* *(27/11/2026 — bị trôi giữa tin tuyển nhóm, không phản hồi)*
12. *"Các anh chị lab coach cho em hỏi là CP1 và CP2 nhóm em phát hiện ra sai sót trong câu trả lời rồi thì giờ còn kịp để có thể nộp lại 2 checkpoint đó không ạ?"* *(27/11/2026 — phải tự bump, chờ 23 phút)*

---

## 4. Đối chiếu hai nguồn (Khớp & lệch ở đâu?)

- **Hai nguồn khớp chặt với nhau:**
  1. Khảo sát ghi nhận **88.9%** phải tìm/hỏi lại thông tin lịch–phòng–hạn nộp; trên kênh thật `#💬-chung`, nhóm câu hỏi này chiếm tới **70.0% (`35/50`)** toàn bộ câu hỏi gốc.
  2. Khảo sát cho thấy **25.9%** từng bị trôi tin chưa ai trả lời và **44.4%** mất 5–15 phút dò tìm; dữ liệu đếm thực tế trên Discord chứng minh tỷ lệ trôi/chậm phản hồi thực trên kênh còn cao hơn (**20/35 = 57.1%** không có phản hồi hoặc chậm >15 phút), kèm các tình huống y hệt lo ngại trong khảo sát như hỏi đổi phòng C303 sát giờ (`21/11`), phân vân giữa 2 nguồn nộp LMS vs submission (`19/11`), hay hỏi lặp lại TKB qua nhiều tuần (`14/11` → `22/11`).
- **Góc nhìn bổ trợ giữa hai nguồn:** Khảo sát phát hiện thêm nhóm sự cố mà log chat công khai không lộ hết: **55.6%** phải tự dùng Search và **48.1%** từng đọc nhầm thông báo cũ; còn kênh Discord giải thích trực quan vì sao câu hỏi bị trôi (tin logistics xen lẫn nhiều thảo luận, link mới không ghim đè tin cũ).

---

## 5. Kết luận

- **Kiểm chứng giả thuyết (`evidence/hypothesis.md`):** Giả thuyết **đúng** và được khẳng định bằng cả hai nguồn độc lập (`n = 27` khảo sát + `N = 50` tin nhắn thật trên `#💬-chung`).
- **Điều chỉnh phạm vi từ dữ liệu thật:** Đã mở rộng đúng sang cả hai lớp L3A/L3B (theo khảo sát) và giữ chặt lát cắt trợ lý tra cứu thông báo/lịch kèm kiểm tra mâu thuẫn (`LMS vs submission`), thông báo cũ/mới và tình trạng phòng chưa chốt (`C303`).
