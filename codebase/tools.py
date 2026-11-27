"""Công cụ của bài toán A2 — Trợ lý tra cứu hạn nộp, lịch & phòng học trên Discord.

Đúng tên hàm và kiểu trả về theo docs/CONTRACT.md §3. Dữ liệu: data/*.json (Toàn bàn giao, mô tả ở data/DATA_CARD.md).
Ba công cụ đầu chỉ đọc. escalate_to_ta KHÔNG gửi gì ra ngoài: chỉ trả phiếu nháp chờ TA duyệt.
"""
import hashlib
import json
import os
import re
import unicodedata

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")

_cache = {}


def _load(name):
    """Đọc data/<name>.json một lần, trả danh sách records."""
    if name not in _cache:
        with open(os.path.join(DATA, name + ".json"), encoding="utf-8") as f:
            _cache[name] = json.load(f)["records"]
    return _cache[name]


# ------------------------------------------------------------ tách thông tin từ câu hỏi (code, không phải AI)

def norm(text):
    """Chữ thường, bỏ dấu tiếng Việt, gộp khoảng trắng — để so khớp từ khoá."""
    text = unicodedata.normalize("NFD", (text or "").lower()).replace("đ", "d")
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", text).strip()


def find_sessions(text):
    """'LAB 11', 'lab11', 'Lec 13', 'hackathon' → {'lab 11', 'lec 13', 'hackathon'}."""
    t = norm(text)
    found = {"%s %d" % (k, int(n)) for k, n in re.findall(r"\b(lab|lec)\s*(\d{1,2})\b", t)}
    if "hackathon" in t:
        found.add("hackathon")
    return found


def find_dates(text):
    """'04/05', '4/5/2027' → {'04/05'} (ngày/tháng, bỏ năm)."""
    return {"%02d/%02d" % (int(d), int(m)) for d, m in re.findall(r"\b(\d{1,2})/(\d{1,2})(?:/\d{2,4})?\b", text or "")}


def find_class(text):
    """'L3B', 'l3 b' → 'L3B'; không nêu lớp → ''."""
    m = re.search(r"\bl\s*([23])\s*([ab])\b", norm(text))
    return ("L%s%s" % (m.group(1), m.group(2).upper())) if m else ""


def find_period(text):
    t = norm(text)
    return "Sáng" if "sang" in t.split() else ("Chiều" if "chieu" in t.split() else "")


def _class_ok(scope, class_name):
    """scope: list lớp (thông báo) hoặc tên lớp như 'L3AB' (lịch)."""
    if not class_name:
        return True
    if isinstance(scope, list):
        return class_name in scope
    return scope == class_name or (scope.endswith("AB") and class_name.startswith(scope[:2]))


# Từ chung xuất hiện ở hầu hết thông báo — không dùng làm bằng chứng "khớp" (tránh kéo nhầm thông báo bài khác).
GENERIC = {"han", "nop", "bai", "lab", "lec", "hoc", "phong", "ngay", "lop", "nao", "khi", "cua", "cho", "the",
           "gio", "may", "deadline", "l3a", "l3b", "buoi", "chieu", "sang", "toi", "nay", "dau", "khong", "duoc",
           "vay", "nhe", "em", "minh", "ban", "bot", "giup", "voi", "thong", "bao", "moi", "nguoi"}


def _words(text):
    return {w for w in re.findall(r"[a-z0-9]+", norm(text)) if len(w) > 2}


def _keywords(text):
    return _words(text) - GENERIC


# ------------------------------------------------------------ công cụ

ANN_FIELDS = ("ann_id", "title", "content", "posted_at", "status", "superseded_by", "conflict_with", "link")


@tool
def search_announcements(query: str, class_name: str = "") -> list:
    """Tìm thông báo chính thức khớp câu hỏi.
    Input: query (str), class_name ("L3A" | "L3B" | "" = không lọc lớp).
    Output: list[dict] với ann_id, title, content, posted_at, status, superseded_by, conflict_with, link;
            [] nếu không có nguồn khớp. Kèm luôn bản thay thế / bản mâu thuẫn của thông báo khớp.
    Tác động ra ngoài: không (chỉ đọc data/announcements.json)."""
    records = _load("announcements")
    by_id = {r["ann_id"]: r for r in records}
    sessions, dates, words = find_sessions(query), find_dates(query), _words(query)
    keys = _keywords(query)

    def score(r):
        hay = norm(" ".join(r["topic_tags"]) + " " + r["title"] + " " + r["content"])
        if sessions:  # có nêu mã buổi → bắt buộc khớp đúng mã (lab 1 ≠ lab 10)
            if not any(re.search(r"\b%s\b" % re.escape(s), hay) for s in sessions):
                return 0
            return 10 + len(words & _words(hay))
        # không có mã buổi: cần trùng ngày, hoặc ≥2 từ khoá riêng (không tính từ chung) với tag / tiêu đề
        date_hit = sum(1 for d in dates if d in r["content"])
        key_hit = len(keys & _words(" ".join(r["topic_tags"]) + " " + r["title"]))
        return 3 * date_hit + key_hit if (date_hit or key_hit >= 2) else 0

    hits = sorted((r for r in records if _class_ok(r["class_scope"], class_name) and score(r) > 0),
                  key=score, reverse=True)[:4]
    ids = [r["ann_id"] for r in hits]
    for r in list(hits):  # kéo theo bản liên quan để agent thấy đủ bức tranh
        for rel in (r.get("superseded_by"), r.get("supersedes"), r.get("conflict_with")):
            if rel and rel not in ids and rel in by_id:
                ids.append(rel)
    return [{k: by_id[i].get(k) for k in ANN_FIELDS} for i in ids]


SCH_FIELDS = ("schedule_id", "date", "weekday", "period_short", "time_range", "class_name", "session", "topic",
              "delivery_mode", "rooms", "extra_rooms", "room_status", "cross_sheet_note", "source_refs")


@tool
def get_schedule(query: str, class_name: str = "") -> list:
    """Tra lịch học / phòng học theo lớp, mã buổi, ngày, buổi sáng/chiều nêu trong câu hỏi.
    Input: query (str), class_name ("L3A" | "L3B" | "" = mọi lớp L3).
    Output: list[dict] buổi học khớp, kèm room_status, rooms, cross_sheet_note, source_refs; [] nếu không khớp.
    Tác động ra ngoài: không (chỉ đọc data/schedules.json)."""
    sessions, dates, period = find_sessions(query), find_dates(query), find_period(query)
    if not sessions and not dates:
        return []  # không đủ manh mối để tra lịch — tránh trả cả 108 buổi
    out = []
    for r in _load("schedules"):
        if not r["class_name"].startswith("L3") or not _class_ok(r["class_name"], class_name):
            continue
        if sessions and norm(r["session"]) not in sessions:
            continue
        if dates and r["date"][:5] not in dates:
            continue
        if period and r["period_short"] != period:
            continue
        out.append({k: r.get(k) for k in SCH_FIELDS})
    return out[:6]


@tool
def search_threads(query: str) -> list:
    """Tìm thread hỏi đáp đã có trên Discord để dẫn lại câu TA đã trả lời.
    Input: query (str). Output: list[dict] thread (thread_id, question, answer_summary,
    related_announcements, status, link); [] nếu không có. Tác động ra ngoài: không (chỉ đọc data/threads.json)."""
    sessions, words = find_sessions(query), _words(query)
    hits = []
    for r in _load("threads"):
        hay = norm(r["question"] + " " + " ".join(r["topic_tags"]))
        if sessions and not any(re.search(r"\b%s\b" % re.escape(s), hay) for s in sessions):
            continue
        overlap = len(words & _words(hay))
        if overlap >= 3:
            hits.append((overlap, r))
    hits.sort(key=lambda x: x[0], reverse=True)
    keys = ("thread_id", "question", "answer_summary", "related_announcements", "status", "link")
    return [{k: r.get(k) for k in keys} for _, r in hits[:2]]


@tool
def escalate_to_ta(question: str, reason: str, related_ids: list = None) -> dict:
    """Tạo phiếu chuyển TA.
    Input: question (str), reason (str), related_ids (list mã TB-/SCH-/TH- liên quan).
    Output: {"status": "draft_pending_approval", "ticket_id", "reason", "related_ids"}.
    Tác động ra ngoài: CÓ TIỀM ẨN (nhắn / gắn thẻ TA) — vì vậy KHÔNG tự gửi, chỉ trả phiếu nháp chờ TA duyệt."""
    ticket = "ESC-" + hashlib.sha1((question + "|" + reason).encode("utf-8")).hexdigest()[:6].upper()
    return {"status": "draft_pending_approval", "ticket_id": ticket, "reason": reason,
            "related_ids": list(related_ids or [])}
