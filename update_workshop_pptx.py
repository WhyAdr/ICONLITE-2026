import os
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

PPTX_PATH = 'ICONLITE_ONT_Amplicon_Sequencing_Workshop.pptx'

# Palette
BLUE = RGBColor(0x17, 0x69, 0xAA)
DARK_BLUE = RGBColor(0x0F, 0x4C, 0x7A)
TEAL = RGBColor(0x1F, 0x7A, 0x6F)
AMBER = RGBColor(0xEA, 0xBF, 0x45)
INK = RGBColor(0x2B, 0x2F, 0x36)
GRAY = RGBColor(0x5F, 0x6B, 0x7A)
PALE_BLUE = RGBColor(0xEA, 0xF3, 0xFA)
PALE_AMBER = RGBColor(0xFF, 0xF6, 0xD9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

def add_bullet_list(slide, items, x, y, w, h, font_size=15):
    txBox = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = txBox.text_frame
    tf.word_wrap = True
    for i, itm in enumerate(items):
        p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
        p.text = itm
        p.level = 0
        p.font.name = "Arial"
        p.font.size = Pt(font_size)
        p.font.color.rgb = INK
        p.space_after = Pt(8)
    return txBox

def add_note_card(slide, text, x, y, w, h, font_size=13, bold=True, fill_color=PALE_AMBER, border_color=AMBER, text_color=INK):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.name = "Arial"
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = text_color
    p.alignment = PP_ALIGN.CENTER
    return shape

def update_notes(slide, notes_text):
    if not slide.has_notes_slide:
        slide.notes_slide
    slide.notes_slide.notes_text_frame.text = notes_text

def remove_shape(shape):
    sp = shape._element
    sp.getparent().remove(sp)

def main():
    prs = pptx.Presentation(PPTX_PATH)
    print(f"Loaded {PPTX_PATH} with {len(prs.slides)} slides.")

    # 1. Slide 1 (Cover)
    s1 = prs.slides[0]
    for shape in s1.shapes:
        if shape.has_text_frame and "[Presenter name]" in shape.text_frame.text:
            shape.text_frame.text = "ICONLITE Workshop 2026 · Technical Workshop Session"
            for p in shape.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(14)
                p.font.color.rgb = PALE_BLUE
    update_notes(s1, "Say: Today we follow one sample all the way from collection to a taxonomic species report. At every step, we ground our experimental decisions in three core biological questions: Who is there? What might they be doing? Why is it necessary to know them? [Time: 1.5 min]")
    print("Slide 1 updated.")

    # 2. Slide 6 (Nanopore Sensing Mechanism)
    s6 = prs.slides[5]
    # Remove crude vector shapes (Shapes 2 to 26), keep Shape 0 (Title), Shape 1 (Bullets), Shape 27 (Note), Shape 28 (Slide num)
    shapes_to_remove = []
    for shape in s6.shapes:
        # Keep title, bullets, slide number, and bottom note
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "How does nanopore" in txt or "A pore sits in a membrane" in txt or "Schematic only" in txt or txt.strip() == "6":
                continue
        shapes_to_remove.append(shape)
    for shp in shapes_to_remove:
        remove_shape(shp)
    
    # Add real scientific illustration from Wang 2021
    if os.path.exists("assets/nanopore-sequencing-principle-Wang2021.png"):
        s6.shapes.add_picture("assets/nanopore-sequencing-principle-Wang2021.png", Inches(5.5), Inches(1.5), width=Inches(7.2), height=Inches(4.0))
    update_notes(s6, "Say: Think of reading a printed tape through a keyhole while measuring current. A motor protein ratchets single-stranded DNA through the pore at ~400 bases/sec, and the ionic current shifts with the bases residing in the reader constriction. Basecalling neural networks decode these continuous current shifts into sequence in real time. [Time: 3 min]")
    print("Slide 6 updated.")

    # 3. Slide 7 (ONT Platforms)
    s7 = prs.slides[6]
    # Adjust bullets width and add flow cell image
    for shape in s7.shapes:
        if shape.has_text_frame and "MinION, GridION and PromethION" in shape.text_frame.text:
            shape.width = Inches(7.0)
    if os.path.exists("assets/minion-promethion-flow-cells.png"):
        s7.shapes.add_picture("assets/minion-promethion-flow-cells.png", Inches(8.0), Inches(1.35), width=Inches(4.7), height=Inches(1.6))
    print("Slide 7 updated.")

    # 4. Slide 9 (H1: PCR Amplicon QC)
    s9 = prs.slides[8]
    for shape in list(s9.shapes):
        if shape.has_text_frame and "Insert real agarose gel photo" in shape.text_frame.text:
            remove_shape(shape)
            break
    if os.path.exists("assets/common-amplicon-markers/16S-rRNA-PCR-gel-image.jpg"):
        s9.shapes.add_picture("assets/common-amplicon-markers/16S-rRNA-PCR-gel-image.jpg", Inches(5.5), Inches(1.5), width=Inches(3.4), height=Inches(2.5))
    update_notes(s9, "Say: Protocols count molecules, so convert mass to molarity. A clean amplicon gel shows one sharp band at the target size (~1.5 kb) without non-specific bands or primer-dimers. 200 fmol of a 1,500 bp amplicon corresponds to ~198 ng. [Time: 3 min]")
    print("Slide 9 (H1) updated.")

    # 5. Slide 13 (H5: Flow Cell Loading)
    s13 = prs.slides[12]
    for shape in s13.shapes:
        if shape.has_text_frame and "Flow cell to room temperature" in shape.text_frame.text:
            shape.width = Inches(7.5)
    if os.path.exists("assets/promethion-flow-cell-annotated-3d.png"):
        s13.shapes.add_picture("assets/promethion-flow-cell-annotated-3d.png", Inches(8.5), Inches(1.35), width=Inches(4.2), height=Inches(1.8))
    print("Slide 13 (H5) updated.")

    # 6. Slide 17 (From raw signal to FASTQ reads)
    s17 = prs.slides[16]
    for shape in list(s17.shapes):
        if shape.has_text_frame and "@<read_id>" in shape.text_frame.text:
            remove_shape(shape)
            break
    if os.path.exists("assets/ONT-signal-to-sequence-basecalling.png"):
        s17.shapes.add_picture("assets/ONT-signal-to-sequence-basecalling.png", Inches(0.6), Inches(4.15), width=Inches(7.2), height=Inches(2.4))
    print("Slide 17 updated.")

    # 7. Slide 20 (Transform from Case Study I to Option B: R9 vs R10 Pore Architecture & Basecalling)
    s20 = prs.slides[19]
    # Remove old placeholder shapes
    shapes_to_remove = []
    for shape in s20.shapes:
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Case study I" in txt or txt.strip() == "20":
                continue
        shapes_to_remove.append(shape)
    for shp in shapes_to_remove:
        remove_shape(shp)
    
    # Update title
    for shape in s20.shapes:
        if shape.has_text_frame and "Case study I" in shape.text_frame.text:
            shape.text_frame.text = "Pore Architecture & Accuracy: R9.4.1 vs. R10.4.1"
            p = shape.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(28)
            p.font.bold = True
            p.font.color.rgb = DARK_BLUE

    # Add bullets on the left
    s20_bullets = [
        "R9.4.1: single reader head (~4–5 bp in sensing region); homopolymer runs prone to indel errors",
        "R10.4.1: dual reader heads spaced vertically along the pore lumen",
        "Dual sensing breaks homopolymer ambiguity (>10 bp)",
        "Modal simplex raw read accuracy now exceeds Q20 (>99%)",
        "Dorado neural basecaller: CNN feature extraction + Transformer sequence modeling + CTC decoding"
    ]
    add_bullet_list(s20, s20_bullets, 0.6, 1.45, 4.8, 4.4, font_size=13.5)

    # Add diagrams on the right
    if os.path.exists("assets/ONTR9vsR10-nanopore-diagram.png"):
        s20.shapes.add_picture("assets/ONTR9vsR10-nanopore-diagram.png", Inches(5.6), Inches(1.45), width=Inches(3.6), height=Inches(4.3))
    if os.path.exists("assets/ONT-basecalling-neural-network-diagram.png"):
        s20.shapes.add_picture("assets/ONT-basecalling-neural-network-diagram.png", Inches(9.35), Inches(1.45), width=Inches(3.4), height=Inches(4.3))
    
    add_note_card(s20, "Dual reader heads and deep learning models eliminate the historical homopolymer bottleneck", 0.6, 6.0, 12.1, 0.65, font_size=13, fill_color=PALE_BLUE, border_color=BLUE, text_color=DARK_BLUE)
    update_notes(s20, "Say: Nanopore accuracy has transformed over recent chemistries. R10.4.1 pores feature two reader heads spaced vertically along the pore lumen, reading each base twice and breaking homopolymer ambiguity. Together with Dorado's deep neural network models, modal simplex accuracy exceeds 99% (Q20+), providing high-confidence amplicon identification. [Time: 3.5 min]")
    print("Slide 20 updated to R9 vs R10 chemistry.")

    # 8. Slide 21 (Transform from Case Study II to Option B: Adapting Workflows to Environmental DNA)
    s21 = prs.slides[20]
    shapes_to_remove = []
    for shape in s21.shapes:
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Case study II" in txt or txt.strip() == "21":
                continue
        shapes_to_remove.append(shape)
    for shp in shapes_to_remove:
        remove_shape(shp)
    
    # Update title
    for shape in s21.shapes:
        if shape.has_text_frame and "Case study II" in shape.text_frame.text:
            shape.text_frame.text = "Adapting Workflows for Environmental DNA (eDNA)"
            p = shape.text_frame.paragraphs[0]
            p.font.name = "Arial"
            p.font.size = Pt(28)
            p.font.bold = True
            p.font.color.rgb = DARK_BLUE

    # Add bullets on the left
    s21_bullets = [
        "Fish eDNA metabarcoding targets short fragments (~163–185 bp MiFish 12S)",
        "Bead clean-up ratio: 0.4× beads discard <1 kb DNA; must derive ratio from amplicon size (≥1.0×)",
        "Flow cell loading target: 100 fmol for <1 kb amplicons (vs. 35–50 fmol for 16S)",
        "Bioinformatics filters: default wf-16s length window (800–2,000 bp) drops short eDNA",
        "Reference database: swap bacterial 16S for curated fish mitochondrial 12S databases",
        "Direct bridge to Pak Hilman's session: Fish eDNA in Anthropogenic Ecosystems"
    ]
    add_bullet_list(s21, s21_bullets, 0.6, 1.45, 5.2, 4.4, font_size=13.5)

    # Add fish 12S diagram on the right
    if os.path.exists("assets/common-amplicon-markers/fish-12S-generated.png"):
        s21.shapes.add_picture("assets/common-amplicon-markers/fish-12S-generated.png", Inches(6.0), Inches(1.45), width=Inches(6.7), height=Inches(4.3))
    
    add_note_card(s21, "A single protocol does not fit all targets: chemistry and bioinformatic filters must match fragment biology", 0.6, 6.0, 12.1, 0.65, font_size=13, fill_color=PALE_AMBER, border_color=AMBER, text_color=INK)
    update_notes(s21, "Say: When adapting this workflow to environmental DNA—such as fish eDNA metabarcoding in Pak Hilman's session—we must adjust several key parameters. A 0.4× bead cleanup completely discards short ~170 bp 12S amplicons, and wf-16s default length filters (800–2,000 bp) would reject them. Method selection must be driven by the biological sample. [Time: 3.5 min]")
    print("Slide 21 updated to eDNA workflow adaptation.")

    prs.save(PPTX_PATH)
    print(f"Successfully saved updated {PPTX_PATH}")

if __name__ == '__main__':
    main()
