"""Trích xuất lịch học giả lập từ bộ training-ops của BTC sang data/schedules.json.

Chạy mặc định từ thư mục gốc repo (khi thư mục đề BTC nằm cạnh repo nhóm):
    python data/extract_schedules.py
Hoặc chỉ định đường dẫn tới thư mục training-ops:
    python data/extract_schedules.py --input-dir "../day15_repo/data/training-ops"
"""
import argparse
import json
import os
import re
import sys

try:
    import openpyxl
except ImportError:
    sys.exit("Cần cài openpyxl để chạy lại script trích xuất: python -m pip install openpyxl")


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INPUT_DIR = os.path.abspath(os.path.join(ROOT, "..", "day15_repo", "data", "training-ops"))
OUTPUT_PATH = os.path.join(ROOT, "data", "schedules.json")


def _clean_rooms(raw: str) -> list:
    parts = [p.strip() for p in re.split(r"[,;]+", raw) if p.strip()]
    out = []
    for p in parts:
        p = re.sub(r"\(.*?\)", "", p).strip()
        if p and p.lower() != "chờ xác nhận" and p not in out:
            out.append(p)
    return out


def _parse_cell(cell_text: str, col_idx: int) -> dict | None:
    text = (cell_text or "").strip()
    if not text or text in ("không có lớp", "NGHỈ LỄ", "KHAI GIẢNG KHOÁ 9"):
        return None
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    if not lines or "—" not in lines[0]:
        return None

    class_part, session_part = [x.strip() for x in lines[0].split("—", 1)]
    delivery_mode = "offline"
    custom_time = None
    topic_lines = []
    rooms = []
    extra_rooms = []
    lecturers = []
    room_status = "confirmed" if col_idx in (4, 5) else "confirmed"

    # Cột D (col 4) và E (col 5) mặc định dùng phòng H209 / H210 trừ khi ô ghi khác hoặc Online
    default_lec_room = {4: "H209", 5: "H210"}.get(col_idx)

    for ln in lines[1:]:
        low = ln.lower()
        if ln == "Online":
            delivery_mode = "online"
            room_status = "online"
        elif re.match(r"^\d{1,2}:\d{2}\s*[–-]\s*\d{1,2}:\d{2}$", ln):
            custom_time = ln
        elif low.startswith("phòng dự kiến:"):
            val = ln.split(":", 1)[1].strip()
            rooms.extend(_clean_rooms(val))
            room_status = "tentative"
        elif low.startswith("phòng thêm:"):
            val = ln.split(":", 1)[1].strip()
            extra_rooms.extend(_clean_rooms(val))
        elif low.startswith("phòng:"):
            val = ln.split(":", 1)[1].strip()
            if "chờ xác nhận" in val.lower():
                room_status = "pending"
            else:
                rooms.extend(_clean_rooms(val))
                room_status = "confirmed"
        elif low.startswith("giảng viên"):
            val = ln.split(":", 1)[1].strip() if ":" in ln else ln
            # Có dạng "H209: Lecturer E" hoặc "Lecturer A, Lecturer B"
            val = re.sub(r"^[A-Z]\d{3}:\s*", "", val)
            for lec in re.split(r"[,;]+", val):
                lec = lec.strip()
                if lec and lec not in lecturers:
                    lecturers.append(lec)
        else:
            topic_lines.append(ln)

    if delivery_mode == "offline" and not rooms and room_status == "confirmed" and default_lec_room:
        rooms = [default_lec_room]

    return {
        "class_name": class_part,
        "session": session_part,
        "topic": " ".join(topic_lines).strip(),
        "delivery_mode": delivery_mode,
        "custom_time": custom_time,
        "rooms": rooms,
        "extra_rooms": extra_rooms,
        "room_status": room_status,
        "lecturers": lecturers,
    }


def _load_lab_coach_rooms(lab_xlsx_path: str) -> dict:
    """Đọc phòng theo (class_name, session, period_short) từ hai sheet lịch lab để phát hiện lệch phòng."""
    if not os.path.exists(lab_xlsx_path):
        return {}
    wb = openpyxl.load_workbook(lab_xlsx_path, data_only=True)
    result = {}

    # Sheet Lịch lab 2604-0805 có cột Phòng ở col 6 (và cột K-P ở col 11-16)
    if "Lịch lab 2604-0805" in wb.sheetnames:
        ws = wb["Lịch lab 2604-0805"]
        for r in range(6, ws.max_row + 1):
            cls = ws.cell(r, 2).value
            ses = ws.cell(r, 3).value
            room_raw = ws.cell(r, 6).value
            period = ws.cell(r, 7).value
            if cls and ses and room_raw:
                raw_s = str(room_raw).strip()
                status = "tentative" if raw_s.lower().startswith("dk:") else ("pending" if "chờ" in raw_s.lower() else "confirmed")
                cleaned = _clean_rooms(re.sub(r"^dk:\s*", "", raw_s, flags=re.I))
                key = (str(cls).strip(), str(ses).strip(), str(period or "").strip())
                result[key] = {
                    "rooms": cleaned,
                    "status": status,
                    "raw": raw_s,
                    "source": f"lab-coach-schedule.xlsx#Lịch lab 2604-0805:F{r}",
                }
    return result


def extract(input_dir: str) -> dict:
    teaching_path = os.path.join(input_dir, "teaching-schedule.xlsx")
    lab_path = os.path.join(input_dir, "lab-coach-schedule.xlsx")
    if not os.path.exists(teaching_path):
        sys.exit(f"Không tìm thấy {teaching_path}")

    wb = openpyxl.load_workbook(teaching_path, data_only=True)
    ws = wb["Khoá 9 (GĐ1)"]
    snapshot = str(ws["D1"].value or "").strip()
    lab_rooms_map = _load_lab_coach_rooms(lab_path)

    # Nhóm bản ghi theo (date, period, class_name, session) để gộp 2 phòng song song D & E của cùng một buổi LEC
    grouped = {}
    current_date = ""
    col_letter = {4: "D", 5: "E", 6: "F", 7: "G", 8: "H"}

    for r in range(6, ws.max_row + 1):
        d_val = ws.cell(r, 1).value
        if d_val:
            current_date = str(d_val).strip()
        weekday = str(ws.cell(r, 2).value or "").strip()
        period_full = str(ws.cell(r, 3).value or "").strip()
        period_short = "Sáng" if period_full.startswith("Sáng") else ("Chiều" if period_full.startswith("Chiều") else period_full)

        for c in range(4, 9):
            raw = ws.cell(r, c).value
            parsed = _parse_cell(str(raw) if raw is not None else "", c)
            if not parsed:
                continue

            gkey = (current_date, period_short, parsed["class_name"], parsed["session"])
            cell_ref = f"teaching-schedule.xlsx#Khoá 9 (GĐ1):{col_letter[c]}{r}"

            if gkey not in grouped:
                slug_cls = re.sub(r"[^A-Z0-9]+", "", parsed["class_name"].upper())
                slug_ses = re.sub(r"[^A-Z0-9]+", "-", parsed["session"].upper()).strip("-")
                grouped[gkey] = {
                    "schedule_id": f"SCH-{slug_cls}-{slug_ses}",
                    "date": current_date,
                    "weekday": weekday,
                    "period": period_full,
                    "period_short": period_short,
                    "time_range": parsed["custom_time"] or ("09:00–13:00" if period_short == "Sáng" else "14:00–18:00"),
                    "class_name": parsed["class_name"],
                    "session": parsed["session"],
                    "topic": parsed["topic"],
                    "delivery_mode": parsed["delivery_mode"],
                    "rooms": list(parsed["rooms"]),
                    "extra_rooms": list(parsed["extra_rooms"]),
                    "room_status": parsed["room_status"],
                    "lecturers": list(parsed["lecturers"]),
                    "source_refs": [cell_ref],
                    "cross_sheet_note": "",
                }
            else:
                rec = grouped[gkey]
                for rm in parsed["rooms"]:
                    if rm not in rec["rooms"]:
                        rec["rooms"].append(rm)
                for rm in parsed["extra_rooms"]:
                    if rm not in rec["extra_rooms"]:
                        rec["extra_rooms"].append(rm)
                for lec in parsed["lecturers"]:
                    if lec not in rec["lecturers"]:
                        rec["lecturers"].append(lec)
                if parsed["room_status"] in ("pending", "tentative") and rec["room_status"] == "confirmed":
                    rec["room_status"] = parsed["room_status"]
                if cell_ref not in rec["source_refs"]:
                    rec["source_refs"].append(cell_ref)

    records = list(grouped.values())

    # Đối chiếu chéo với bảng lab coach để gắn cờ nếu có phòng lệch / dự kiến
    for rec in records:
        lkey = (rec["class_name"], rec["session"], rec["period_short"])
        if lkey in lab_rooms_map:
            lc = lab_rooms_map[lkey]
            if sorted(lc["rooms"]) != sorted(rec["rooms"]) or lc["status"] != rec["room_status"]:
                rec["cross_sheet_note"] = (
                    f"Bảng lab-coach ghi: {lc['raw']} (trạng thái: {lc['status']}, nguồn: {lc['source']})"
                )

    return {
        "metadata": {
            "source": "BTC training-ops (giả lập Khoá 9, ẩn danh)",
            "teaching_snapshot": snapshot,
            "total_sessions": len(records),
            "note": "Dữ liệu giả lập dùng cho bản chạy thử A2, không phải bằng chứng pain.",
        },
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description="Trích xuất lịch học từ training-ops sang JSON.")
    parser.add_argument("--input-dir", default=DEFAULT_INPUT_DIR, help="Thư mục chứa teaching-schedule.xlsx và lab-coach-schedule.xlsx")
    parser.add_argument("--output", default=OUTPUT_PATH, help="Đường dẫn file JSON đầu ra")
    args = parser.parse_args()

    payload = extract(args.input_dir)
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Đã xuất {payload['metadata']['total_sessions']} buổi học -> {args.output}")


if __name__ == "__main__":
    main()
