"""Build the eight-slide NoSpinNoWin demo deck as a PDF.

Run from the repository root with:
    python slides/build_slides.py

The generator uses Pillow only for slide typography and PDF export. App/runtime
code remains on the Python standard library.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "demo-slides.pdf"
W, H = 1920, 1080
BG = (10, 18, 33)
CARD = (18, 31, 51)
CARD2 = (23, 39, 61)
WHITE = (241, 246, 252)
MUTED = (159, 176, 196)
TEAL = (62, 220, 195)
LIME = (191, 240, 119)
AMBER = (255, 190, 92)
CORAL = (255, 117, 112)
LINE = (46, 65, 88)

FONT_DIR = Path("C:/Windows/Fonts")
REG = FONT_DIR / "arial.ttf"
BOLD = FONT_DIR / "arialbd.ttf"
ITALIC = FONT_DIR / "ariali.ttf"


def font(size, bold=False, italic=False):
    path = BOLD if bold else ITALIC if italic else REG
    return ImageFont.truetype(str(path), size)


def rounded(draw, box, fill=CARD, radius=24, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def label(draw, xy, text, color=TEAL, size=22):
    draw.text(xy, text.upper(), font=font(size, True), fill=color)


def wrap_lines(draw, text, f, max_width):
    lines = []
    for para in text.split("\n"):
        if not para:
            lines.append("")
            continue
        words, line = para.split(), ""
        for word in words:
            trial = word if not line else line + " " + word
            if draw.textlength(trial, font=f) <= max_width:
                line = trial
            else:
                if line:
                    lines.append(line)
                line = word
        if line:
            lines.append(line)
    return lines


def paragraph(draw, xy, text, size=28, color=WHITE, max_width=700, leading=1.28,
              bold=False, italic=False):
    x, y = xy
    f = font(size, bold, italic)
    step = int(size * leading)
    for line in wrap_lines(draw, text, f, max_width):
        draw.text((x, y), line, font=f, fill=color)
        y += step
    return y


def pill(draw, x, y, text, color=TEAL, bg=(23, 58, 68), size=19):
    f = font(size, True)
    tw = draw.textlength(text, font=f)
    box = (x, y, x + tw + 34, y + 42)
    rounded(draw, box, bg, 18)
    draw.text((x + 17, y + 8), text, font=f, fill=color)
    return box[2]


def metric(draw, x, y, value, caption, color=TEAL, size=80, width=650):
    draw.text((x, y), value, font=font(size, True), fill=color)
    paragraph(draw, (x, y + size + 9), caption, 24, MUTED, width, 1.18)


def base(page, section, title, source):
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    # restrained corner motif and page furniture
    d.ellipse((W - 265, -250, W + 180, 195), fill=(17, 39, 56))
    d.ellipse((W - 170, -156, W + 86, 100), outline=(28, 77, 86), width=3)
    d.ellipse((62, 49, 82, 69), fill=TEAL)
    d.text((99, 45), "NOSPINNOWIN  /  AI20K · K5", font=font(20, True), fill=WHITE)
    d.text((W - 338, 47), f"{section}     {page:02d} / 08", font=font(19, True), fill=MUTED)
    d.line((64, 1019, W - 64, 1019), fill=LINE, width=2)
    d.text((66, 1035), source, font=font(17), fill=MUTED)
    d.text((W - 300, 1034), "NO SPIN. CHỈ CÓ NGUỒN.", font=font(16, True), fill=(104, 133, 155))
    paragraph(d, (66, 130), title, 54, WHITE, 1530, 1.12, True)
    return im, d


def slide1():
    im, d = base(1, "PAIN", "Thông báo rải rác khiến học viên phải tự kiểm chứng", "Nguồn: evidence/summary.md · khảo sát n=27 · Discord công khai N=50")
    rounded(d, (66, 300, 923, 715), CARD, 28)
    pill(d, 100, 330, "KHẢO SÁT ẨN DANH · n=27")
    metric(d, 100, 405, "88,9%", "phải tìm lại hoặc hỏi lại lịch, phòng hay hạn nộp ít nhất mỗi tháng", TEAL, 91, 740)
    d.line((100, 585, 870, 585), fill=LINE, width=2)
    metric(d, 100, 615, "59,3%", "từng suýt trễ hạn / trễ hạn hoặc đi nhầm phòng", AMBER, 66, 740)

    rounded(d, (965, 300, 1854, 715), CARD, 28)
    pill(d, 1000, 330, "QUAN SÁT KÊNH THẬT · N=50", LIME, (42, 55, 42))
    metric(d, 1000, 405, "70%", "câu hỏi gốc trong #💬-chung hỏi về logistics khoá học", LIME, 91, 760)
    d.line((1000, 585, 1800, 585), fill=LINE, width=2)
    metric(d, 1000, 615, "57,1%", "câu logistics không được trả lời hoặc chờ hơn 15 phút", CORAL, 66, 760)

    rounded(d, (66, 760, 1854, 963), (17, 43, 54), 24, outline=(34, 93, 99), width=2)
    label(d, (102, 785), "TIẾNG NÓI NGƯỜI HỌC", TEAL, 18)
    paragraph(d, (102, 823), "“thông tin lộn xộn, rời rạc ở nhiều nơi, các thông báo nếu không được ghim thì sẽ bị tin nhắn khác làm trôi”", 31, WHITE, 1550, 1.25, italic=True)
    d.text((102, 920), "— Phiếu S15 · học viên L3B", font=font(19, True), fill=MUTED)
    return im


def slide2():
    im, d = base(2, "DECISION", "Chọn bài toán có impact lớn và làm kịp trong một lát cắt", "Nguồn: spec.md §2 · phép tính chính dùng dữ liệu khảo sát và quy mô khoá")
    rounded(d, (66, 290, 1120, 950), CARD, 28)
    pill(d, 105, 325, "HƯỚNG ĐƯỢC CHỌN")
    paragraph(d, (105, 394), "Tra cứu hạn nộp, phòng học và thông báo chính thức trên Discord", 37, WHITE, 900, 1.18, True)
    metric(d, 105, 540, "≈186 giờ", "thời gian tìm kiếm có thể tiết kiệm mỗi tháng trên khối L3 (~700 học viên)", TEAL, 89, 900)
    paragraph(d, (105, 745), "700 × 2,65 lần/tháng × 6,02 phút/lần ≈ 11.167 phút/tháng", 27, WHITE, 900, 1.3, True)
    paragraph(d, (105, 827), "Ngoài thời gian, 59,3% mẫu khảo sát từng suýt trễ hạn hoặc đi nhầm phòng.", 24, MUTED, 900)

    rounded(d, (1155, 290, 1854, 950), CARD2, 28)
    label(d, (1195, 330), "CÁC HƯỚNG ĐÃ CÂN NHẮC", AMBER)
    paragraph(d, (1195, 390), "01  Bản tin cuối ngày cho TA", 28, WHITE, 590, bold=True)
    paragraph(d, (1232, 434), "Loại ở nhịp đầu: không giúp học viên xác minh ngay lúc cần gấp.", 22, MUTED, 560)
    d.line((1195, 520, 1812, 520), fill=LINE, width=2)
    paragraph(d, (1195, 555), "02  Gỡ lỗi code lab", 28, WHITE, 590, bold=True)
    paragraph(d, (1232, 600), "Loại: đòi hỏi ngữ cảnh bài tập và code, vượt lát cắt hiện tại.", 22, MUTED, 560)
    d.line((1195, 690, 1812, 690), fill=LINE, width=2)
    pill(d, 1195, 730, "CHỌN TRA CỨU", TEAL)
    paragraph(d, (1195, 795), "Tập trung giảm lội tin, đọc nhầm bản cũ và hỏi lặp lại.", 26, WHITE, 590, 1.25)
    paragraph(d, (1195, 875), "Các ước tính cho hướng bị loại được đánh dấu riêng trong spec.", 18, MUTED, 590)
    return im


def slide3():
    im, d = base(3, "SOLUTION", "Trả lời khi căn cứ rõ; chuyển TA khi dữ liệu chưa chắc", "Nguồn: spec.md §4 · docs/CONTRACT.md · dữ liệu mẫu trong data/")
    steps = [
        (70, "01", "HỌC VIÊN HỎI", "Hạn nộp / phòng / lịch", TEAL),
        (520, "02", "TRA CỨU", "18 tin · 108 buổi · 8 thread", LIME),
        (970, "03", "QUYẾT ĐỊNH", "1 lần gọi model", AMBER),
        (1420, "04", "HẬU KIỂM", "Nguồn + luật cứng", CORAL),
    ]
    for x, n, head, sub, c in steps:
        rounded(d, (x, 320, x + 390, 520), CARD, 24, outline=LINE, width=2)
        d.text((x + 26, 347), n, font=font(28, True), fill=c)
        paragraph(d, (x + 26, 398), head, 24, WHITE, 335, bold=True)
        paragraph(d, (x + 26, 454), sub, 21, MUTED, 335)
    for x in [470, 920, 1370]:
        d.line((x, 420, x + 42, 420), fill=TEAL, width=4)
        d.polygon([(x + 42, 410), (x + 60, 420), (x + 42, 430)], fill=TEAL)

    rounded(d, (70, 590, 910, 920), (17, 43, 54), 26, outline=(34, 93, 99), width=2)
    label(d, (110, 628), "AI ĐƯỢC PHÉP", TEAL)
    paragraph(d, (110, 680), "Hiểu câu hỏi tự nhiên, chọn câu trả lời / hỏi lại / chuyển TA dựa trên JSON căn cứ.", 29, WHITE, 730, 1.25)
    paragraph(d, (110, 800), "Kết quả rõ ràng luôn kèm mã nguồn để người học tự kiểm chứng.", 24, MUTED, 730)

    rounded(d, (950, 590, 1850, 920), (53, 35, 39), 26, outline=(117, 69, 64), width=2)
    label(d, (990, 628), "AI KHÔNG ĐƯỢC PHÉP", CORAL)
    paragraph(d, (990, 680), "Không đoán hạn / phòng khi thiếu nguồn, có mâu thuẫn hoặc chưa chốt.", 28, WHITE, 790, 1.23)
    paragraph(d, (990, 785), "Không sửa dữ liệu, không phát tin công khai. Phiếu ESC là bản nháp chờ TA duyệt.", 23, MUTED, 790)
    return im


def slide4():
    im, d = base(4, "DEMO", "Hai tình huống: trả lời có nguồn · dừng khi nguồn mâu thuẫn", "Nguồn: eval/run-2.csv · B03 và B06 · output rút gọn từ lượt chạy thật")
    rounded(d, (66, 295, 923, 925), CARD, 26)
    pill(d, 102, 330, "THƯỜNG  /  B03")
    paragraph(d, (102, 398), "“Chiều 04/05 lab L3B học phòng nào?”", 29, WHITE, 750, 1.2, True)
    d.line((102, 492, 875, 492), fill=LINE, width=2)
    label(d, (102, 528), "OUTPUT THỰC TẾ", LIME, 18)
    paragraph(d, (102, 570), "LAB 12 · 04/05/2027 · C201, E402, H104 hoặc H201", 30, WHITE, 750, 1.2, True)
    pill(d, 102, 688, "SCH-L3B-LAB-12", LIME, (42, 55, 42), 18)
    paragraph(d, (102, 770), "Đạt · 1/1 · trích đúng bốn phòng và mã nguồn.", 24, MUTED, 750)

    rounded(d, (965, 295, 1854, 925), CARD, 26)
    pill(d, 1000, 330, "KHÓ  /  B06", AMBER, (66, 49, 31))
    paragraph(d, (1000, 398), "“LAB 13 lớp L3B hạn nộp mấy giờ?”", 29, WHITE, 790, 1.2, True)
    d.line((1000, 492, 1812, 492), fill=LINE, width=2)
    label(d, (1000, 528), "OUTPUT THỰC TẾ · RÚT GỌN", AMBER, 18)
    paragraph(d, (1000, 570), "TB-11: 23:59  ·  TB-12: 18:00\nChưa chốt → [CHUYỂN TA]", 32, WHITE, 780, 1.35, True)
    pill(d, 1000, 692, "PHIẾU NHÁP ESC-FA8B1E · CHƯA GỬI", AMBER, (66, 49, 31), 17)
    paragraph(d, (1000, 770), "Đạt · không chọn giờ tuỳ ý; chuyển người duyệt.", 24, MUTED, 780)

    rounded(d, (66, 950, 1854, 1000), (54, 43, 29), 16)
    paragraph(d, (88, 958), "Dự phòng khi mất mạng: cần chuẩn bị video demo offline trước buổi trình bày (chưa có video trong repo).", 19, AMBER, 1700)
    return im


def slide5():
    im, d = base(5, "EVALUATION", "Lượt 2 đạt chuẩn; lỗi trích nguồn của lượt 1 đã được sửa", "Nguồn: eval/README.md · eval/report.md · eval/run-1.csv · eval/run-2.csv")
    # Dataset strip
    rounded(d, (66, 285, 1854, 410), CARD, 22)
    label(d, (100, 308), "DỮ LIỆU KIỂM THỬ", TEAL, 18)
    paragraph(d, (100, 350), "108 lịch (training-ops)   ·   18 thông báo mẫu   ·   8 thread mẫu   ·   20 câu benchmark", 25, WHITE, 1650, bold=True)

    rounded(d, (66, 435, 815, 870), CARD, 24)
    pill(d, 100, 465, "LƯỢT 1 · GEMINI 3.5 FLASH LITE")
    metric(d, 100, 535, "17/20", "85% tổng câu", TEAL, 78, 620)
    paragraph(d, (100, 685), "Run ID\nrun-1@20261128-080232", 24, WHITE, 620, 1.3, True)
    paragraph(d, (100, 785), "Trích đúng nguồn: 9/12 (75%)", 23, CORAL, 620, bold=True)

    rounded(d, (850, 435, 1590, 870), CARD, 24)
    pill(d, 884, 465, "LƯỢT 2 · GEMINI 3.1 FLASH LITE", LIME, (42, 55, 42))
    metric(d, 884, 535, "19/20", "95% tổng câu", LIME, 78, 620)
    paragraph(d, (884, 685), "Run ID\nrun-2@20261128-090447", 24, WHITE, 620, 1.3, True)
    paragraph(d, (884, 785), "Trích đúng nguồn: 12/12 (100%)", 23, LIME, 620, bold=True)

    rounded(d, (1625, 435, 1854, 870), (49, 42, 31), 22, outline=(110, 88, 54), width=2)
    label(d, (1650, 472), "CHUẨN", AMBER, 17)
    paragraph(d, (1650, 520), "≥85%\n0 báo sai\n100% từ chối an toàn", 24, WHITE, 180, 1.5, True)

    rounded(d, (66, 900, 1854, 985), (53, 35, 39), 18)
    paragraph(d, (95, 918), "Còn 1 lỗi: B10 thiếu [CHUYỂN TA] khi không có nguồn. Lượt 2: 4/4 câu từ chối đạt; 20/20 không báo sai.", 23, WHITE, 1700, 1.2)
    return im


def slide6():
    im, d = base(6, "COST", "Tác động đã đo; chi phí/task chưa có mô phỏng thật", "Nguồn: spec.md §2 · cost/personas.yaml · cost/cost-estimate.md · kiểm tra thư mục cost/")
    rounded(d, (66, 300, 875, 930), CARD, 27)
    pill(d, 102, 338, "IMPACT ĐO TỪ KHẢO SÁT")
    metric(d, 102, 415, "15,95 phút", "tìm kiếm / người / tháng\n(2,65 lần × 6,02 phút)", TEAL, 71, 690)
    d.line((102, 600, 832, 600), fill=LINE, width=2)
    metric(d, 102, 632, "≈186 giờ", "thời gian tìm kiếm / tháng ở quy mô cơ sở 700 người", LIME, 66, 690)
    paragraph(d, (102, 815), "Chưa tính rủi ro trễ hạn hoặc đi nhầm phòng.", 22, MUTED, 690)

    rounded(d, (905, 300, 1854, 930), CARD2, 27)
    label(d, (950, 338), "KỊCH BẢN QUY MÔ ĐÃ CHỐT", AMBER)
    for y, tag, people, color in [(405, "THẤP", "350", TEAL), (500, "CƠ SỞ", "700", LIME), (595, "CAO", "1.000", AMBER)]:
        pill(d, 950, y, tag, color, (36, 52, 59) if color == TEAL else (42, 55, 42) if color == LIME else (66, 49, 31), 17)
        d.text((1135, y - 2), f"{people} học viên", font=font(28, True), fill=WHITE)
    d.line((950, 675, 1808, 675), fill=LINE, width=2)
    label(d, (950, 708), "$/TASK THÀNH CÔNG", CORAL)
    paragraph(d, (950, 755), "CHƯA CÓ SỐ ĐO", 45, CORAL, 800, bold=True)
    paragraph(d, (950, 817), "Chưa có mô phỏng thật ≥50 phiên. `simulate-mock.csv` là dữ liệu mock, không dùng làm kết quả. Model eval lượt 2: gemini-3.1-flash-lite; model mô phỏng chưa xác nhận.", 21, WHITE, 820, 1.25)
    return im


def slide7():
    im, d = base(7, "DECISION", "Quyết định: ITERATE trước khi mở rộng", "Căn cứ: evidence/summary.md · eval/report.md · cost/cost-estimate.md")
    rounded(d, (66, 305, 1265, 950), (17, 43, 54), 30, outline=(34, 93, 99), width=2)
    pill(d, 110, 350, "PAIN CÓ THẬT · GIẢI PHÁP ĐẠT CHUẨN")
    metric(d, 110, 430, "2 nguồn", "đối chiếu độc lập: khảo sát 27 người + 50 câu hỏi Discord công khai", TEAL, 70, 1020)
    d.line((110, 600, 1215, 600), fill=(34, 93, 99), width=2)
    metric(d, 110, 630, "19/20", "câu benchmark đạt ở lượt 2 · 95% · qua chuẩn an toàn", LIME, 77, 1020)
    paragraph(d, (110, 815), "Chỉ pilot đọc-only, với phiếu chuyển TA luôn ở trạng thái nháp chờ duyệt.", 25, WHITE, 1020, 1.25)

    rounded(d, (1300, 305, 1854, 950), CARD, 28)
    label(d, (1340, 355), "VÌ SAO CHƯA GO?", AMBER)
    paragraph(d, (1340, 420), "Chi phí / task chưa được đo bằng ≥50 phiên thật.", 30, WHITE, 450, 1.24, True)
    d.line((1340, 555, 1810, 555), fill=LINE, width=2)
    paragraph(d, (1340, 595), "Kho dữ liệu demo là synthetic. Chưa có người dùng thử ghi nhận trong validation log.", 26, MUTED, 450, 1.3)
    pill(d, 1340, 805, "ITERATE → PILOT", TEAL)
    return im


def slide8():
    im, d = base(8, "NEXT WEEK", "Một tuần nữa: đóng lỗi, đo chi phí, thử với người dùng", "Nguồn: eval/report.md §4 · validation/log.md · cost/personas.yaml")
    actions = [
        (300, "01", "ĐÓNG LỖI NO-SOURCE", "B10 đã từ chối thay vì chuyển TA. Ép tạo phiếu nháp khi thiếu nguồn; thêm retry timeout.", CORAL),
        (500, "02", "ĐO CHI PHÍ THẬT", "Chạy ≥50 phiên theo run-2, ghi model/token/chi phí mỗi task thành công và so với impact 15,95 phút/người/tháng.", AMBER),
        (700, "03", "PILOT CÓ GIÁM SÁT", "Thử read-only với L3A, L3B và TA; ghi lại hành vi. Chuẩn bị video demo offline — validation log hiện chưa có phiên thử.", TEAL),
    ]
    for y, n, title, body, c in actions:
        rounded(d, (66, y, 1854, y + 160), CARD, 24, outline=LINE, width=2)
        rounded(d, (95, y + 34, 169, y + 108), (31, 51, 66), 20)
        d.text((113, y + 50), n, font=font(28, True), fill=c)
        label(d, (205, y + 28), title, c, 20)
        paragraph(d, (205, y + 69), body, 25, WHITE, 1560, 1.22)
    rounded(d, (66, 910, 1854, 985), (17, 43, 54), 18)
    paragraph(d, (98, 928), "Mốc kết thúc: có số $/task được tái lập, lỗi B10 đã qua kiểm tra, và quyết định pilot dựa trên quan sát thật.", 23, TEAL, 1700, bold=True)
    return im


def main():
    slides = [slide1(), slide2(), slide3(), slide4(), slide5(), slide6(), slide7(), slide8()]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    slides[0].save(OUT, "PDF", resolution=144.0, save_all=True, append_images=slides[1:], quality=92)
    print(f"Created {OUT} ({len(slides)} slides)")


if __name__ == "__main__":
    main()
