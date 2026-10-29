#!/usr/bin/env python3
"""
Sinh file .docx văn bản hành chính đúng thể thức Nghị định 30/2020/NĐ-CP.

Cài đặt (một lần):
    pip install python-docx

Dùng:
    python tao_docx.py van-ban.json -o "Cong-van-125.docx"
    python tao_docx.py van-ban.json -o out.docx --co-chu 14 --le-trai 30 --le-phai 15

Cấu trúc JSON (các khoá không bắt buộc có thể bỏ):
{
  "co_quan_chu_quan": "ỦY BAN NHÂN DÂN TỈNH ...",   // ô 2, dòng trên
  "co_quan": "VĂN PHÒNG ỦY BAN NHÂN DÂN",           // ô 2, dòng dưới (bắt buộc)
  "so_ky_hieu": "125/UBND-VP",                       // ô 3 (bắt buộc)
  "dia_danh": "Hà Nội",                              // ô 4
  "ngay": "05", "thang": "3", "nam": "2026",
  "ten_loai": "QUYẾT ĐỊNH",                          // ô 5a, bỏ trống nếu là công văn
  "trich_yeu": "Về việc bổ nhiệm Phó Chánh Văn phòng",
  "cong_van": false,                                 // true: trích yếu thành "V/v ..." dưới số
  "blocks": [ ... ],                                 // ô 6
  "ky": { "quyen_han": "TM. ỦY BAN NHÂN DÂN", "chuc_vu": "CHỦ TỊCH", "ho_ten": "Nguyễn Văn A" },
  "noi_nhan": ["Như trên", "Chủ tịch UBND tỉnh (để b/c)", "Lưu: VT, HC (2)."],
  "dia_chi": "Số 1 Tràng Tiền, Hà Nội. ĐT: 024.xxxx. Fax: ... E-Mail: ... Website: ..."
}

Các loại block trong "blocks":
  {"t": "p", "text": "...", "align": "justify|center|left|right", "bold": true, "italic": true,
   "indent": 1.27, "size": 14, "space_after": 6, "upper": true}
  {"t": "heading", "text": "I. MỤC ĐÍCH, YÊU CẦU"}       // in hoa, đậm, canh giữa
  {"t": "ky", "text": "QUYẾT ĐỊNH:"}                      // in hoa, đậm, canh giữa
  {"t": "table", "header": true, "widths": [2, 6, 8], "rows": [["A", "B", "C"], ...]}
  {"t": "pagebreak"}
  "Chuỗi thuần" cũng được hiểu là một đoạn văn căn đều.
"""

from __future__ import annotations

import argparse
import json
import sys

try:
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.enum.table import WD_ALIGN_VERTICAL
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Mm, Pt
except ImportError:  # pragma: no cover
    sys.exit("Thiếu thư viện python-docx. Cài bằng: pip install python-docx")

ALIGN = {
    "left": WD_ALIGN_PARAGRAPH.LEFT,
    "center": WD_ALIGN_PARAGRAPH.CENTER,
    "right": WD_ALIGN_PARAGRAPH.RIGHT,
    "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
}


def set_run(run, size, bold=False, italic=False, underline=False, caps=False):
    run.font.name = "Times New Roman"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.underline = underline
    run.font.all_caps = caps
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), "Times New Roman")
    return run


def para(container, text="", align="justify", size=13, bold=False, italic=False,
         indent=0, space_after=6, space_before=0, caps=False, underline=False,
         line=1.15, keep_next=False):
    p = container.add_paragraph()
    p.alignment = ALIGN[align]
    pf = p.paragraph_format
    pf.space_before = Pt(space_before)
    pf.space_after = Pt(space_after)
    pf.line_spacing = line
    if indent:
        pf.first_line_indent = Cm(indent)
    if keep_next:
        pf.keep_with_next = True
    if text:
        set_run(p.add_run(text), size, bold, italic, underline, caps)
    return p


def no_borders(table):
    tbl_pr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "none")
        el.set(qn("w:sz"), "0")
        borders.append(el)
    tbl_pr.append(borders)
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tbl_pr.append(layout)


def zero_cell_margins(table):
    tbl_pr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for edge in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:w"), "0")
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tbl_pr.append(mar)


def set_widths(table, widths_cm):
    table.autofit = False
    for row in table.rows:
        for cell, w in zip(row.cells, widths_cm):
            cell.width = Cm(w)


def cell_para(cell, text="", align="center", size=13, bold=False, italic=False,
              space_after=0, underline=False, first=False):
    p = cell.paragraphs[0] if first and not cell.paragraphs[0].text else cell.add_paragraph()
    p.alignment = ALIGN[align]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.0
    if text:
        set_run(p.add_run(text), size, bold, italic, underline)
    return p


def rule_line(doc, width_chars=12, size=13):
    """Đường kẻ ngắn dưới tiêu đề (dùng dấu cách gạch chân để co giãn được)."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(10)
    set_run(p.add_run(" " * width_chars), size, underline=True)
    return p


def horizontal_line(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(4)
    p_pr = p._p.get_or_add_pPr()
    p_bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "000000")
    p_bdr.append(bottom)
    p_pr.append(p_bdr)
    return p


def add_page_number_footer(section, size=13):
    section.different_first_page_header_footer = True
    footer = section.footer
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    set_run(run, size)
    fld_begin = OxmlElement("w:fldChar")
    fld_begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    fld_end = OxmlElement("w:fldChar")
    fld_end.set(qn("w:fldCharType"), "end")
    run._r.append(fld_begin)
    run._r.append(instr)
    run._r.append(fld_end)


def build(data, out, co_chu=13, le_tren=20, le_duoi=20, le_trai=30, le_phai=15):
    doc = Document()

    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(co_chu)
    style.element.rPr.rFonts.set(qn("w:eastAsia"), "Times New Roman")

    section = doc.sections[0]
    section.page_width = Mm(210)
    section.page_height = Mm(297)
    section.top_margin = Mm(le_tren)
    section.bottom_margin = Mm(le_duoi)
    section.left_margin = Mm(le_trai)
    section.right_margin = Mm(le_phai)
    add_page_number_footer(section)

    # ---- Ô 1, 2, 3, 4 -------------------------------------------------
    head = doc.add_table(rows=3, cols=2)
    no_borders(head)
    zero_cell_margins(head)
    set_widths(head, [7.4, 9.1])

    left0, right0 = head.cell(0, 0), head.cell(0, 1)
    left1, right1 = head.cell(1, 0), head.cell(1, 1)
    left2, right2 = head.cell(2, 0), head.cell(2, 1)

    if data.get("co_quan_chu_quan"):
        cell_para(left0, data["co_quan_chu_quan"].upper(), size=12, first=True)
    else:
        cell_para(left0, "", size=12, first=True)
    cell_para(right0, "CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM", size=12, bold=True, first=True)
    cell_para(left1, data["co_quan"].upper(), size=12, bold=True, underline=True, first=True)
    cell_para(right1, "Độc lập - Tự do - Hạnh phúc", size=13, bold=True, underline=True, first=True)

    so = data["so_ky_hieu"]
    p_so = cell_para(left2, "", size=13, first=True)
    set_run(p_so.add_run("Số: "), 13)
    set_run(p_so.add_run(so), 13)
    if data.get("cong_van") and data.get("trich_yeu"):
        cell_para(left2, "V/v " + data["trich_yeu"], size=12, space_after=0)
    ngay = f"{data.get('dia_danh', '')}, ngày {data.get('ngay', '')} tháng {data.get('thang', '')} năm {data.get('nam', '')}"
    cell_para(right2, ngay, size=13, italic=True, first=True)

    for cell in (left0, left1, left2, right0, right1, right2):
        cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP

    # ---- Ô 5a --------------------------------------------------------
    if data.get("ten_loai"):
        para(doc, data["ten_loai"].upper(), align="center", size=co_chu + 1, bold=True,
             space_before=12, space_after=0)
        if data.get("trich_yeu"):
            para(doc, data["trich_yeu"], align="center", size=co_chu + 1, bold=True,
                 space_after=0)
        rule_line(doc, size=co_chu + 1)

    # ---- Ô 6 ---------------------------------------------------------
    for block in data.get("blocks", []):
        if isinstance(block, str):
            block = {"t": "p", "text": block}
        kind = block.get("t", "p")
        if kind == "p":
            para(doc, block.get("text", ""),
                 align=block.get("align", "justify"),
                 size=block.get("size", co_chu),
                 bold=block.get("bold", False), italic=block.get("italic", False),
                 indent=block.get("indent", 1.27),
                 space_after=block.get("space_after", 6),
                 space_before=block.get("space_before", 0),
                 caps=block.get("upper", False), line=block.get("line", 1.15))
        elif kind in ("heading", "ky"):
            para(doc, block["text"], align="center", size=co_chu + 1, bold=True,
                 space_before=10, space_after=6, caps=(kind == "heading"),
                 keep_next=True)
        elif kind == "table":
            widths = block.get("widths")
            rows = block["rows"]
            table = doc.add_table(rows=len(rows), cols=len(rows[0]))
            table.style = "Table Grid"
            if widths:
                set_widths(table, widths)
            for r, row in enumerate(rows):
                for c, value in enumerate(row):
                    cell = table.cell(r, c)
                    p = cell.paragraphs[0]
                    p.alignment = ALIGN["left"] if c == 0 else ALIGN["center"]
                    p.paragraph_format.space_after = Pt(0)
                    p.paragraph_format.line_spacing = 1.0
                    set_run(p.add_run(str(value)), co_chu - 1,
                            bold=(r == 0 and block.get("header", True)))
            para(doc, "", space_after=6)
        elif kind == "pagebreak":
            doc.add_page_break()

    # ---- Kết văn bản -------------------------------------------------
    para(doc, "", space_after=0)

    ky = data.get("ky", {})
    noi_nhan = data.get("noi_nhan") or []
    tail = doc.add_table(rows=1, cols=2)
    no_borders(tail)
    zero_cell_margins(tail)
    set_widths(tail, [8.6, 7.9])
    left_cell, right_cell = tail.cell(0, 0), tail.cell(0, 1)
    left_cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
    right_cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP

    if noi_nhan:
        cell_para(left_cell, "Nơi nhận:", align="left", size=12, bold=True, italic=True, first=True)
        for item in noi_nhan:
            cell_para(left_cell, "- " + item, align="left", size=11, space_after=0)
    else:
        cell_para(left_cell, "", size=11, first=True)

    if ky.get("quyen_han"):
        cell_para(right_cell, ky["quyen_han"], size=co_chu + 1, bold=True, first=True)
    if ky.get("chuc_vu"):
        cell_para(right_cell, ky["chuc_vu"], size=co_chu + 1, bold=True, first=not ky.get("quyen_han"))
    for _ in range(3):
        cell_para(right_cell, "", size=co_chu)
    cell_para(right_cell, ky.get("ho_ten", ""), size=co_chu + 1, bold=True)

    # ---- Ô 13 --------------------------------------------------------
    if data.get("dia_chi"):
        horizontal_line(doc)
        para(doc, data["dia_chi"], align="left", size=11, indent=0, space_after=0)

    doc.core_properties.title = data.get("trich_yeu", "") or data["so_ky_hieu"]
    doc.core_properties.author = data.get("co_quan", "")
    doc.save(out)
    return out


def main():
    ap = argparse.ArgumentParser(description="Sinh .docx văn bản hành chính theo Nghị định 30/2020/NĐ-CP")
    ap.add_argument("json_file")
    ap.add_argument("-o", "--out", default="van-ban.docx")
    ap.add_argument("--co-chu", type=float, default=13, help="cỡ chữ nội dung (13 hoặc 14)")
    ap.add_argument("--le-tren", type=float, default=20, help="lề trên, mm")
    ap.add_argument("--le-duoi", type=float, default=20, help="lề dưới, mm")
    ap.add_argument("--le-trai", type=float, default=30, help="lề trái, mm")
    ap.add_argument("--le-phai", type=float, default=15, help="lề phải, mm")
    args = ap.parse_args()

    with open(args.json_file, encoding="utf-8") as fh:
        data = json.load(fh)
    if not data.get("co_quan") or not data.get("so_ky_hieu"):
        sys.exit("JSON phải có 'co_quan' và 'so_ky_hieu'")

    out = build(data, args.out, args.co_chu, args.le_tren, args.le_duoi, args.le_trai, args.le_phai)
    print(f"Đã tạo: {out}")


if __name__ == "__main__":
    main()
