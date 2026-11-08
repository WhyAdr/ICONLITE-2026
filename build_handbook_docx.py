import os
import re
from PIL import Image
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

MD_PATH = 'ICONLITE_ONT_Amplicon_Sequencing_Handbook.md'
OUT_DOCX = 'ICONLITE_ONT_Amplicon_Sequencing_Handbook.docx'

BLUE = RGBColor(0x17, 0x69, 0xAA)
DARK_BLUE = RGBColor(0x0F, 0x4C, 0x7A)
TEAL = RGBColor(0x1F, 0x7A, 0x6F)
AMBER = RGBColor(0xEA, 0xBF, 0x45)
INK = RGBColor(0x2B, 0x2F, 0x36)
GRAY = RGBColor(0x5F, 0x6B, 0x7A)
LIGHT_GRAY = RGBColor(0x8C, 0x9B, 0xAA)

HEX_BLUE = "1769AA"
HEX_PALE_BLUE = "EAF3FA"
HEX_PALE_AMBER = "FFF6D9"
HEX_PALE_TEAL = "E8F5F3"
HEX_BORDER = "D5DEE6"
HEX_CODE_BG = "F4F6F8"

def set_cell_margins(cell, top=70, bottom=70, left=100, right=100):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    tcPr.append(shd)

def set_table_borders(table, color_hex="D5DEE6"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}>'
                        f'<w:top w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
                        f'<w:bottom w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
                        f'<w:left w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
                        f'<w:right w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
                        f'<w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
                        f'<w:insideV w:val="single" w:sz="4" w:space="0" w:color="{color_hex}"/>'
                        f'</w:tblBorders>')
    tblPr.append(borders)

def apply_callout_style(paragraph, bg_hex, border_hex):
    pPr = paragraph._p.get_or_add_pPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_hex}"/>')
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}>'
                     f'<w:left w:val="single" w:sz="24" w:space="12" w:color="{border_hex}"/>'
                     f'</w:pBdr>')
    pPr.append(shd)
    pPr.append(pBdr)
    paragraph.paragraph_format.left_indent = Inches(0.2)
    paragraph.paragraph_format.right_indent = Inches(0.1)
    paragraph.paragraph_format.space_before = Pt(5)
    paragraph.paragraph_format.space_after = Pt(7)

def add_field(p, field_name):
    fldSimple = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="{field_name}"/>')
    p._p.append(fldSimple)

def parse_inline_formatting(paragraph, text, default_size=10.0, default_color=INK, default_bold=False, default_italic=False, font_name="Arial"):
    # Splits by tokens: **bold**, *italic*, `code`, and plain math expressions
    tokens = re.split(r'(\*\*.*?\*\*|\*[^\*]+?\*|`.*?`|\$\$.*?\$\$|\$.*?\$)', text)
    for token in tokens:
        if not token:
            continue
        if token.startswith('**') and token.endswith('**') and len(token) >= 4:
            run = paragraph.add_run(token[2:-2])
            run.font.name = font_name
            run.font.size = Pt(default_size)
            run.font.color.rgb = default_color
            run.bold = True
            run.italic = default_italic
        elif token.startswith('*') and token.endswith('*') and len(token) >= 2:
            run = paragraph.add_run(token[1:-1])
            run.font.name = font_name
            run.font.size = Pt(default_size)
            run.font.color.rgb = default_color
            run.bold = default_bold
            run.italic = True
        elif token.startswith('`') and token.endswith('`') and len(token) >= 2:
            run = paragraph.add_run(token[1:-1])
            run.font.name = "Courier New"
            run.font.size = Pt(max(8.5, default_size - 1.0))
            run.font.color.rgb = RGBColor(0x1B, 0x3E, 0x5F)
            run.bold = default_bold
            run.italic = default_italic
        elif token.startswith('$$') and token.endswith('$$') and len(token) >= 4:
            # Display math in prose
            clean_math = token[2:-2].strip()
            clean_math = clean_math.replace('\\text{', '').replace('}', '').replace('\\times', '×').replace('\\approx', '≈')
            clean_math = clean_math.replace('\\cdot', '·').replace('\\sum', 'Σ').replace('\\le', '≤').replace('\\ge', '≥')
            run = paragraph.add_run(clean_math)
            run.font.name = "Cambria Math"
            run.font.size = Pt(default_size)
            run.font.color.rgb = DARK_BLUE
            run.bold = True
        elif token.startswith('$') and token.endswith('$') and len(token) >= 2:
            clean_math = token[1:-1].strip()
            clean_math = clean_math.replace('\\text{', '').replace('}', '').replace('\\times', '×').replace('\\approx', '≈')
            clean_math = clean_math.replace('\\cdot', '·').replace('\\sum', 'Σ').replace('\\le', '≤').replace('\\ge', '≥')
            run = paragraph.add_run(clean_math)
            run.font.name = "Cambria Math"
            run.font.size = Pt(default_size)
            run.font.color.rgb = DARK_BLUE
            run.italic = True
        else:
            run = paragraph.add_run(token)
            run.font.name = font_name
            run.font.size = Pt(default_size)
            run.font.color.rgb = default_color
            run.bold = default_bold
            run.italic = default_italic

def main():
    with open(MD_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    doc = docx.Document()
    
    # Configure Section 1 (Cover Page)
    sec_cover = doc.sections[0]
    sec_cover.page_width = Inches(8.27)
    sec_cover.page_height = Inches(11.69)
    sec_cover.top_margin = Inches(1.2)
    sec_cover.bottom_margin = Inches(1.0)
    sec_cover.left_margin = Inches(1.0)
    sec_cover.right_margin = Inches(1.0)

    # Build Cover Page
    p_pre = doc.add_paragraph()
    p_pre.paragraph_format.space_before = Pt(80)
    p_pre.paragraph_format.space_after = Pt(12)
    r = p_pre.add_run("ICONLITE Workshop 2026")
    r.font.name = "Arial"
    r.font.size = Pt(14)
    r.font.color.rgb = GRAY
    r.bold = True

    p_title = doc.add_paragraph()
    p_title.paragraph_format.space_after = Pt(14)
    r = p_title.add_run("From Sample to Species")
    r.font.name = "Arial"
    r.font.size = Pt(36)
    r.font.color.rgb = BLUE
    r.bold = True

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(10)
    r = p_sub.add_run("Amplicon Sequencing Using Oxford Nanopore Technology")
    r.font.name = "Arial"
    r.font.size = Pt(18)
    r.font.color.rgb = DARK_BLUE
    r.bold = True

    p_desc = doc.add_paragraph()
    p_desc.paragraph_format.space_after = Pt(100)
    r = p_desc.add_run("Companion Laboratory and Bioinformatics Handbook")
    r.font.name = "Arial"
    r.font.size = Pt(13)
    r.font.color.rgb = INK

    p_kit = doc.add_paragraph()
    p_kit.paragraph_format.space_after = Pt(6)
    r = p_kit.add_run("Native Barcoding Kit 24 V14 (SQK-NBD114.24) · PromethION · EPI2ME wf-16s")
    r.font.name = "Arial"
    r.font.size = Pt(10.5)
    r.font.color.rgb = GRAY
    r.bold = True

    p_ver = doc.add_paragraph()
    p_ver.paragraph_format.space_after = Pt(30)
    r = p_ver.add_run("Version 1.0 (draft) · 8 November 2026")
    r.font.name = "Arial"
    r.font.size = Pt(10)
    r.font.color.rgb = INK

    p_warn = doc.add_paragraph()
    apply_callout_style(p_warn, HEX_PALE_AMBER, "EABF45")
    r_w = p_warn.add_run("Educational companion. ")
    r_w.bold = True
    r_w.font.name = "Arial"
    r_w.font.size = Pt(9.5)
    r_w.font.color.rgb = INK
    r_w2 = p_warn.add_run("The current Oxford Nanopore Technologies protocol remains the controlling reference for any actual laboratory work. For research use only.")
    r_w2.font.name = "Arial"
    r_w2.font.size = Pt(9.5)
    r_w2.font.color.rgb = INK
    r_w2.italic = True

    # Section 2: Main Document
    sec_main = doc.add_section()
    sec_main.page_width = Inches(8.27)
    sec_main.page_height = Inches(11.69)
    sec_main.top_margin = Inches(0.9)
    sec_main.bottom_margin = Inches(0.85)
    sec_main.left_margin = Inches(1.0)
    sec_main.right_margin = Inches(1.0)
    sec_main.header.is_linked_to_previous = False
    sec_main.footer.is_linked_to_previous = False

    # Header
    hp = sec_main.header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hrun = hp.add_run("ICONLITE 2026 · ONT Amplicon Sequencing Handbook")
    hrun.font.name = "Arial"
    hrun.font.size = Pt(8.5)
    hrun.font.color.rgb = GRAY

    # Footer
    fp = sec_main.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    frun1 = fp.add_run("v1.0 draft · 8 November 2026                   Page ")
    frun1.font.name = "Arial"
    frun1.font.size = Pt(8.5)
    frun1.font.color.rgb = GRAY
    add_field(fp, "PAGE")
    frun2 = fp.add_run(" of ")
    frun2.font.name = "Arial"
    frun2.font.size = Pt(8.5)
    frun2.font.color.rgb = GRAY
    add_field(fp, "NUMPAGES")

    # Parsing markdown
    i = 0
    # Skip front matter in lines (Cover is already written)
    # Find start of Table of Contents or About This Handbook
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("## Table of Contents") or line.startswith("## About This Handbook"):
            break
        i += 1

    in_table = False
    table_lines = []
    in_code_block = False
    code_lines = []
    in_callout = False
    callout_lines = []
    callout_type = "NOTE"

    def flush_table():
        nonlocal in_table, table_lines
        if not table_lines:
            in_table = False
            return
        
        # Clean rows
        rows_data = []
        for tl in table_lines:
            cells = [c.strip() for c in tl.split('|')[1:-1]]
            # check if separator row
            if all(re.match(r'^:?-+:?$', c) for c in cells):
                continue
            rows_data.append(cells)
        
        if rows_data:
            num_cols = max(len(r) for r in rows_data)
            # Normalize row lengths
            for r in rows_data:
                while len(r) < num_cols:
                    r.append("")
            
            table = doc.add_table(rows=len(rows_data), cols=num_cols)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            set_table_borders(table, HEX_BORDER)
            
            content_width_in = 6.27
            col_width = Inches(content_width_in / num_cols)
            
            for row_idx, r_data in enumerate(rows_data):
                row = table.rows[row_idx]
                trPr = row._tr.get_or_add_trPr()
                trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))
                if row_idx == 0:
                    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

                for col_idx, cell_text in enumerate(r_data):
                    cell = row.cells[col_idx]
                    cell.width = col_width
                    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
                    set_cell_margins(cell, top=50, bottom=50, left=80, right=80)
                    
                    if row_idx == 0:
                        set_cell_shading(cell, HEX_BLUE)
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_before = Pt(2)
                        p.paragraph_format.space_after = Pt(2)
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        parse_inline_formatting(p, cell_text, default_size=9.0, default_color=RGBColor(0xFF, 0xFF, 0xFF), default_bold=True)
                    else:
                        bg_color = "FFFFFF" if row_idx % 2 == 1 else HEX_PALE_BLUE
                        set_cell_shading(cell, bg_color)
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_before = Pt(2)
                        p.paragraph_format.space_after = Pt(2)
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        parse_inline_formatting(p, cell_text, default_size=8.5, default_color=INK)
            
            # spacing after table
            sp_p = doc.add_paragraph()
            sp_p.paragraph_format.space_after = Pt(6)
        
        table_lines = []
        in_table = False

    def flush_callout():
        nonlocal in_callout, callout_lines, callout_type
        if not callout_lines:
            in_callout = False
            return
        
        bg_hex = HEX_PALE_BLUE
        border_hex = HEX_BLUE
        if callout_type == "WARNING":
            bg_hex = HEX_PALE_AMBER
            border_hex = "EABF45"
        elif callout_type == "TIP":
            bg_hex = HEX_PALE_TEAL
            border_hex = "1F7A6F"
        elif callout_type == "IMPORTANT":
            bg_hex = HEX_PALE_AMBER
            border_hex = "0F4C7A"

        p = doc.add_paragraph()
        apply_callout_style(p, bg_hex, border_hex)
        full_text = " ".join(callout_lines).strip()
        parse_inline_formatting(p, full_text, default_size=9.5, default_color=INK)
        
        callout_lines = []
        in_callout = False

    def flush_code():
        nonlocal in_code_block, code_lines
        if not code_lines:
            in_code_block = False
            return
        
        p = doc.add_paragraph()
        apply_callout_style(p, HEX_CODE_BG, "8C9BAA")
        full_code = "\n".join(code_lines)
        run = p.add_run(full_code)
        run.font.name = "Courier New"
        run.font.size = Pt(8.5)
        run.font.color.rgb = RGBColor(0x2B, 0x2F, 0x36)
        code_lines = []
        in_code_block = False

    while i < len(lines):
        raw_line = lines[i]
        line = raw_line.strip()

        # Handle code blocks
        if line.startswith("```"):
            if in_code_block:
                flush_code()
            else:
                if in_table: flush_table()
                if in_callout: flush_callout()
                in_code_block = True
                code_lines = []
            i += 1
            continue
        
        if in_code_block:
            code_lines.append(raw_line.rstrip('\r\n'))
            i += 1
            continue

        # Handle callouts
        if line.startswith(">"):
            if in_table: flush_table()
            quote_content = line[1:].strip()
            if quote_content.startswith("[!NOTE]"):
                if in_callout: flush_callout()
                in_callout = True
                callout_type = "NOTE"
                callout_lines = []
            elif quote_content.startswith("[!TIP]"):
                if in_callout: flush_callout()
                in_callout = True
                callout_type = "TIP"
                callout_lines = []
            elif quote_content.startswith("[!WARNING]"):
                if in_callout: flush_callout()
                in_callout = True
                callout_type = "WARNING"
                callout_lines = []
            elif quote_content.startswith("[!IMPORTANT]"):
                if in_callout: flush_callout()
                in_callout = True
                callout_type = "IMPORTANT"
                callout_lines = []
            else:
                if not in_callout:
                    in_callout = True
                    callout_type = "NOTE"
                    callout_lines = []
                callout_lines.append(quote_content)
            i += 1
            continue
        else:
            if in_callout:
                flush_callout()

        # Handle tables
        if line.startswith("|") and line.endswith("|"):
            if not in_table:
                in_table = True
                table_lines = []
            table_lines.append(line)
            i += 1
            continue
        else:
            if in_table:
                flush_table()

        # Blank lines
        if not line:
            i += 1
            continue

        # Horizontal Rule
        if line == "---":
            i += 1
            continue

        # Headings
        if line.startswith("# "):
            title_text = line[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.page_break_before = True
            p.paragraph_format.space_before = Pt(18)
            p.paragraph_format.space_after = Pt(10)
            parse_inline_formatting(p, title_text, default_size=20.0, default_color=BLUE, default_bold=True)
            i += 1
            continue

        if line.startswith("## "):
            title_text = line[3:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(16)
            p.paragraph_format.space_after = Pt(8)
            parse_inline_formatting(p, title_text, default_size=15.0, default_color=BLUE, default_bold=True)
            i += 1
            continue

        if line.startswith("### "):
            title_text = line[4:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(14)
            p.paragraph_format.space_after = Pt(6)
            parse_inline_formatting(p, title_text, default_size=12.0, default_color=DARK_BLUE, default_bold=True)
            i += 1
            continue

        if line.startswith("#### "):
            title_text = line[5:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(10)
            p.paragraph_format.space_after = Pt(4)
            p.paragraph_format.keep_with_next = True
            parse_inline_formatting(p, title_text, default_size=10.0, default_color=BLUE, default_bold=True)
            i += 1
            continue

        # Images
        img_match = re.match(r'^!\[(.*?)\]\((.*?)\)$', line)
        if img_match:
            alt_text, img_path = img_match.groups()
            img_path = img_path.strip()
            if os.path.exists(img_path):
                try:
                    with Image.open(img_path) as im:
                        orig_w, orig_h = im.size
                        aspect = orig_h / orig_w
                    
                    max_w = 6.0
                    target_w = min(max_w, 6.0)
                    target_h = target_w * aspect
                    if target_h > 4.2:
                        target_h = 4.2
                        target_w = target_h / aspect

                    p_img = doc.add_paragraph()
                    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p_img.paragraph_format.space_before = Pt(10)
                    p_img.paragraph_format.space_after = Pt(4)
                    p_img.paragraph_format.keep_with_next = True
                    p_img.add_run().add_picture(img_path, width=Inches(target_w), height=Inches(target_h))
                except Exception as e:
                    p_err = doc.add_paragraph(f"[Image load error: {img_path} - {e}]")
                    p_err.paragraph_format.space_after = Pt(4)
            else:
                p_err = doc.add_paragraph(f"[Image not found: {img_path}]")
                p_err.paragraph_format.space_after = Pt(4)
            i += 1
            continue

        # Captions (*Figure X. ...*)
        if line.startswith("*Figure") and line.endswith("*"):
            cap_text = line[1:-1].strip()
            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(2)
            p_cap.paragraph_format.space_after = Pt(12)
            parse_inline_formatting(p_cap, cap_text, default_size=8.5, default_color=GRAY, default_italic=True)
            i += 1
            continue

        # Lists: Unordered
        bullet_match = re.match(r'^([*\-]\s+)(.*)$', line)
        if bullet_match:
            b_text = bullet_match.group(2)
            p = doc.add_paragraph(style='List Bullet')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(3)
            parse_inline_formatting(p, b_text, default_size=10.0, default_color=INK)
            i += 1
            continue

        # Lists: Numbered
        num_match = re.match(r'^(\d+\.\s+)(.*)$', line)
        if num_match:
            n_text = num_match.group(2)
            p = doc.add_paragraph(style='List Number')
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(3)
            parse_inline_formatting(p, n_text, default_size=10.0, default_color=INK)
            i += 1
            continue

        # Math block: $$ ... $$
        if line.startswith("$$") and line.endswith("$$") and len(line) >= 4:
            math_text = line[2:-2].strip()
            p_m = doc.add_paragraph()
            p_m.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_m.paragraph_format.space_before = Pt(6)
            p_m.paragraph_format.space_after = Pt(6)
            parse_inline_formatting(p_m, f"$${math_text}$$", default_size=10.5, default_color=DARK_BLUE, default_bold=True)
            i += 1
            continue

        # Regular Body Paragraph
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        parse_inline_formatting(p, line, default_size=10.0, default_color=INK)
        i += 1

    if in_table:
        flush_table()
    if in_callout:
        flush_callout()
    if in_code_block:
        flush_code()

    doc.save(OUT_DOCX)
    print(f"Successfully generated {OUT_DOCX}")

if __name__ == '__main__':
    main()
