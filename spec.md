# AI SPEC — Trợ lý tra cứu lịch học & hạn nộp Discord (Track A2) · Nhóm NoSpinNoWin · Lớp L3B

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Trạng thái CP1 (17:00 Thứ Sáu 27/11): Đã hoàn thiện §0, §1, §2 và phân công §10; các mục §3–§9 sẽ điền chi tiết theo đúng tiến độ CP2–CP4.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: **A2 · Trợ lý Discord**
Data BTC cấp đã dùng (nếu có — không commit nguyên file): `data/training-ops/` (bộ lịch giảng dạy & lab coach giả lập, chỉ dùng ở local làm nguồn chạy thử cho trợ lý, không dùng làm bằng chứng pain).

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này trong khoá:
  1. Ban đào tạo hoặc TA đăng thông báo lịch học, phòng học, link nộp bài và hạn nộp lên các kênh Discord / LMS của khoá; khi thiếu phòng hoặc đổi ca sát ngày thì nhắn cập nhật thêm trong kênh hoặc thread.
  2. Học viên bận lịch ban ngày khi tối mới mở Discord phải cuộn lại tin nhắn ở kênh thông báo, kênh lớp và các thread hỏi đáp để kiểm tra phiên bản mới nhất.
  3. Nếu không thấy hoặc thấy hai tin lệch nhau, học viên nhắn hỏi lại trên kênh hỏi đáp chung.
  4. TA hoặc Lab coach vào đọc, tra lại thông báo cũ rồi trả lời thủ công từng người *(ảnh chụp giao diện minh hoạ từ tài khoản cá nhân đã che tên sẽ bổ sung ở CP2)*.
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn: Chưa kiểm chi tiết bot đang bật trên Discord của khoá (sẽ quan sát các kênh công khai trước CP2).

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): Học viên lớp L3 đang đi làm hoặc vướng lịch học ban ngày, tối mới vào Discord xem thông báo trước buổi học/lab; và TA trực kênh hỏi đáp.
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): Tra cứu chính xác hạn nộp bài, phòng học và thông báo chính thức mới nhất trên Discord trước mỗi buổi học hoặc hạn nộp.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: Tự cuộn kênh thông báo, dùng ô tìm kiếm của Discord hoặc nhắn hỏi lại trên kênh chung / hỏi bạn bè. Cách này hỏng khi thông báo nằm rải ở nhiều kênh/thread hoặc bản cập nhật mới không ghi đè rõ lên tin cũ; chưa bỏ được vì Discord vẫn là kênh báo tin nhanh nhất của khoá khi có thay đổi sát giờ.
- Pain (KHÔNG chữ AI): Học viên L3 bận lịch ban ngày khi chuẩn bị nộp lab hoặc trước giờ lên lớp thường phải lội qua nhiều kênh và thread trên Discord để tìm hạn nộp hay phòng học mới nhất do thông báo nằm rải rác và hay thay đổi sát giờ, nên dễ xem nhầm thông báo cũ, mất thời gian tìm hoặc hỏi lặp lại khiến TA phải trả lời cùng một câu nhiều lần.
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): Đang ở mốc CP1 — nhóm mới chốt giả thuyết ở `evidence/hypothesis.md` và bắt đầu triển khai khảo sát lớp, phỏng vấn học viên/TA cùng thống kê kênh Discord công khai ngay từ 17:00 hôm nay để đưa số liệu thực vào CP2–CP3.

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| 1. Tra cứu hạn nộp, phòng học & thông báo chính thức trên Discord cho học viên (không chắc chuyển TA) | ~350 HV L3B *(tự ước tính theo quy mô ~700 HV L3 chia đôi L3A/L3B)* | ~4 lần/người *(tự ước tính theo nhịp ~2 buổi/tuần, ~1–2 lần tra lại lịch/hạn mỗi tuần)* | ~6 phút tự lội tin + rủi ro trễ hạn/nhầm phòng *(tự ước tính)* | ~8.400 phút/tháng (~140 giờ công tra cứu lặp) *(tự ước tính)* | Có (10h, đủ dữ liệu mẫu `training-ops` + thông báo mẫu) | **Chọn** |
| 2. Gom câu hỏi tồn & tạo bản tin tổng hợp cuối ngày cho TA/Lab coach | ~15–20 TA/coach L3B *(tự ước tính)* | ~12 lượt/tháng (3 buổi/tuần) *(tự ước tính)* | ~15 phút lội thread lọc câu chưa ai trả lời *(tự ước tính)* | ~3.600 phút/tháng (~60 giờ) *(tự ước tính)* | Hạn chế (chưa xử lý trực tiếp ngay lúc học viên hỏi) | Loại ở nhịp đầu |
| 3. Hỗ trợ gỡ lỗi code lab & gợi ý bài tập trực tiếp trên Discord | ~350 HV L3B *(tự ước tính)* | ~4 lần/người *(tự ước tính)* | ~15 phút chờ trả lời lỗi *(tự ước tính)* | ~21.000 phút/tháng *(tự ước tính)* | Không kịp & sai phạm vi (trùng A1/A6, dễ lộ đáp án lab) | Loại |

*(Lưu ý: Mọi con số tần suất và thời gian ở bảng trên tại CP1 đều đang gắn nhãn `*(tự ước tính)*` trên cơ sở quy mô lớp L3 được nêu trong tài liệu khoá; toàn bộ sẽ được cập nhật bằng số đo thật từ khảo sát và phỏng vấn tại CP2–CP3.)*

- **Impact / tháng** của hướng chọn = 350 người × 4 lần/tháng × 6 phút = 8.400 phút/tháng (~140 giờ/tháng) *(tự ước tính sơ bộ ở CP1 — nguồn thừa số: quy mô lớp L3 hơn 700 học viên từ tài liệu khoá chia đôi L3B ~350; tần suất và phút mất sẽ cập nhật từ khảo sát/phỏng vấn tại CP2–CP3)*.
- Hướng ĐÃ LOẠI + vì sao (giữ lại, đừng xoá):
  - **Hướng 2 (Bản tin cuối ngày cho TA):** Giải quyết bài toán tổng hợp sau buổi, chưa giúp học viên kiểm ngay được hạn nộp hay phòng học lúc đang vội; có thể mở rộng thêm ở giai đoạn sau khi luồng tra cứu chuẩn đã ổn định.
  - **Hướng 3 (Gỡ lỗi code lab trên Discord):** Đòi hỏi ngữ cảnh đề bài + code riêng từng người, dễ trùng hướng A1 (Tutor) và có rủi ro AI đưa nguyên lời giải làm mất mục tiêu tự làm lab trong vòng 10 tiếng hackathon.
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8): *(Sẽ điền sau khi có dữ liệu khảo sát & phỏng vấn ở CP2–CP3)*.

## §3. Giải pháp tương tự *(guide 2.1)*
*(Điền ở CP2)*

## §4. Thiết kế *(guide 2.2, 3.2)*
*(Điền đủ sơ đồ, kiến trúc, công cụ, mức tự chủ và nguyên tắc HAX trước CP2)*

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*
*(Điền trước CP2)*

## §6. Bốn đường đi của trải nghiệm
*(Điền trước CP2/CP3)*

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` · metric: `eval/metric_spec.yaml`
- **Chuẩn "đạt"** (sẽ chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): *(Chốt ở CP2)*
- Kết quả: *(Cập nhật ở CP3/CP4)*

## §8. Chi phí khi dùng thật *(guide 4.2)*
*(Điền ở CP4)*

## §9. Rủi ro & an toàn
*(Điền trước CP2/CP3)*

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"):
  - **Chặng 1–2 (Khám phá & Canvas → CP1):** Cả nhóm chốt Track A2, viết giả thuyết (`evidence/hypothesis.md`), hoàn thiện `canvas.md` và `spec.md` §0–§2.
  - **Chặng 3 (Thiết kế & Khung → CP2):** Cặp 1 (Lê Quý Toàn · Đàm Hồng Thái) dựng sơ đồ `spec.md` §4 & khung `codebase/` chạy giả; Cặp 2 (Lê Danh Giang · Nguyễn Bảo Duy) dựng `eval/metric_spec.yaml`, 10 câu thử đầu, `data/DATA_CARD.md` và tổng hợp đợt khảo sát/phỏng vấn đầu. Đổi chéo review trước 19:30.
  - **Chặng 4–6 (CP3 → CP4):** Chia cặp nối model thật, mở rộng 20–30 câu thử, chạy `eval` lượt 1 → cải tiến → lượt 2, chạy `simulate` và làm slide/demo.
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`): Nhóm dùng trợ lý AI để rà kiểm cấu trúc file nộp theo yêu cầu đề bài và chỉnh câu chữ diễn đạt ở `canvas.md`, `spec.md` cho gọn rõ; toàn bộ ý tưởng lát cắt, giả thuyết và phần phân công do nhóm tự thảo luận và chỉnh lại.
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4**

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
| *(Chưa tới CP2)* | | |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)**

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
| *(Chưa tới CP4)* | | |
