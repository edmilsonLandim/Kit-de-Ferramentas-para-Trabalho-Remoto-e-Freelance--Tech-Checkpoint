"""Converte o entregaveis-1.md (subconjunto de Markdown usado) para .docx."""
import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

SRC, DST = sys.argv[1], sys.argv[2]
NAVY = RGBColor(0x1F, 0x4E, 0x79)
GREY = RGBColor(0x59, 0x59, 0x59)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21), Cm(29.7)
for side in ("left_margin", "right_margin"):
    setattr(sec, side, Cm(2.2))
sec.top_margin = sec.bottom_margin = Cm(2)

st = doc.styles
st["Normal"].font.name = "Calibri"
st["Normal"].font.size = Pt(10.5)
st["Normal"].paragraph_format.space_after = Pt(4)
for name, size in (("Title", 20), ("Heading 1", 15), ("Heading 2", 12.5), ("Heading 3", 11)):
    s = st[name]
    s.font.name = "Calibri"
    s.font.size = Pt(size)
    s.font.bold = True
    s.font.color.rgb = NAVY
    s.paragraph_format.space_before = Pt(12 if name != "Title" else 0)
    s.paragraph_format.space_after = Pt(6)
    s.paragraph_format.keep_with_next = True
    rpr = s.element.get_or_add_rPr()
    fonts = rpr.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        rpr.append(fonts)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        fonts.set(qn(a), "Calibri")
    # remove theme font overrides
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if fonts.get(qn(a)) is not None:
            del fonts.attrib[qn(a)]

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*]+\*|`[^`]+`)")


def add_inline(par, text, base_italic=False, color=None):
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            r = par.add_run(part[2:-2]); r.bold = True
        elif part.startswith("`") and part.endswith("`"):
            r = par.add_run(part[1:-1]); r.font.name = "Consolas"; r.font.size = Pt(9.5)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            r = par.add_run(part[1:-1]); r.italic = True
        else:
            r = par.add_run(part)
        if base_italic:
            r.italic = True
        if color:
            r.font.color.rgb = color


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcolor)
    tcPr.append(shd)


def left_border(par, color="1F4E79"):
    pPr = par._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    for k, v in (("w:val", "single"), ("w:sz", "18"), ("w:space", "8"), ("w:color", color)):
        left.set(qn(k), v)
    bdr.append(left)
    pPr.append(bdr)


def add_table(rows, quoted=False):
    rows = [r for r in rows if not re.match(r"^\|?\s*:?-{3,}", r.strip().strip("|").strip() or "---")]
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    ncol = max(len(r) for r in cells)
    t = doc.add_table(rows=len(cells), cols=ncol)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, r in enumerate(cells):
        for j in range(ncol):
            c = t.cell(i, j)
            c.paragraphs[0].paragraph_format.space_after = Pt(0)
            add_inline(c.paragraphs[0], r[j] if j < len(r) else "")
            for run in c.paragraphs[0].runs:
                run.font.size = Pt(9.5)
                if i == 0:
                    run.bold = True
                    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            if i == 0:
                shade(c, "1F4E79")
            elif i % 2 == 0:
                shade(c, "EAF1F8")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_code(lines):
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    c = t.cell(0, 0)
    shade(c, "F2F2F2")
    first = True
    for ln in lines:
        p = c.paragraphs[0] if first else c.add_paragraph()
        first = False
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(ln if ln else " ")
        r.font.name = "Consolas"; r.font.size = Pt(9)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


raw = open(SRC, encoding="utf8").read().splitlines()
lines = []
ITEM = re.compile(r"^(\d+\.|-)\s")
for ln in raw:
    q = ln.startswith(">")
    body = ln[1:] if q else ln
    if body.startswith(" ") and q:
        body = body[1:]
    prev = lines[-1] if lines else ""
    pq = prev.startswith(">")
    pbody = (prev[1:].lstrip() if pq else prev)
    if (body.startswith("  ") and body.strip() and q == pq and not ITEM.match(body.strip())
            and ITEM.match(pbody.strip()) and not body.strip().startswith("|")):
        lines[-1] = prev.rstrip() + " " + body.strip()
        continue
    bs, ps = body.strip(), pbody.strip()
    if (q and pq and bs and ps and not ITEM.match(bs) and not bs.startswith(("|", "**", "["))
            and not ps.startswith("|") and not ps.endswith(("**", ",", "]", ":"))):
        lines[-1] = prev.rstrip() + " " + bs
        continue
    lines.append(ln)
i = 0
while i < len(lines):
    ln = lines[i]
    s = ln.strip()
    if s.startswith("```"):
        j = i + 1
        block = []
        while not lines[j].strip().startswith("```"):
            block.append(lines[j]); j += 1
        add_code(block); i = j + 1; continue
    if s.startswith("|"):
        block = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            block.append(lines[i]); i += 1
        add_table(block); continue
    if s.startswith(">"):
        block = []
        while i < len(lines) and lines[i].strip().startswith(">"):
            block.append(lines[i].strip()[1:].strip()); i += 1
        # quoted tables inside the block
        k = 0
        while k < len(block):
            b = block[k]
            if b.startswith("|"):
                tb = []
                while k < len(block) and block[k].startswith("|"):
                    tb.append(block[k]); k += 1
                add_table(tb); continue
            if b == "":
                k += 1; continue
            m = re.match(r"^(\d+\.|-)\s+(.*)", b)
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.6 if not m else 1.1)
            if m:
                p.paragraph_format.first_line_indent = Cm(-0.5)
            p.paragraph_format.space_after = Pt(2)
            left_border(p)
            if m:
                prefix = m.group(1) + " " if m.group(1) != "-" else "– "
                add_inline(p, prefix + m.group(2))
            else:
                add_inline(p, b)
            k += 1
        doc.add_paragraph().paragraph_format.space_after = Pt(2)
        continue
    if s == "---":
        p = doc.add_paragraph()
        pPr = p._p.get_or_add_pPr()
        bdr = OxmlElement("w:pBdr"); bot = OxmlElement("w:bottom")
        for k, v in (("w:val", "single"), ("w:sz", "6"), ("w:space", "1"), ("w:color", "BFBFBF")):
            bot.set(qn(k), v)
        bdr.append(bot); pPr.append(bdr)
        i += 1; continue
    if s.startswith("# "):
        doc.add_paragraph(s[2:], style="Title"); i += 1; continue
    if s.startswith("## "):
        doc.add_paragraph(s[3:], style="Heading 1"); i += 1; continue
    if s.startswith("### "):
        doc.add_paragraph(s[4:], style="Heading 2"); i += 1; continue
    m = re.match(r"^(\d+)\.\s+(.*)", s)
    if m:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.8)
        p.paragraph_format.first_line_indent = Cm(-0.5)
        p.paragraph_format.space_after = Pt(2)
        add_inline(p, m.group(1) + ".  " + m.group(2)); i += 1; continue
    if s.startswith("- "):
        p = doc.add_paragraph(style="List Bullet")
        add_inline(p, s[2:]); i += 1; continue
    if not s:
        i += 1; continue
    # paragraph: join continuation lines
    buf = [s]
    i += 1
    while i < len(lines) and lines[i].strip() and not re.match(r"^(#|>|\||```|- |\d+\.\s|---|\*\*[^*]+:\*\*)", lines[i].strip()):
        buf.append(lines[i].strip()); i += 1
    p = doc.add_paragraph()
    add_inline(p, " ".join(buf))

# rodapé com número de página
fp = sec.footer.paragraphs[0]
fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run("Entregáveis 1 – Sessão 1 – AI Productivity Sprint   |   página ")
r.font.size = Pt(8); r.font.color.rgb = GREY
r2 = fp.add_run()
for tag, txt in (("begin", None), (None, "PAGE"), ("end", None)):
    if tag:
        e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), tag)
    else:
        e = OxmlElement("w:instrText"); e.set(qn("xml:space"), "preserve"); e.text = txt
    r2._r.append(e)
r2.font.size = Pt(8)

doc.save(DST)
print("ok", DST)
