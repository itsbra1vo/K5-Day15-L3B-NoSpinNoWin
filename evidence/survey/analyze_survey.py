"""Thống kê kết quả khảo sát từ evidence/survey/results.csv (chỉ dùng thư viện chuẩn).

Chạy từ thư mục gốc repo:
    python evidence/survey/analyze_survey.py
"""
import csv
import os
from collections import Counter

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results.csv")


def main():
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    data = rows[1:]
    n = len(data)
    print(f"Tổng số phiếu hợp lệ (ngoài nhóm): n = {n}\n")

    for idx, title in [
        (1, "Câu 1 — Vai trò"),
        (2, "Câu 2 — Lần gần nhất tìm lại tin"),
        (3, "Câu 3 — Tần suất tìm/hỏi lại trong 1 tháng"),
        (5, "Câu 5 — Thời gian trung bình mỗi lần"),
    ]:
        print(f"### {title}")
        for k, v in Counter(r[idx].strip() for r in data).most_common():
            print(f"  - {k}: {v}/{n} ({v / n * 100:.1f}%)")
        print()

    multi_specs = [
        (4, "Câu 4 — Cách tìm thông tin", [
            "Cuộn lại các kênh thông báo",
            "Dùng thanh tìm kiếm (Search)",
            "Nhắn hỏi lại trên kênh chat chung",
            "Nhắn riêng hỏi bạn cùng lớp hoặc TA",
            "Kiểm tra lại trên LMS",
        ]),
        (6, "Câu 6 — Sự cố đã gặp trong 1 tháng qua", [
            "Đọc nhầm thông báo cũ",
            "Thấy hai kênh hoặc hai tin nhắn ghi hạn nộp / phòng học khác nhau",
            "Nhắn hỏi trên kênh chung nhưng tin bị trôi",
            "Tới sát giờ học mới biết phòng đổi",
            "Chưa từng gặp tình huống nào",
        ]),
        (7, "Câu 7 — Hậu quả gần nhất", [
            "Mất thời gian lội nhiều kênh",
            "Suýt trễ hoặc trễ hạn nộp bài",
            "Phải nhắn làm phiền TA",
            "Không ảnh hưởng đáng kể",
        ]),
    ]
    for idx, title, opts in multi_specs:
        print(f"### {title}")
        for o in opts:
            cnt = sum(1 for r in data if o in r[idx])
            print(f"  - {o}: {cnt}/{n} ({cnt / n * 100:.1f}%)")
        print()

    inc = sum(1 for r in data if "Chưa từng gặp" not in r[6])
    freq_pos = sum(1 for r in data if not r[3].startswith("0 lần"))
    freq_mid = {"0 lần (không phải tìm lại)": 0.0, "1–2 lần / tháng": 1.5, "3–5 lần / tháng": 4.0, "Trên 5 lần / tháng": 6.0}
    min_mid = {"Dưới 2 phút": 1.5, "Từ 2 đến 5 phút": 3.5, "Từ 5 đến 15 phút": 10.0}
    avg_f = sum(freq_mid[r[3].strip()] for r in data) / n
    avg_m = sum(min_mid[r[5].strip()] for r in data) / n
    print(f"Tỉ lệ phải tìm lại ≥1 lần/tháng: {freq_pos}/{n} ({freq_pos / n * 100:.1f}%)")
    print(f"Tỉ lệ gặp ≥1 sự cố (Câu 6): {inc}/{n} ({inc / n * 100:.1f}%)")
    print(f"Trung bình có trọng số: {avg_f:.2f} lần/người/tháng · {avg_m:.2f} phút/lần")


if __name__ == "__main__":
    main()
