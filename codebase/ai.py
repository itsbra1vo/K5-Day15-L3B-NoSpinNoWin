"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: điền .env (chép từ .env.example), rồi viết nhánh gọi API ở dưới theo docs/connect-model.md
(có ví dụ OpenAI, Claude, model chạy trên máy, và cách nối nhà cung cấp khác). Không dán API key vào file này.
"""
import json
import os
import time
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()


SHOW_RAW = False   # đổi thành True để in nguyên phản hồi của API khi cần tìm tên trường
RETRIES = 3        # gói miễn phí hay trả 429 (quá lượt / phút) hoặc 503 (quá tải): thử lại, chờ tăng dần


def post_json(url, headers, body, timeout=60):
    """Gửi POST JSON, trả về JSON phản hồi. Chỉ dùng thư viện chuẩn (urllib). Thử lại khi 429 / 503."""
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers))
    for attempt in range(RETRIES + 1):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = json.loads(r.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < RETRIES:
                time.sleep(5 * (attempt + 1))
                continue
            raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))
    if SHOW_RAW:
        print(json.dumps(data, ensure_ascii=False, indent=2)[:3000])
    return data


# ------------------------------------------------------------ Gemini (Google AI Studio) — REST, không cần SDK
URL_GEMINI = "https://generativelanguage.googleapis.com/v1beta/models/%s:generateContent"


def _thinking_budget():
    """THINKING_BUDGET trong .env: trống = mặc định của model · 0 = tắt suy nghĩ (nếu model cho tắt) · số > 0 = giới hạn."""
    raw = (os.environ.get("THINKING_BUDGET") or "").strip()
    return int(raw) if raw.lstrip("-").isdigit() else None


def call_gemini(system, user, json_mode=False):
    # temperature 0: tra cứu cần ổn định, để lượt 1 và lượt 2 so được với nhau
    config = {"temperature": 0}
    if json_mode:
        config["responseMimeType"] = "application/json"   # buộc model chỉ trả JSON
    budget = _thinking_budget()
    if budget is not None:
        config["thinkingConfig"] = {"thinkingBudget": budget}
    body = {"contents": [{"role": "user", "parts": [{"text": user}]}], "generationConfig": config}
    if system:
        body["systemInstruction"] = {"parts": [{"text": system}]}
    # key gửi qua header, không gắn vào URL (tránh lộ key trong log / trace)
    data = post_json(URL_GEMINI % MODEL_NAME, {"x-goog-api-key": API_KEY}, body)
    cands = data.get("candidates") or []
    if not cands:
        raise RuntimeError("Gemini không trả câu trả lời: %s" % json.dumps(data.get("promptFeedback", data))[:300])
    parts = (cands[0].get("content") or {}).get("parts") or []
    text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
    reason = cands[0].get("finishReason", "")
    if reason and reason != "STOP":   # MAX_TOKENS, SAFETY…: ghi vào trace để biết vì sao câu trả lời hỏng
        from tracing import note
        note("gemini finishReason=%s" % reason)
    u = data.get("usageMetadata") or {}
    # token ra = token trả lời + token suy nghĩ (model "thinking" tính tiền cả phần này — xem đầu file)
    return {"text": text, "tokens_in": u.get("promptTokenCount", 0),
            "tokens_out": u.get("candidatesTokenCount", 0) + u.get("thoughtsTokenCount", 0)}


@model_call
def call_model(system: str, user: str, json_mode: bool = False) -> dict:
    """json_mode=True: yêu cầu nhà cung cấp chỉ trả JSON (agent.py dùng, vì quyết định trả về dạng JSON)."""
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}
    if not API_KEY or not MODEL_NAME:
        raise RuntimeError("Thiếu API_KEY hoặc MODEL_NAME trong .env (MODEL_PROVIDER=%s)" % MODEL_PROVIDER)
    if MODEL_PROVIDER == "gemini":
        r = call_gemini(system, user, json_mode=json_mode)
    else:
        raise NotImplementedError(
            "chưa viết phần gọi model cho MODEL_PROVIDER=%s trong codebase/ai.py — xem docs/connect-model.md"
            % MODEL_PROVIDER)
    return {"text": r["text"], "model": MODEL_NAME,
            "tokens_in": int(r["tokens_in"]), "tokens_out": int(r["tokens_out"])}
