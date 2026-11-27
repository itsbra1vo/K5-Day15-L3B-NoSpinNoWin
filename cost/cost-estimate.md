# Chi phí khi dùng thật — Nhóm NoSpinNoWin (Track A2)

*(Trạng thái chuẩn bị CP3: Đã chốt toàn bộ đầu vào persona, quy mô người dùng thật và bảng giá trả phí trong `cost/personas.yaml`. Phần kết quả mô phỏng chính thức và so sánh impact sẽ điền ngay sau khi chạy `python run.py simulate --rate-from eval/run-2.csv` với model thật ở CP4.)*

## 1. Đầu vào

- **Persona (`cost/personas.yaml` — rút từ Câu 3 khảo sát `n = 27`, `evidence/survey/results.csv`):**
  - `hoc_vien_hoi_it` (59%): `1.2` phiên/người/tháng · `1` lượt hỏi/phiên *(từ 16/27 người hỏi 0 hoặc 1–2 lần/tháng; số lượt/phiên tự ước tính)*
  - `hoc_vien_hoi_vua` (26%): `4` phiên/người/tháng · `2` lượt hỏi/phiên *(từ 7/27 người hỏi 3–5 lần/tháng; số lượt/phiên tự ước tính)*
  - `hoc_vien_hoi_nhieu_va_ta` (15%): `7` phiên/người/tháng · `3` lượt hỏi/phiên *(từ 4/27 người hỏi >5 lần/tháng; ước tính 7 phiên & 3 lượt/phiên)*
- **Quy mô người dùng thật (3 kịch bản):**
  - **Thấp:** `350` người *(tự ước tính — 1 lớp L3B chia đôi khối L3)*
  - **Cơ sở:** `700` người *(nguồn: tài liệu khoá AI20K K5 — lớp L3 hơn 700 học viên)*
  - **Cao:** `1.000` người *(nguồn: tài liệu khoá AI20K K5 — cả khoá hơn 1.000 học viên L23 & L34)*
- **Bảng giá model trả phí (USD / 1M token, tra từ bảng giá K5 ngày 25/11/2026):**
  - `gpt-4o-mini` (tầng Nhỏ): vào `$0.15` · ra `$0.60` (`https://developers.openai.com/api/docs/pricing`)
  - `gemini-3.1-flash-lite` (tầng Nhỏ): vào `$0.25` · ra `$1.50` (`https://ai.google.dev/gemini-api/docs/pricing`)
  - `gemini-4-hydrogen` (tầng Lớn): vào `$1.50` · ra `$7.50` (`https://ai.google.dev/gemini-api/docs/pricing`)
- **Tỉ lệ đạt dùng để tính:** *(Chờ kết quả `eval/run-2.csv` sau khi nối model thật ở CP3–CP4)*
- **Model đo token:** *(Ghi rõ "đo trên model X, tính giá theo 3 tầng model trên" sau khi chạy `simulate` thật)*

## 2. Kết quả mô phỏng

*(Chờ dán bảng từ `cost/simulate-1-summary.md` sau khi chạy `python run.py simulate --rate-from eval/run-2.csv` ở CP4.)*

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (350) | / tháng — cơ sở (700) | / tháng — cao (1.000) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| `gpt-4o-mini` | | | | | | |
| `gemini-3.1-flash-lite` | | | | | | |
| `gemini-4-hydrogen` | | | | | | |

## 3. So với impact

- **Impact / người / tháng (`spec.md` §2):** `2.65 lần/tháng × 6.02 phút/lần ≈ 15.95 phút/người/tháng` (~186 giờ/tháng cho toàn khối L3 700 học viên), chưa tính rủi ro trễ hạn nộp hoặc đi nhầm phòng (59.3% mẫu khảo sát từng gặp).
- **Chi phí / người / tháng (kịch bản cơ sở):** *(Cập nhật từ mục 2 ở CP4)*
- **Kết luận — có đáng làm không:** *(Cập nhật sau khi có chi phí thực đo ở CP4)*
