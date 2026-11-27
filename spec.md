# AI SPEC — Trợ lý tra cứu lịch học & hạn nộp Discord (Track A2) · Nhóm NoSpinNoWin · Lớp L3B

- **Track:** A (EdTech) — Hướng A2: Trợ lý Discord
- **Dữ liệu chạy thử:** Dùng bộ `data/training-ops/` giả lập ở local kết hợp thông báo/thread mẫu tự dựng (không dùng làm bằng chứng pain).

## §0. Hiện tại việc này diễn ra thế nào
- Luồng hiện tại trong khoá:
  1. Ban đào tạo hoặc TA đăng thông báo lịch học, phòng học, link nộp bài và hạn nộp lên các kênh Discord / LMS của khoá; khi thiếu phòng hoặc đổi ca sát ngày thì nhắn cập nhật thêm trong kênh hoặc thread.
  2. Học viên bận lịch ban ngày khi tối mới mở Discord phải cuộn lại tin nhắn ở kênh thông báo, kênh lớp và các thread hỏi đáp để kiểm tra phiên bản mới nhất.
  3. Nếu không thấy hoặc thấy hai tin lệch nhau, học viên nhắn hỏi lại trên kênh hỏi đáp chung.
  4. TA hoặc Lab coach vào đọc, tra lại thông báo cũ rồi trả lời thủ công từng người *(ảnh minh hoạ giao diện đã che tên sẽ bổ sung ở CP2)*.
- Công cụ / bot đang dùng cho việc này: Chưa kiểm chi tiết bot hiện có trên Discord khoá (sẽ quan sát trước CP2).

## §1. Người dùng & bằng chứng
- **Người dùng chính:** Học viên lớp L3 đang đi làm hoặc vướng lịch học ban ngày, tối mới vào Discord xem thông báo trước buổi học/lab; và TA trực kênh hỏi đáp.
- **Việc cần hoàn thành:** Tra cứu chính xác hạn nộp bài, phòng học và thông báo chính thức mới nhất trên Discord trước mỗi buổi học hoặc hạn nộp.
- **Cách đang xoay xở & chỗ hỏng:** Tự cuộn kênh thông báo, tìm bằng từ khoá trên Discord hoặc nhắn hỏi lại trên kênh chung / hỏi bạn bè. Cách này hỏng khi thông báo nằm rải ở nhiều kênh/thread hoặc bản cập nhật mới không ghi đè rõ lên tin cũ; chưa bỏ được vì Discord vẫn là kênh báo tin nhanh nhất của khoá khi có thay đổi sát giờ.
- **Pain:** Học viên L3 bận lịch ban ngày khi chuẩn bị nộp lab hoặc trước giờ lên lớp thường phải lội qua nhiều kênh và thread trên Discord để tìm hạn nộp hay phòng học mới nhất do thông báo nằm rải rác và hay thay đổi sát giờ, nên dễ xem nhầm thông báo cũ, mất thời gian tìm hoặc hỏi lặp lại khiến TA phải trả lời cùng một câu nhiều lần.
- **Bằng chứng:** Đang ở mốc CP1 — nhóm đã chốt giả thuyết tại `evidence/hypothesis.md` và bắt đầu triển khai khảo sát lớp, phỏng vấn học viên/TA cùng thống kê kênh Discord công khai ngay từ 17:10 hôm nay để đưa số liệu thực vào CP2–CP3 (chi tiết tại `evidence/summary.md`).

## §2. Impact & quyết định chọn

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| 1. Tra cứu hạn nộp, phòng học & thông báo chính thức trên Discord cho học viên (không chắc chuyển TA) | ~350 HV L3B *(tự ước tính theo quy mô ~700 HV L3 chia đôi L3A/L3B)* | ~4 lần/người *(tự ước tính theo nhịp ~2 buổi/tuần, ~1–2 lần tra lại lịch/hạn mỗi tuần)* | ~6 phút tự lội tin + rủi ro trễ hạn/nhầm phòng *(tự ước tính)* | ~8.400 phút/tháng (~140 giờ) *(tự ước tính)* | Có | **Chọn** |
| 2. Gom câu hỏi tồn & tạo bản tin tổng hợp cuối ngày cho TA/Lab coach | ~15–20 TA/coach L3B *(tự ước tính)* | ~12 lượt/tháng *(tự ước tính)* | ~15 phút lội thread lọc câu chưa trả lời *(tự ước tính)* | ~3.600 phút/tháng (~60 giờ) *(tự ước tính)* | Hạn chế | Loại ở nhịp đầu |
| 3. Hỗ trợ gỡ lỗi code lab & gợi ý bài tập trực tiếp trên Discord | ~350 HV L3B *(tự ước tính)* | ~4 lần/người *(tự ước tính)* | ~15 phút chờ trả lời lỗi *(tự ước tính)* | ~21.000 phút/tháng *(tự ước tính)* | Không | Loại |

- **Impact / tháng của hướng chọn:** 350 người × 4 lần/tháng × 6 phút = **8.400 phút/tháng (~140 giờ/tháng)** *(tự ước tính sơ bộ ở CP1 trên quy mô lớp L3B ~350 học viên; tần suất và thời gian mất thực tế sẽ cập nhật từ khảo sát và phỏng vấn ở CP2–CP3)*.
- **Hướng đã loại & lý do:**
  - *Bản tin cuối ngày cho TA:* Chỉ tổng hợp sau buổi, chưa giúp học viên kiểm ngay hạn nộp hay phòng học lúc đang cần gấp; có thể mở rộng sau khi luồng tra cứu chính chạy ổn.
  - *Gỡ lỗi code lab trên Discord:* Đòi hỏi ngữ cảnh bài tập + code riêng từng bạn, dễ trùng với hướng Tutor (A1) và tiềm ẩn rủi ro lộ đáp án lab trong quỹ thời gian 10 tiếng.
- **Tần suất theo kiểu người dùng (dùng cho mô phỏng chi phí ở §8):** *(Cập nhật sau đợt khảo sát/phỏng vấn tại CP2–CP3)*.

## §3. Giải pháp tương tự
*(Cập nhật tại CP2)*

## §4. Thiết kế
*(Cập nhật sơ đồ, kiến trúc, công cụ, mức tự chủ và nguyên tắc thiết kế tại CP2)*

## §5. Chỗ khó
*(Cập nhật các kịch bản khó và tấn công tại CP2)*

## §6. Bốn đường đi của trải nghiệm
*(Cập nhật tại CP2–CP3)*

## §7. Đánh giá & chuẩn "đạt"
*(Sẽ chốt cứng bằng số trước 19:30 Thứ Sáu 27/11 tại CP2)*

## §8. Chi phí khi dùng thật
*(Cập nhật tại CP4)*

## §9. Rủi ro & an toàn
*(Cập nhật tại CP2–CP3)*

## §10. Phân công & nhật ký thay đổi
- **Phân công:**
  - *Phân công chính theo `TEAMS.md`:* Đàm Hồng Thái (Đội trưởng: khảo sát pain và người dùng, điều phối nộp checkpoint) · Lê Quý Toàn (thu thập và chuẩn hóa nguồn thông tin, `DATA_CARD.md` & kho tra cứu) · Lê Danh Giang (thiết kế luồng trợ lý và giới hạn an toàn, `spec.md` §4–§5 & §9) · Nguyễn Bảo Duy (làm mẫu thử `codebase/`, bộ câu thử & đánh giá `eval/`, mô phỏng chi phí `cost/`).
  - *Phối hợp theo chặng:* Cả nhóm cùng chốt Track A2, khảo sát/phỏng vấn người dùng (≥1 người/thành viên), đọc chéo câu trượt sau lượt 1 và chuẩn bị demo/slide CP4.
- **Dùng AI vào việc gì:** Nhóm dùng trợ lý AI hỗ trợ rà lại cấu trúc repo theo quy chuẩn khung nộp bài và chỉnh diễn đạt ở `canvas.md`, `spec.md` §0–§2 cho rõ ý (chi tiết trong `docs/ai-usage.md`).
- **Nhật ký thay đổi (từ sau CP2):** *(Chưa có thay đổi)*
