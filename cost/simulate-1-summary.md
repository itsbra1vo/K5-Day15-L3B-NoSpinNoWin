# Tóm tắt mô phỏng simulate-1@20261128-093336

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| hoc_vien_hoi_it | 26 | 1 | 1465 | 112 | 1.0 | 2.9 |
| hoc_vien_hoi_vua | 18 | 2 | 2910 | 234 | 2.0 | 5.9 |
| hoc_vien_hoi_nhieu_va_ta | 5 | 3 | 4461 | 371 | 3.0 | 8.6 |

Tỉ lệ đạt dùng để tính: 19/20 (95%) — lượt run-2@20261128-090447

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (350 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.00046 | $0.00048 | $0.00030 | $0.6089 | $1.22 | $1.74 | $0.0017 |
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00085 | $0.00090 | $0.00057 | $1.14 | $2.28 | $3.26 | $0.0033 |
| gemini-4-hydrogen (vào 1.5 · ra 7.5 $/1M) | $0.0048 | $0.0051 | $0.0032 | $6.46 | $12.92 | $18.46 | $0.0185 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.6) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.1-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 1/50.
