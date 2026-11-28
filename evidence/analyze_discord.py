"""Tái lập thống kê đào dữ liệu kênh Discord công khai từ evidence/discord_summary.csv.

Chạy từ thư mục gốc repo (chỉ dùng thư viện chuẩn):
    python evidence/analyze_discord.py
"""
import csv
import os

CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "discord_summary.csv")


def main():
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    cats = [r for r in rows if r["bang"] == "phan_loai"]
    resp = [r for r in rows if r["bang"] == "phan_hoi_logistics"]

    total_n = sum(int(r["so_luong"]) for r in cats)
    logistics_n = sum(int(r["so_luong"]) for r in cats if r["la_logistics"] == "1")
    non_logistics_n = total_n - logistics_n
    resp_total = sum(int(r["so_luong"]) for r in resp)

    assert logistics_n == resp_total, f"Lệch tổng logistics: {logistics_n} != {resp_total}"

    by_resp = {r["nhom"]: int(r["so_luong"]) for r in resp}
    slow_or_none = by_resp["khong_phan_hoi"] + by_resp["sau_15_phut"]
    daytime_slow_or_none = slow_or_none - 2  # loại 2 câu hỏi đêm khuya (~01:06–01:15 sáng)

    print(f"Tổng câu hỏi gốc hợp lệ (N): {total_n}")
    print(f"Câu hỏi logistics (x1): {logistics_n}/{total_n} ({logistics_n / total_n * 100:.1f}%)")
    print(f"Câu hỏi ngoài logistics: {non_logistics_n}/{total_n} ({non_logistics_n / total_n * 100:.1f}%)\n")

    print("### Phân rã 6 nhóm câu hỏi logistics:")
    for r in cats:
        if r["la_logistics"] == "1":
            cnt = int(r["so_luong"])
            print(f"  - {r['nhom']}: {cnt}/{logistics_n} logistics ({cnt / logistics_n * 100:.1f}%) — {r['ghi_chu']}")

    print("\n### Tình trạng phản hồi trong nhóm logistics:")
    print(f"  - Không có phản hồi: {by_resp['khong_phan_hoi']}/{logistics_n} ({by_resp['khong_phan_hoi'] / logistics_n * 100:.1f}%)")
    print(f"  - Trả lời sau >15 phút: {by_resp['sau_15_phut']}/{logistics_n} ({by_resp['sau_15_phut'] / logistics_n * 100:.1f}%)")
    print(f"  - Trả lời trong ≤15 phút: {by_resp['trong_15_phut']}/{logistics_n} ({by_resp['trong_15_phut'] / logistics_n * 100:.1f}%)")
    print(
        f"  => Tổng trôi / không phản hồi / chậm >15 phút (x2): "
        f"{slow_or_none}/{logistics_n} logistics ({slow_or_none / logistics_n * 100:.1f}%) · "
        f"{slow_or_none}/{total_n} toàn mẫu ({slow_or_none / total_n * 100:.1f}%)"
    )
    print(
        f"  => Nếu loại 2 câu đêm khuya (~01:06–01:15): "
        f"{daytime_slow_or_none}/{logistics_n} ({daytime_slow_or_none / logistics_n * 100:.1f}%)"
    )


if __name__ == "__main__":
    main()
