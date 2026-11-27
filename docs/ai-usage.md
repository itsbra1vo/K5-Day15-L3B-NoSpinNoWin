# Khai báo dùng AI — Nhóm NoSpinNoWin

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Thiết lập khung repo & tài liệu CP1 | Coding agent / LLM | Hỗ trợ dọn cấu trúc repo về đúng thư mục gốc và gợi ý diễn đạt nháp cho `canvas.md`, `spec.md` §0–§2 | Cả nhóm chốt bài toán A2, kiểm định giả thuyết, sửa câu chữ cho sát thực tế | Đàm Hồng Thái, Lê Quý Toàn |
| Khảo sát pain và người dùng | | Chỉ rà câu hỏi tránh dẫn dắt | | Đàm Hồng Thái |
| Thu thập & chuẩn hóa nguồn thông tin | Coding agent / LLM | Hỗ trợ viết `data/extract_schedules.py` trích lịch từ `training-ops` và sinh bản nháp 18 thông báo + 8 thread mẫu trong `data/` | Kiểm tay 100% (18/18 thông báo, 8/8 thread) và đối chiếu 108 buổi trích xuất với sheet gốc `Khoá 9 (GĐ1)`, chỉnh các ca `conflict`/`superseded`/`pending` | Lê Quý Toàn |
| Thiết kế luồng trợ lý & giới hạn an toàn | | | | Lê Danh Giang |
| Làm mẫu thử, đánh giá & mô phỏng chi phí | | | Tự chấm/kiểm lại từng câu thử | Nguyễn Bảo Duy |
