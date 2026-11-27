# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Thiết lập khung repo & tài liệu CP1 | Coding agent / LLM | Hỗ trợ đưa nội dung `starter-repo/` ra thư mục gốc đúng quy định đề bài, gợi ý câu chữ nháp cho `canvas.md`, `spec.md` §0–§2 | Cả nhóm kiểm định lại lát cắt A2, đối chiếu từng mục với `02-guide.md`, tự sửa lại giả thuyết và bảng impact | Đàm Hồng Thái, Lê Quý Toàn |
| Code bản chạy thử | | | | Lê Quý Toàn |
| Prompt / thiết kế lời gọi mô hình | | | | Lê Quý Toàn |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | Nguyễn Bảo Duy |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | Đàm Hồng Thái |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | Lê Danh Giang |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | Nguyễn Bảo Duy |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | Lê Danh Giang |
| Slide, văn bản | | | | Đàm Hồng Thái |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
