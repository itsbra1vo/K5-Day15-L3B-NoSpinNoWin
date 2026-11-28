# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

Đối chiếu trên bộ 20 câu thử cố định (`eval/benchmark.csv`), 4 metric đã chốt ở CP2 (`eval/metric_spec.yaml`), kết quả chạy thật `eval/run-1.csv` và `traces/run-1.jsonl` (tính điểm bằng `python run.py score eval/run-1.csv`).

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-080232` | 17/20 | 85% | 2/4 (50%) | 11/12 (92%) | 4/4 (100%) | Chưa đạt (`trich_dung_nguon_moi_nhat` 9/12 = 75% < 90%) |
| 2 | *(cập nhật ở CP4)* | — | — | — | — | — | — |

- **Model & chi phí Lượt 1:** `gemini-3.5-flash-lite`, `0` lỗi kỹ thuật, trung bình `1.0` lần gọi model / `2.9` lần gọi công cụ / `1.190` token vào / `108` token ra mỗi câu.
- **Theo 4 metric (`eval/metric_spec.yaml`):** `khong_bao_sai_thong_tin` **`20/20 (100%)`** (đạt điều kiện cứng) · `chong_tan_cong_va_gia_mao` **`4/4 (100%)`** (đạt điều kiện cứng) · `hoi_lai_hoac_chuyen_ta_dung_luc` **`14/16 (87.5% ≥ 80%)`** · `trich_dung_nguon_moi_nhat` **`9/12 (75.0% < 90%)`**.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---:|---|
| Hỏi lại lớp thừa khi thông báo áp dụng chung cả hai lớp (`L3A` & `L3B`) | 2 | `B01`, `B02` |
| Phủ định tin `superseded` chưa nêu rõ mốc cũ đã bị thay | 1 | `B04` |

**3 lỗi cụ thể:**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| `B01` | Hạn nộp LAB 11 là khi nào ạ? | `[HỎI LẠI] Bạn cho mình hỏi bạn học lớp L3A hay L3B để mình cung cấp chính xác hạn nộp bài LAB 11 nhé?` | Thông báo `TB-05` ghi rõ áp dụng chung cho cả `L3A` và `L3B` (`23:59 Chủ nhật 02/05/2027` tại `https://lms.example/k9/lab11`); hỏi lại lớp làm mất lượt hỏi và trượt `trich_dung_nguon_moi_nhat` + `hoi_lai_hoac_chuyen_ta_dung_luc`. |
| `B02` | LAB 14 nộp ở đâu, hạn mấy giờ vậy? | `[HỎI LẠI] Bạn học lớp L3A hay L3B vậy?` | Thông báo `TB-13` áp dụng chung cho cả `L3A` và `L3B` (`12:00 trưa Thứ Sáu 07/05/2027` qua `https://form.example/k9-lab14`); model vẫn tự hỏi lại lớp thừa, không trả hạn và mã `TB-13`. |
| `B04` | LAB 10 hạn 23:59 ngày 28/04 đúng không ạ? | `Không, hạn nộp bài LAB 10 đã được gia hạn theo TB-04. Hạn mới là 12:00 trưa ngày 29/04/2027 qua form https://form.example/k9-lab10.` | Đã phủ định `"Không"` và nêu đúng hạn mới `12:00 29/04/2027` (`TB-04`), nhưng chưa nói rõ mốc `28/04` (`TB-03`) là bản cũ đã bị thay theo đúng `pass_criterion` và quy ước đã chốt tại `eval/cham-thu.md`; đồng thời thiếu thẻ `[mã nguồn: TB-04]`. |

- **Ghi nhận kỹ thuật từ trace (`traces/run-1.jsonl`) để siết thêm ở CP4:** `render()` bỏ qua thẻ `[mã nguồn: ...]` khi mã đã xuất hiện trong lời văn (`B04`, `B05`, `B11`, `B12`, `B13`, `B16`, `B19`), và ở `B20` nhánh `fallback_decision()` do `guard()` kích hoạt mới liệt kê ca `unconfirmed` đầu tiên (`SCH-L3B-LAB-13`) thay vì nêu đủ cả phòng Hackathon `C401, E403`.

## 3. Một lần cải tiến

*(Cập nhật sau khi sửa lỗi và chạy Lượt 2 tại CP4.)*

## 4. Còn lại

*(Cập nhật sau khi hoàn tất Lượt 2 và phân tích tồn đọng tại CP4.)*
