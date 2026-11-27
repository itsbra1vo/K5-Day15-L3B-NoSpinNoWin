# Tổng hợp bằng chứng pain

*(Cập nhật CP2 · 27/11/2026 18:45: Đã hoàn thành khảo sát ẩn danh đạt ngưỡng `n = 27 ≥ 20` người ngoài nhóm. Nhóm tiếp tục phỏng vấn `≥3` người ngoài nhóm và/hoặc đếm kênh Discord công khai làm nguồn đối chiếu thứ hai trước CP3.)*

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ Đạt (`n = 27`) | `evidence/survey/questions.md`, `evidence/survey/results.csv`, `evidence/survey/analyze_survey.py` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ *(đang triển khai cho nguồn đối chiếu 2)* | `evidence/interviews/` |
| Đào data kênh Discord công khai | ☐ *(bổ sung nếu kịp trước CP3)* | `evidence/data-mining.md` |

## 2. Số liệu chính từ khảo sát (`n = 27`, chạy lại bằng `python evidence/survey/analyze_survey.py`)

- **Thành phần mẫu:** 18/27 (66.7%) học viên lớp L3B · 8/27 (29.6%) học viên lớp L3A · 1/27 (3.7%) TA / Lab Coach / Key Coach.
- **Tần suất phát sinh pain:**
  - **24/27 (88.9%)** phải tìm lại hoặc hỏi lại lịch học, phòng học, hạn nộp trên Discord ít nhất 1 lần/tháng (`13/27` gặp 1–2 lần · `7/27` gặp 3–5 lần · `4/27` gặp trên 5 lần · chỉ `3/27` trả lời 0 lần).
  - **20/27 (74.1%)** vừa phải tìm lại tin trong tuần này hoặc ngay hôm nay (`10/27` hôm nay · `10/27` trong tuần này).
  - Trung bình có trọng số toàn mẫu: **~2.65 lần/người/tháng** · **~6.02 phút/lần** (`12/27` mất 5–15 phút · `10/27` mất 2–5 phút · `5/27` dưới 2 phút).
- **Cách xoay xở hiện tại (chọn nhiều):**
  - 15/27 (55.6%) dùng thanh tìm kiếm (Search) hoặc xem tin ghim (Pinned)
  - 14/27 (51.9%) phải đối chiếu chéo lại trên LMS / email / Google Calendar
  - 12/27 (44.4%) cuộn lại từng kênh thông báo đọc từ trên xuống
  - 12/27 (44.4%) nhắn hỏi lại trên kênh chat chung · 10/27 (37.0%) nhắn riêng hỏi bạn hoặc TA
- **Sự cố cụ thể gặp trong 1 tháng qua (22/27 — 81.5% gặp ≥1 sự cố):**
  - **13/27 (48.1%)** đọc nhầm thông báo cũ dù đã có thông báo mới gia hạn/đổi phòng
  - **11/27 (40.7%)** thấy hai kênh hoặc hai tin nhắn ghi hạn nộp / phòng học khác nhau
  - **7/27 (25.9%)** nhắn hỏi trên kênh chung nhưng tin bị trôi, không thấy ai trả lời ngay
  - **6/27 (22.2%)** tới sát giờ học mới biết phòng đổi hoặc chuyển sang học Online
- **Hậu quả gần nhất:** **17/27 (63.0%)** mất thời gian lội nhiều kênh/thread kiểm chứng lại · **16/27 (59.3%)** suýt trễ hoặc trễ hạn nộp bài / đi nhầm phòng học · **6/27 (22.2%)** phải nhắn làm phiền TA/bạn trả lời lại chuyện đã thông báo rồi.

## 3. Trích dẫn nguyên văn từ khảo sát (ẩn danh theo số thứ tự phiếu)

1. *"Thông thường, mỗi phòng lab có một thông báo trên lớp mà không có thông báo trên các kênh nên việc đấy có thể khiến học viên rơi vào tình huống hỏi lại thông tin nộp bài thông qua lab coach hoặc TA"* — **Phiếu S06** *(Học viên L3B)*
2. *"thông tin lộn xộn, rời rạc ở nhiều nơi, các thông báo nếu không được ghim thì sẽ bị tin nhắn khác làm trôi"* — **Phiếu S15** *(Học viên L3B)*
3. *"sát giờ học mà chưa biết nội dung, học phòng nào"* — **Phiếu S13** *(Học viên L3B)*
4. *"Quá nhiều kênh thông tin và phải nhận biết được vấn đề mình nằm ở phần kênh thông tin nào để hỏi"* — **Phiếu S26** *(Học viên L3A)*
5. *"search engine không quá mơ hồ, không match nội dung cần tìm"* — **Phiếu S18** *(Học viên L3B)*
6. *"Quá nhiều kênh gây nhiễu trong khi User bình thường chỉ cần tham gia đọc trong một vài kênh nhất định"* — **Phiếu S19** *(Học viên L3B)*
7. *"là khiến tôi đến muộn mà mất thời gian di chuyển"* — **Phiếu S08** *(Học viên L3A)*

## 4. Kết luận sơ bộ & đối chiếu giả thuyết (`evidence/hypothesis.md`)

- **So với giả thuyết ban đầu:** Giả thuyết đặt ngưỡng đúng khi `≥12/20` học viên từng phải tìm lại hoặc mất trên 5 phút trong tháng qua. Kết quả thực tế cho thấy **24/27 (88.9%)** phải tìm lại thông tin trên Discord ít nhất 1 lần/tháng, **12/27 (44.4%)** mất 5–15 phút mỗi lần và tới **22/27 (81.5%)** gặp ít nhất 1 sự cố (48.1% đọc nhầm thông báo cũ, 40.7% gặp hai kênh ghi lệch nhau). **Giả thuyết ban đầu được xác nhận**, đồng thời dữ liệu mới cho thấy pain không chỉ giới hạn ở "học viên đi làm buổi tối" mà trải đều trên **cả học viên L3A lẫn L3B** do có quá nhiều kênh thông báo rải rác.
- **Điều cần làm tiếp cho nguồn đối chiếu thứ hai (trước CP3):** Phỏng vấn sâu `≥3` người ngoài nhóm (2 học viên + 1 TA) và đếm mẫu câu hỏi lặp trên kênh công khai để giải thích rõ vì sao tin nhắn trên lớp/Discord hay bị trôi và TA thường tốn thời gian nhất ở loại câu hỏi nào.

## 5. Lịch phỏng vấn đối chiếu tiếp theo (cập nhật CP2 → CP3)

| Đối tượng | Thời gian dự kiến | Trạng thái |
|---|---|---|
| Phỏng vấn P1 (học viên L3B từng gặp tin lệch phòng/hạn) | 20:00 Thứ Sáu 27/11 | Chưa xong |
| Phỏng vấn P2 (học viên L3A từng đến muộn / lỡ thông báo) | 20:30 Thứ Sáu 27/11 | Chưa xong |
| Phỏng vấn P3 (TA / Lab Coach trực kênh hỏi đáp) | 21:00 Thứ Sáu 27/11 | Chưa xong |
