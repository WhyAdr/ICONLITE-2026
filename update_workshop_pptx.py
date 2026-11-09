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
LIGHT_GRAY = RGBColor(0x8C, 0x9B, 0xAA)
PALE_BLUE = RGBColor(0xEA, 0xF3, 0xFA)
PALE_AMBER = RGBColor(0xFF, 0xF6, 0xD9)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

def add_bullet_list(slide, items, x, y, w, h, font_size=14, space_after=8):
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
        p.space_after = Pt(space_after)
    return txBox

def add_card(slide, title, body, x, y, w, h, fill_color=PALE_BLUE, border_color=BLUE, title_color=DARK_BLUE, body_color=INK):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.color.rgb = border_color
    shape.line.width = Pt(1.5)
    tf = shape.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = "Arial"
    p0.font.size = Pt(12.5)
    p0.font.bold = True
    p0.font.color.rgb = title_color
    p0.space_after = Pt(4)
    
    p1 = tf.add_paragraph()
    p1.text = body
    p1.font.name = "Arial"
    p1.font.size = Pt(11.0)
    p1.font.color.rgb = body_color
    return shape

def add_note_card(slide, text, x, y, w, h, font_size=12, bold=True, fill_color=PALE_AMBER, border_color=AMBER, text_color=INK):
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

def remove_footers_and_numbers(prs):
    """Remove repeating footer and slide number shapes from masters, layouts, and slides."""
    # 1. Slide Masters
    for m in prs.slide_masters:
        for s in list(m.shapes):
            if "Slide Number" in s.name or "Footer" in s.name:
                remove_shape(s)
            elif s.has_text_frame and ("ICONLITE" in s.text_frame.text or s.text_frame.text.strip().isdigit()):
                remove_shape(s)
        # Layouts
        for l in m.slide_layouts:
            for s in list(l.shapes):
                if "Slide Number" in s.name or "Footer" in s.name:
                    remove_shape(s)
                elif s.has_text_frame and ("ICONLITE" in s.text_frame.text or s.text_frame.text.strip().isdigit()):
                    remove_shape(s)

    # 2. Individual Slides
    for s in prs.slides:
        for shape in list(s.shapes):
            if "Slide Number" in shape.name or "Footer" in shape.name:
                remove_shape(shape)
            elif shape.has_text_frame:
                txt = shape.text_frame.text.strip()
                # If it's a standalone slide number or repeating event header at bottom (top > 6.0 inches)
                if txt.isdigit() and shape.top.inches > 6.0:
                    remove_shape(shape)
                elif "ICONLITE 2026 · From Sample to Species" in txt and shape.top.inches > 6.0:
                    remove_shape(shape)

def main():
    prs = pptx.Presentation(PPTX_PATH)
    print(f"Loaded {PPTX_PATH} with {len(prs.slides)} slides.")

    # 0. Global Cleanup: Remove footers and slide numbers across all slides
    remove_footers_and_numbers(prs)
    print("Removed recurring footers and slide numbering across all slides.")

    # Ensure 25 slides exist
    if len(prs.slides) == 23:
        layout = prs.slide_layouts[1]
        s_new1 = prs.slides.add_slide(layout)
        sldIdLst = prs.slides._sldIdLst
        elem = list(sldIdLst)[-1]
        sldIdLst.remove(elem)
        sldIdLst.insert(7, elem)
        
        s_new2 = prs.slides.add_slide(layout)
        sldIdLst = prs.slides._sldIdLst
        elem = list(sldIdLst)[-1]
        sldIdLst.remove(elem)
        sldIdLst.insert(20, elem)

    # 1. Slide 1 (Cover)
    s1 = prs.slides[0]
    for shape in s1.shapes:
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "[Presenter name]" in txt:
                shape.text_frame.text = "ICONLITE Workshop 2026 · Technical Workshop Session"
                for p in shape.text_frame.paragraphs:
                    p.font.name = "Arial"
                    p.font.size = Pt(14)
                    p.font.color.rgb = PALE_BLUE
            elif "Taxonomic report" in txt:
                shape.text_frame.text = "Taxonomic profile\n(genus & species)"
                for p in shape.text_frame.paragraphs:
                    p.font.name = "Arial"
                    p.font.size = Pt(11)
                    p.font.color.rgb = INK
    update_notes(s1, 
        "Welcome everyone to this technical workshop session at ICONLITE 2026. Today, we trace one biological sample "
        "all the way from extraction through long-read Oxford Nanopore sequencing to a high-resolution taxonomic profile. "
        "Throughout the next 50 minutes, we will ground every experimental choice—from primer design and enzymatic ligation "
        "to neural basecalling—in three fundamental biological questions: First, who is there? Second, what might they be doing? "
        "And third, why is it necessary to know them? We have allocated time at the end for an open discussion and a seamless handoff "
        "to Pak Hilman's session on fish eDNA metabarcoding. Let's begin. [Time: 1.5 min]"
    )

    # 2. Slide 2 (Why Amplicon Sequencing)
    s2 = prs.slides[1]
    update_notes(s2,
        "Let's start with a foundational problem in microbial ecology: if we plate a natural water or soil sample on agar, "
        "fewer than 1% of the microbes present will ever form visible colonies. Traditional culture severely distorts our view of microbial life. "
        "Targeted amplicon sequencing bypasses culturing entirely by targeting conserved, taxonomically informative marker genes. "
        "[Cue: Ask audience] Before we jump into chemistry, let me ask: How many of you currently use 16S or ITS sequencing in your research? "
        "Notice that while short-read platforms dominate routine profiling, long-read sequencing allows us to sequence entire operons intact. "
        "This gives us the phylogenetic depth needed to distinguish closely related strains and pathogenic species. [Time: 2 min]"
    )

    # 3. Slide 3 (Barcoding vs Metabarcoding vs Metagenomics)
    s3 = prs.slides[2]
    update_notes(s3,
        "It is crucial to clarify terminology right at the outset. DNA barcoding refers to identifying an individual specimen "
        "from pure tissue, such as identifying a single insect using a COI marker. DNA metabarcoding, our workshop focus, "
        "amplifies a marker from a complex environmental mixture—containing hundreds of species—to generate a community census. "
        "Shotgun metagenomics, in contrast, skips PCR entirely and shears all environmental DNA to sequence total genomes, including functional genes. "
        "While shotgun sequencing provides metabolic gene capacity, amplicon metabarcoding remains vastly more accessible, cost-effective, "
        "and sensitive for deep taxonomic surveillance in low-biomass environments. [Time: 2 min]"
    )

    # 4. Slide 4 (Choosing Markers)
    s4 = prs.slides[3]
    for shape in s4.shapes:
        if shape.has_table:
            for row in shape.table.rows:
                cells = [c.text.strip() for c in row.cells]
                if len(cells) > 0 and "12S rRNA" in cells[0]:
                    row.cells[2].text = "163–185 bp (MiFish; Miya et al. 2015)"
                    p = row.cells[2].text_frame.paragraphs[0]
                    p.font.name = "Arial"
                    p.font.size = Pt(10)
    update_notes(s4,
        "No single molecular marker fits every biological kingdom. The choice of marker dictates both the taxonomic boundary "
        "and phylogenetic resolution of your study. For bacteria and archaea, the 16S rRNA gene is the gold standard. For fungi, "
        "we target the internal transcribed spacer, ITS. For metazoans, mitochondrial COI is standard. "
        "Critically, for aquatic vertebrate and fish environmental DNA, we rely on the mitochondrial 12S rRNA gene—specifically the "
        "163 to 185 base pair MiFish fragment established by Miya et al. in 2015. Always ensure your marker selection matches both "
        "the degradation state of your DNA and the availability of curated reference databases. [Time: 2 min]"
    )

    # 5. Slide 5 (Short-Read vs Long-Read)
    s5 = prs.slides[4]
    update_notes(s5,
        "Here we see why read length matters so profoundly. Traditional Illumina amplicon workflows sequence short hypervariable windows, "
        "typically the V3–V4 region (~460 bp) or V4 alone (~250 bp). While short reads are cheap and accurate, multiple distinct bacterial species "
        "often share identical sequences across a single variable loop, limiting taxonomic assignment to the genus or family level. "
        "With Oxford Nanopore long reads, we can sequence the entire 1,500 bp 16S gene—spanning all nine hypervariable regions V1 through V9—in a "
        "single continuous read. This multi-region coverage provides the resolving power needed for species-level differentiation. [Time: 2 min]"
    )

    # 6. Slide 6 (Nanopore Biophysical Mechanism)
    s6 = prs.slides[5]
    for shape in list(s6.shapes):
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Schematic only" in txt:
                remove_shape(shape)
    # Add caption credit
    add_note_card(s6, "Nanopore biosensing principle. Adapted from Wang et al., 2021 (Nat. Biotechnol.)", 0.6, 6.2, 12.1, 0.45, font_size=10.5, bold=False, fill_color=WHITE, border_color=LIGHT_GRAY, text_color=GRAY)
    update_notes(s6,
        "Let's look at the biophysics inside a flow cell. A biological protein nanopore sits embedded within an electrically resistant synthetic polymer membrane, "
        "separating two electrolyte chambers. Under an applied voltage, a steady ionic current of potassium and chloride ions flows through the pore barrel. "
        "A motor protein derived from a helicase unzips double-stranded DNA and steps the single strand through the pore constriction at roughly 400 bases per second. "
        "As bases occupy the constriction, they partially block the ion flow. Because different nucleotide combinations have unique shapes and charges, "
        "the current shifts characteristically. An ASIC sensor chip samples this current thousands of times per second, recording a continuous electrical 'squiggle'. [Time: 2.5 min]"
    )

    # 7. Slide 7 (ONT Platforms)
    s7 = prs.slides[6]
    update_notes(s7,
        "Oxford Nanopore scales this identical sensing chemistry across multiple hardware form factors. The portable MinION features 512 channels, "
        "with a manufacturer warranty guaranteeing at least 800 active sequencing pores on delivery—ideal for field deployments and small sample pools. "
        "The benchtop GridION runs up to five MinION flow cells concurrently. At the enterprise scale, the PromethION houses high-density flow cells "
        "containing 3,000 sensor channels addressing up to 12,000 physical pores, with a factory warranty of at least 5,000 active pores upon receipt. "
        "For large multiplexed amplicon cohorts, a single PromethION flow cell generates millions of reads, reducing per-sample sequencing costs significantly. [Time: 2 min]"
    )

    # 8. Slide 8 (Selecting Your ONT Library Kit: Native vs. Dedicated 16S)
    s8 = prs.slides[7]
    for shp in list(s8.shapes):
        if not (shp.is_placeholder and shp.placeholder_format.type == 1):
            remove_shape(shp)
    for shp in s8.shapes:
        if shp.is_placeholder and shp.placeholder_format.type == 1:
            shp.text_frame.text = "Selecting Your ONT Library Kit: Native vs. Dedicated 16S"
            for p in shp.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(24)
                p.font.bold = True
                p.font.color.rgb = DARK_BLUE
    add_card(s8, "SQK-NBD114.24 / .96", "Native Barcoding Kit (Our Workshop Choice)\n• Chemistry: Enzymatic ligation (dA-tailing + blunt/TA barcode ligation)\n• Amplicons: Universal for ANY marker (16S, 18S, ITS, COI, 12S, custom)\n• PCR Strategy: User performs custom PCR; zero PCR in library prep\n• Key Advantage: Preserves native amplicon stoichiometry without kit primer bias\n• Scope: Foundation for eDNA, fungi, vertebrates, and multi-marker projects", 0.6, 1.4, 3.85, 5.0, fill_color=PALE_BLUE, border_color=BLUE, title_color=DARK_BLUE)
    add_card(s8, "SQK-MAB114.24", "16S Barcoding Kit 24 V14 (Dedicated 16S)\n• Chemistry: PCR-based barcoding with rapid adapter attachment\n• Amplicons: Bacterial 16S rRNA ONLY (pre-mixed 27F / 1492R primers)\n• PCR Strategy: 4-primer or two-step PCR directly adds barcode tags\n• Turnaround: Fastest hands-on protocol (~2.0–2.5 hours total)\n• Major Limitation: Strictly locked to bacterial 16S; cannot barcode other loci", 4.75, 1.4, 3.85, 5.0, fill_color=WHITE, border_color=TEAL, title_color=TEAL)
    add_card(s8, "Kit Lineage & EPI2ME [LAB]", "Evolutionary History & Compatibility\n• Lineage: SQK-16S024 (legacy) → SQK-16S114.24 → SQK-MAB114.24\n• wf-16s Support: While docs list MAB/16S as defaults, wf-16s processes demultiplexed FASTQs from ANY kit [LAB]\n• Pedagogical Role: NBD teaches universal ligation chemistry that generalizes\n• Capacity: 24-plex standard; expandable to 96-plex with SQK-NBD114.96\n• Recommendation: Master NBD ligation first for cross-domain flexibility", 8.9, 1.4, 3.85, 5.0, fill_color=PALE_AMBER, border_color=AMBER, title_color=DARK_BLUE)
    update_notes(s8,
        "Before diving into our hands-on protocol, we must address library kit selection. Oxford Nanopore provides two distinct barcoding routes: dedicated 16S kits and native barcoding kits. Dedicated kits—evolving from legacy SQK-16S024 to SQK-16S114.24 and currently SQK-MAB114.24—use PCR-based barcoding with bundled 27F/1492R primers. They offer rapid 2-hour turnaround for routine bacterial monitoring, but cannot barcode fungal ITS, eukaryotic 18S, or fish 12S amplicons. In this workshop, we specifically teach Native Barcoding Kit 24 V14 (SQK-NBD114.24). Native barcoding uses enzymatic ligation without PCR, accommodating any user-defined amplicon. Crucially, while EPI2ME wf-16s lists MAB as its default protocol, it accepts demultiplexed FASTQs from any kit, making NBD the ideal foundation for multi-marker research. [Time: 2 min]"
    )

    # 9. Slide 9 (Laboratory Workflow Big Picture)
    s9 = prs.slides[8]
    update_notes(s8,
        "Now we transition into the wet-lab workflow. Our laboratory strategy uses ONT's Native Barcoding Kit 24 V14 (SQK-NBD114.24) on a PromethION. "
        "Notice a key terminology distinction: ONT calls this library preparation 'PCR-free' because once amplicons enter the workflow, barcodes and adapters "
        "are attached purely through enzymatic end-repair and cohesive TA-ligation—no subsequent PCR amplification cycles are performed. "
        "However, our starting amplicons were initially generated via PCR. To protect data integrity, every batch must include three mandatory controls: "
        "an extraction blank to detect kit contamination, a PCR no-template control (NTC) for aerosol carryover, and a positive mock community. [Time: 2.5 min]"
    )

    # 10. Slide 10 (H1: PCR Amplicon Evaluation)
    s10 = prs.slides[9]
    update_notes(s9,
        "In Section 9.1, our first operational rule is that enzymatic ligation kinetics depend strictly on the molar concentration of DNA termini (femtomoles), "
        "not on mass in nanograms. Equal mass does not mean equal molecules! One hundred nanograms of a short 500 bp amplicon contains three times as many "
        "ligatable ends as 100 ng of a 1,500 bp amplicon. On the gel image here, we verify a clean, single band at 1.5 kb with zero primer-dimers. "
        "Using our mass-to-molarity formula, delivering 200 fmol of full-length 16S requires exactly 198 ng of amplicon DNA in an 11.5 µL volume. "
        "Always quantify with Qubit fluorometry—never NanoDrop, which overestimates DNA in the presence of free dNTPs. [Time: 2.5 min]"
    )

    # 11. Slide 11 (H2: End-Prep)
    s11 = prs.slides[10]
    update_notes(s10,
        "In step H2, amplicons undergo end-preparation using NEBNext Ultra II reagents. Amplicons generated by proofreading polymerases possess blunt or ragged ends. "
        "The end-prep master mix repairs these ends, phosphorylates the 5-prime termini, and appends a single 3-prime deoxyadenosine (dA) overhang. "
        "The thermal cycler program runs at 20 °C for 5 minutes for repair, followed by 65 °C for 5 minutes to heat-inactivate the enzymes and complete dA-tailing. "
        "Following reaction cleanup with 1.0× AMPure XP magnetic beads and two fresh 80% ethanol washes, we elute the purified dA-tailed amplicons in 10 µL of nuclease-free water. [Time: 2 min]"
    )

    # 12. Slide 12 (H3: Native Barcode Ligation)
    s12 = prs.slides[11]
    update_notes(s11,
        "In step H3, we multiplex our samples using Native Barcoding Kit 24. Each sample receives a unique double-stranded barcode (NB01 through NB24) "
        "for cohesive TA ligation with dA-tailed amplicons. The reaction incubates with Blunt/TA ligase for 20 minutes at room temperature. "
        "Immediately following ligation, we add 4 µL of EDTA (blue cap) to quench ligase activity before combining samples. "
        "Crucial warning: Once samples are pooled into a single tube, mislabeled samples cannot be recovered! "
        "We pool 24 µL per sample—yielding 576 µL for a 24-plex run—and purify with a 0.4× AMPure XP bead cleanup, washing twice with Short Fragment Buffer (SFB). [Time: 2.5 min]"
    )

    # 13. Slide 13 (H4: Sequencing Adapter Ligation)
    s13 = prs.slides[12]
    update_notes(s12,
        "In step H4, we attach the Native Adapter (NA) to our pooled barcoded amplicons. Do not confuse barcodes with adapters! "
        "Barcodes identify sample biological origin; the Native Adapter carries the vital motor protein that docks into the nanopore and unwinds DNA. "
        "This ligation runs for 20 minutes with Quick T4 Ligase. In the final magnetic bead cleanup, we wash twice with Short Fragment Buffer (SFB). "
        "Absolute warning: Never use ethanol during post-adapter wash steps! Ethanol denatures the sequencing motor protein, causing active pore occupancy "
        "to drop to near zero when sequencing begins. The final library is eluted in Elution Buffer (EB). [Time: 2.5 min]"
    )

    # 14. Slide 14 (H5: Flow Cell Priming and Loading)
    s14 = prs.slides[13]
    update_notes(s13,
        "In step H5, we prime and load the PromethION flow cell. The priming solution combines 1,170 µL Flow Cell Flush (FCF) with 30 µL Flow Cell Tether (FCT). "
        "The tether consists of lipid-conjugated oligonucleotides that concentrate library molecules directly at the synthetic membrane surface near the pores. "
        "When opening the inlet port, gently draw back 20 to 30 µL to clear any trapped air bubbles—air bubbles permanently destroy the active membrane! "
        "We introduce 500 µL of priming mix, wait 5 minutes, prime with another 500 µL, and load our 200 µL library mix (100 µL SB, 68 µL LIB, 32 µL library). "
        "Allow the loaded flow cell to rest for at least 10 minutes before starting the run to maximize library availability across pores. [Time: 2.5 min]"
    )

    # 15. Slide 15 (H6: MinKNOW Run Setup)
    s15 = prs.slides[14]
    # Remove old placeholder shapes and overlapping chips
    for shape in list(s14.shapes):
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Insert real MinKNOW" in txt or any(k in txt for k in ['Kit: SQK-NBD114.24', 'Position + sample ID', 'Basecalling + demux', 'Output: POD5 + FASTQ']):
                remove_shape(shape)
    # Embed real screenshot
    screenshot_14 = "assets/software-screenshots/MinKNOW-sequencing-run-configuration1.jpeg"
    if os.path.exists(screenshot_14):
        s14.shapes.add_picture(screenshot_14, Inches(5.3), Inches(1.4), width=Inches(7.4), height=Inches(4.4))
    update_notes(s14,
        "Here on Slide 14, we see the live MinKNOW run configuration interface. MinKNOW governs instrument telemetry, voltage feedback, and real-time basecalling. "
        "We select our flow cell position, verify chemistry FLO-PRO114M, and select kit SQK-NBD114.24. "
        "Selecting Native Barcoding 24 enables automated real-time demultiplexing, barcode trimming, and mid-read filtering. "
        "Under basecalling settings, we select the Super-Accuracy (SUP) or High-Accuracy (HAC) model depending on GPU compute capacity. "
        "We set outputs to generate both raw POD5 signal files—essential for long-term re-basecalling—and demultiplexed FASTQ files for immediate analysis. [Time: 2 min]"
    )

    # 16. Slide 16 (H7: EPI2ME wf-16s)
    s16 = prs.slides[15]
    # Remove old placeholder shapes
    for shape in list(s15.shapes):
        if shape.has_text_frame and "Insert real wf-16s" in shape.text_frame.text:
            remove_shape(shape)
    # Embed real screenshot
    screenshot_15 = "assets/software-screenshots/wf16s-run-start-page.jpeg"
    if os.path.exists(screenshot_15):
        s15.shapes.add_picture(screenshot_15, Inches(0.6), Inches(4.2), width=Inches(12.1), height=Inches(2.5))
    update_notes(s15,
        "Once FASTQ reads are generated, we feed them into EPI2ME wf-16s, ONT's official Nextflow workflow. "
        "As displayed on this interface screenshot, wf-16s executes end-to-end QC, length filtering, alignment, and taxonomic assignment. "
        "Default parameters assume full-length 16S amplicons, setting a length filter of 800 to 2,000 bp and aligning via minimap2 against the NCBI 16S/18S database. "
        "Crucial caveat: If analyzing fungal ITS or fish 12S eDNA, running wf-16s with default settings will filter out your reads or leave them unclassified! "
        "You must adjust min_len and supply a dedicated reference database. The pipeline outputs an interactive HTML report and taxon abundance matrices. [Time: 2.5 min]"
    )

    # 17. Slide 17 (H8: Five Critical Decisions)
    s17 = prs.slides[16]
    # Remove old sparse cards and replace with rich concrete questions
    for shape in list(s16.shapes):
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if any(k in txt for k in ["Q1", "Q2", "Q3", "Q4", "Q5", "Interactive Checkpoint", "Answer by hands"]):
                remove_shape(shape)
    
    # Add 5 rich scenario cards (12.5 pt bold title, 11 pt body text)
    q_data = [
        ("Q1 · Stoichiometry", "1,500 bp amplicon at 30 ng/µL.\nMass & volume for 200 fmol?\n\n→ A: 198 ng (6.6 µL)\n→ B: 66 ng (2.2 µL)\n→ C: 300 ng (10.0 µL)", 0.6),
        ("Q2 · Controls [LAB]", "6 samples + blank + NTC [LAB].\nTotal barcodes to allocate?\n\n→ A: 6 barcodes; pool at start\n→ B: 8 barcodes; pool post-EDTA\n→ C: 8 barcodes; pool pre-ligation", 3.05),
        ("Q3 · Size Selection", "Purifying a 1.5 kb amplicon library.\nWhich wash buffer is required?\n\n→ A: SFB (mandatory for <3 kb)\n→ B: LFB (enriches ≥3 kb)\n→ C: 80% Ethanol", 5.5),
        ("Q4 · Flow Cell Loading", "PromethION library loading mix composition & rest time?\n\n→ A: 100 µL SB + 68 LIB + 32 DNA\n→ B: 200 µL pure DNA library\n→ Rest ≥10 min before run", 7.95),
        ("Q5 · Lab Diagnosis", "Student accidentally washed beads with 80% EtOH after adapter ligation.\nOutcome?\n\n→ A: Yield improves 20%\n→ B: Pore occupancy ~0%\n→ C: No effect on run", 10.4)
    ]
    for title, body, x in q_data:
        add_card(s16, title, body, x, 1.5, 2.3, 4.6, fill_color=WHITE, border_color=BLUE, title_color=DARK_BLUE, body_color=INK)
    # Bottom banner strictly without printing answers! Answers remain in speaker notes & handbook only!
    add_note_card(s16, "Interactive Checkpoint: Quick 3-minute audience poll across critical workflow decisions (Discuss options, then reveal answers)", 0.6, 6.25, 12.1, 0.45, font_size=11.5, bold=True, fill_color=PALE_AMBER, border_color=AMBER, text_color=INK)
    update_notes(s16,
        "Let's test our understanding with a quick 3-minute interactive checkpoint across five critical workflow decisions. "
        "[Ask audience]: For Q1, calculating mass for 200 fmol of 1,500 bp DNA: who says A, 198 ng? Correct! 200 × 1500 × 660 / 10^6 = 198 ng. "
        "For Q2, always allocate barcodes to your extraction blank and NTC [LAB], pooling strictly after quenching with EDTA (Answer B). "
        "For Q3, SFB is mandatory; LFB selectively enriches fragments over 3 kb and depletes amplicons (Answer A). "
        "For Q4, PromethION uses 100 µL SB, 68 µL LIB, and 32 µL library, resting for ≥10 minutes before starting run (Answer A). "
        "And for Q5: washing with ethanol after adapter ligation denatures the motor protein, causing pore occupancy to collapse to near 0% (Answer B). "
        "Every single step has a direct biophysical consequence. [Time: 3 min]"
    )

    # 18. Slide 18 (Signal to FASTQ)
    s18 = prs.slides[17]
    for shape in list(s17.shapes):
        if shape.has_text_frame and "Classic event-segmented" in shape.text_frame.text:
            remove_shape(shape)
    # Add caption clarifying event-calling vs direct raw signal decoding
    add_note_card(s17, "Classic event-segmented view; modern Dorado neural models decode raw electrical current directly without prior event segmentation (Wick et al., 2019).", 0.6, 6.6, 12.1, 0.35, font_size=9.5, bold=False, fill_color=WHITE, border_color=LIGHT_GRAY, text_color=GRAY)
    update_notes(s17,
        "Now we shift to the dry-lab: how continuous ionic current measurements become digital nucleotide sequences. "
        "Historically, nanopores used event segmentation before basecalling; modern Dorado neural networks process raw POD5 current traces directly. "
        "Convolutional layers extract local signal features, while Transformer layers model long-range temporal dependencies. "
        "The decoder assigns individual bases along with Phred quality scores, where Q20 represents 99% accuracy. "
        "Always remember: Basecalling produces nucleotide sequences, not biological identifications! A high Q-score means the machine accurately read the DNA; "
        "whether that sequence represents a living bacterium, dead relic DNA, or an extraction contaminant depends entirely on downstream analysis. [Time: 2 min]"
    )

    # 19. Slide 19 (Read QC & Taxonomic Classification)
    s19 = prs.slides[18]
    update_notes(s18,
        "Once reads pass quality filtering, how do we assign taxonomy? In wf-16s, you choose between two classification philosophies: "
        "minimap2 performs full-length pairwise alignment against reference sequences. It requires strict identity (≥95%) and coverage (≥90%), "
        "providing exceptional species-level resolution but requiring more compute. Kraken2, in contrast, breaks reads into 35-mers and matches them "
        "against lowest common ancestor trees, re-estimated by Bracken. Kraken2 is lightning fast, but sensitive to reference database gaps. "
        "Neither tool is universally superior; choose alignment for high-confidence species calls and k-mer matching for rapid diagnostic screening. [Time: 2.5 min]"
    )

    # 20. Slide 20 (Critical Community Interpretation)
    s20 = prs.slides[19]
    update_notes(s19,
        "When inspecting community composition bar plots, we must avoid the central trap of microbiome research: "
        "[Cue: Ask audience] If taxon A shows twice as many sequence reads as taxon B, did the sample contain twice as many bacterial cells? "
        "The answer is an emphatic NO. First, bacterial genomes vary widely in 16S ribosomal RNA gene copy numbers—from 1 copy in many oligotrophic taxa "
        "up to 21 copies in spore-forming bacilli, as documented in the rrnDB database (v5.x, reporting 1–21 copies; Stoddard et al., 2015). A single Bacillus cell produces 10 to 15 times more PCR amplicons than a single Pseudomonas cell! "
        "Second, differential lysis efficiencies and PCR primer biases distort ratios. Third, amplicon data are compositional percentages summing to 100%. "
        "Always treat read counts as relative sequence shares, never absolute cell abundances. [Time: 2.5 min]"
    )

    # 21. Slide 21 (From Taxonomy to Function: Predictive Metagenomics with PICRUSt2 & FUNGuild)
    s21 = prs.slides[20]
    for shp in list(s21.shapes):
        if not (shp.is_placeholder and shp.placeholder_format.type == 1):
            remove_shape(shp)
    for shp in s21.shapes:
        if shp.is_placeholder and shp.placeholder_format.type == 1:
            shp.text_frame.text = "From Taxonomy to Function: Predictive Metagenomics"
            for p in shp.text_frame.paragraphs:
                p.font.name = "Arial"
                p.font.size = Pt(24)
                p.font.bold = True
                p.font.color.rgb = DARK_BLUE
    add_card(s21, "Bacterial Metabolic Potential: PICRUSt2", "Phylogenetic Hidden-State Reconstruction\n• Phylogenetic Placement: Aligns full-length 16S reads into ~20,000 reference genomes via EPA-ng / GAPPA\n• Hidden State Prediction: Castor evolutionary models infer unobserved KO and MetaCyc gene families\n• Copy-Number Normalization: Divides observed counts by predicted 16S operon counts (1–21 copies)\n• Pathway Inference: Maps predicted gene families into structured MetaCyc pathways via MinPath", 0.6, 1.4, 5.9, 3.1, fill_color=PALE_BLUE, border_color=BLUE, title_color=DARK_BLUE)
    add_card(s21, "Fungal Ecological Guilds: FUNGuild", "Trophic Strategy & Ecological Trait Mapping\n• Taxonomic Guild Mapping: Links fungal ITS/28S taxa to curated ecological life-history traits\n• Trophic Modes: Parses taxa into Pathotroph (host damage), Saprotroph (decay), or Symbiotroph (mutualist)\n• Confidence Tiers: Qualifies assignments as Highly Probable, Probable, or Possible\n• Ecological Role: Translates raw fungal taxonomic inventories into functional niche dynamics", 6.8, 1.4, 5.9, 3.1, fill_color=WHITE, border_color=TEAL, title_color=TEAL)
    add_card(s21, "Critical Scientific Realism: What Predictions Can & Cannot Claim [LAB]", "Methodological Boundaries & Best Practices\n• Genomic Potential ≠ Expressed Activity: Predicts DNA coding capacity, NOT active transcription (mRNA) or enzyme activity\n• Nearest Sequenced Taxon Index (NSTI): Accuracy degrades severely in uncharacterized biomes (soil, marine; NSTI > 0.15)\n• Hypothesis Generator: Copy-number normalization is model-dependent; validate candidate pathways via shotgun metagenomics or RNA-seq", 0.6, 4.65, 12.1, 1.85, fill_color=PALE_AMBER, border_color=AMBER, title_color=DARK_BLUE)
    update_notes(s21,
        "On Slide 21, we bridge from 'Who is there?' to 'What are they doing?' using predictive metagenomics. For bacteria, PICRUSt2 places full-length 16S reads into a reference phylogenetic tree using EPA-ng, infers unobserved gene families via ancestral state reconstruction with castor, normalizes for 16S copy number variation, and predicts MetaCyc metabolic pathways. For fungi, FUNGuild classifies taxa into trophic guilds—pathotrophs, saprotrophs, and symbiotrophs. However, critical realism is essential: genomic capacity does not equate to active gene expression or enzymatic flux. Furthermore, accuracy drops sharply in non-human biomes with high Nearest Sequenced Taxon Index (NSTI > 0.15). Treat predictive profiles as hypothesis generators that must be validated with direct shotgun metagenomics or metatranscriptomics. [Time: 2 min]"
    )

    # 22. Slide 22 (R9 vs R10 Pore Architecture & Basecalling)
    s22 = prs.slides[21]
    for shape in list(s20.shapes):
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Pore Architecture" in txt:
                continue
        remove_shape(shape)
    
    t_shape = None
    for shape in s20.shapes:
        if shape.has_text_frame and "Pore Architecture" in shape.text_frame.text:
            t_shape = shape
            break
    if not t_shape:
        t_shape = s20.shapes.add_textbox(Inches(0.6), Inches(0.35), Inches(12.1), Inches(0.9))
        t_shape.text_frame.text = "Pore Architecture & Accuracy: R9.4.1 vs. R10.4.1"
    p = t_shape.text_frame.paragraphs[0]
    p.font.name = "Arial"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    # 3 crisp bullets on the left (14.5 pt font), with softened homopolymer claim and dropped ~1.4 nm spacing
    s20_bullets = [
        "Pore Geometry: R9.4.1 single reader head (CsgG, ~4–5 bp) evolved into R10.4.1 dual reader heads spaced vertically along the pore lumen.",
        "Homopolymer Resolution: Dual consecutive reading breaks current ambiguity, significantly improving homopolymer resolution up to ~9–10 bp.",
        "Accuracy Milestone: Kit 14 chemistry + Dorado Super-Accuracy (SUP) neural basecalling delivers modal simplex raw accuracy of Q20+ (~99.2%) and duplex reads reaching ~Q30 (>99.7%)."
    ]
    add_bullet_list(s20, s20_bullets, 0.6, 1.4, 5.0, 4.4, font_size=14.5, space_after=14)

    # Diagrams on the right
    if os.path.exists("assets/ONTR9vsR10-nanopore-diagram.png"):
        s20.shapes.add_picture("assets/ONTR9vsR10-nanopore-diagram.png", Inches(5.8), Inches(1.4), width=Inches(3.3), height=Inches(4.4))
    if os.path.exists("assets/ONT-basecalling-neural-network-diagram.png"):
        s20.shapes.add_picture("assets/ONT-basecalling-neural-network-diagram.png", Inches(9.3), Inches(1.4), width=Inches(3.4), height=Inches(4.4))
    
    add_note_card(s20, "Dual reader heads and deep learning models eliminate historical homopolymer and raw accuracy bottlenecks", 0.6, 6.15, 12.1, 0.55, font_size=12, fill_color=PALE_BLUE, border_color=BLUE, text_color=DARK_BLUE)
    update_notes(s20,
        "Here on Slide 20, we explore how Oxford Nanopore achieved its dramatic accuracy leap from ~90% in early chemistries to over 99% (Q20+) today. "
        "The breakthrough centers on pore engineering: R9.4.1 pores had a single constriction where 4 to 5 bases sat simultaneously, causing current plateaus "
        "and indel errors in homopolymers. In contrast, R10.4.1 pores feature dual reader heads spaced vertically inside the barrel. Each nucleotide is read twice "
        "at shifted intervals, breaking homopolymer degeneracy and significantly improving homopolymer resolution up to ~9–10 base pairs. Combined with Dorado's PyTorch convolutional and Transformer deep learning models, "
        "modal simplex raw read accuracy reaches Q20+ (~99.2%), with duplex reads reaching ~Q30 (>99.7%). [Time: 2.5 min]"
    )

    # 23. Slide 23 (Adapting Workflows for eDNA)
    s23 = prs.slides[22]
    for shape in list(s21.shapes):
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Adapting Workflows" in txt:
                continue
        remove_shape(shape)
    
    t_shape21 = None
    for shape in s21.shapes:
        if shape.has_text_frame and "Adapting Workflows" in shape.text_frame.text:
            t_shape21 = shape
            break
    if not t_shape21:
        t_shape21 = s21.shapes.add_textbox(Inches(0.6), Inches(0.35), Inches(12.1), Inches(0.9))
        t_shape21.text_frame.text = "Adapting Workflows for Environmental DNA (eDNA)"
    p = t_shape21.text_frame.paragraphs[0]
    p.font.name = "Arial"
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = DARK_BLUE

    s21_bullets = [
        "Fragment Biology: Aquatic environmental DNA is naturally degraded; fish metabarcoding targets short ~163–185 bp mitochondrial 12S rRNA fragments (MiFish).",
        "Protocol Bottlenecks [ADAPT]: Standard 0.4× SPRI bead cleanups (pooling & post-adapter) select against short DNA; recovering ~170 bp amplicons requires empirically titrated higher bead ratios (~1.5×–1.8×) and 100 fmol loading.",
        "Bioinformatics & Session Bridge: Default wf-16s drops reads <800 bp and lacks fish 12S in its database. Pak Hilman's Illumina short-read workflow natively avoids these hurdles, making it ideal for fragmented eDNA!"
    ]
    add_bullet_list(s21, s21_bullets, 0.6, 1.4, 5.2, 4.4, font_size=14.5, space_after=14)

    if os.path.exists("assets/common-amplicon-markers/fish-12S-generated.png"):
        s21.shapes.add_picture("assets/common-amplicon-markers/fish-12S-generated.png", Inches(6.0), Inches(1.4), width=Inches(6.7), height=Inches(4.4))
    
    add_note_card(s21, "Direct Bridge to Pak Hilman's Session: Fish eDNA Metabarcoding in Anthropogenic Ecosystems", 0.6, 6.15, 12.1, 0.55, font_size=12, fill_color=PALE_AMBER, border_color=AMBER, text_color=INK)
    update_notes(s21,
        "Slide 21 forms our direct bridge to Pak Hilman's upcoming session. When transitioning from intact bacterial 16S amplicons (~1,500 bp) "
        "to aquatic vertebrate eDNA, the biological sample is fundamentally different. Environmental water shed by fish contains fragmented DNA, "
        "requiring short markers like the 163 to 185 bp MiFish 12S amplicon. In our standard ONT protocol, both the post-pooling and post-adapter 0.4× bead cleanups "
        "would discard these short fragments. Recovering them requires adapted bead ratios (~1.5×–1.8×) and 100 fmol loading amounts. "
        "Furthermore, EPI2ME wf-16s default length filters and databases exclude 12S. As we'll hear next from Pak Hilman, short-read Illumina sequencing "
        "natively handles ~170 bp fragments without these modifications. [Time: 2.5 min]"
    )

    # 24. Slide 24 (Strengths, Limitations, Pitfalls)
    s24 = prs.slides[23]
    for shape in s22.shapes:
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Real-time data" in txt or "Strengths" in txt:
                shape.text_frame.text = (
                    "Strengths & Capabilities\n"
                    "• Full-length operon sequencing resolves species & strains\n"
                    "• Real-time data acquisition: stop run once depth is met\n"
                    "• Portable sequencing from remote field to core facility\n"
                    "• Functional prediction: link taxonomy to ecology (PICRUSt2/FUNGuild)\n"
                    "• Directly addresses: Who is there? What are they doing?"
                )
                for p_idx, p in enumerate(shape.text_frame.paragraphs):
                    p.font.name = "Arial"
                    p.font.size = Pt(13.5) if p_idx == 0 else Pt(11.5)
                    p.font.bold = (p_idx == 0)
                    p.font.color.rgb = WHITE  # Crisp white text on Teal background
                    for r in p.runs:
                        r.font.color.rgb = WHITE
            elif "Primer bias" in txt or "Limitations" in txt:
                shape.text_frame.text = (
                    "Limitations & Critical Pitfalls\n"
                    "• PCR primer amplification bias distorts true taxon ratios\n"
                    "• Reagent 'kitome' contamination in low-biomass extractions\n"
                    "• 16S rRNA gene copy number variation (1–21 copies per genome)\n"
                    "• Reference database gaps lead to false 'unclassified' calls\n"
                    "• Relative read proportions ≠ living organism cell counts"
                )
                for p_idx, p in enumerate(shape.text_frame.paragraphs):
                    p.font.name = "Arial"
                    p.font.size = Pt(13.5) if p_idx == 0 else Pt(11.5)
                    p.font.bold = (p_idx == 0)
                    p.font.color.rgb = WHITE  # Crisp white text on Amber/Dark background
                    for r in p.runs:
                        r.font.color.rgb = WHITE
    update_notes(s22,
        "On Slide 22, we synthesize our capabilities against methodological pitfalls. Amplicon sequencing empowers culture-independent surveillance, "
        "allowing us to identify organisms and infer their functional potential—such as using PICRUSt2 for predicted metabolic pathways or FUNGuild for ecological guilds, "
        "answering what they might be doing. However, rigorous science demands troubleshooting discipline: universal primers amplify taxa unequally, "
        "commercial spin columns carry a background kitome, and 16S copy numbers vary up to 21-fold. "
        "Always evaluate negative controls first: if your extraction blank has reads, flag those taxa before interpreting your biological samples! [Time: 2.5 min]"
    )

    # 25. Slide 25 (Key Takeaways & Session Handoff)
    s25 = prs.slides[24]
    for shape in s23.shapes:
        if shape.has_text_frame:
            txt = shape.text_frame.text
            if "Session Handoff:" in txt or "Discussion:" in txt:
                shape.text_frame.text = "Session Handoff: Pak Hilman · Fish eDNA Metabarcoding in Anthropogenic Ecosystems"
                p = shape.text_frame.paragraphs[0]
                p.font.name = "Arial"
                p.font.size = Pt(13)
                p.font.bold = True
                p.font.color.rgb = WHITE  # Crisp Stark White on Dark Navy bar!
                for r in p.runs:
                    r.font.name = "Arial"
                    r.font.size = Pt(13)
                    r.font.bold = True
                    r.font.color.rgb = WHITE
    update_notes(s23,
        "To conclude: amplicon sequencing is an interconnected chain of decisions from biological question to taxonomic classification. "
        "Marker selection defines your taxonomic scope; stoichiometric precision (femtomoles) governs enzymatic ligation; "
        "proper priming and bubble elimination safeguard flow cell pores; and neural basecalling yields calibrated sequences that must be interpreted "
        "with compositionality and copy-number awareness. "
        "We now have 10 full minutes for audience questions and discussion, after which I am delighted to hand the stage over to Pak Hilman, "
        "who will share real-world field case studies using Illumina short-read sequencing for fish eDNA metabarcoding. Thank you very much! [Time: 2 min]"
    )
    update_notes(s23,
        "To conclude: amplicon sequencing is an interconnected chain of decisions from biological question to taxonomic classification. "
        "Marker selection defines your taxonomic scope; stoichiometric precision (femtomoles) governs enzymatic ligation; "
        "proper priming and bubble elimination safeguard flow cell pores; and neural basecalling yields calibrated sequences that must be interpreted "
        "with compositionality and copy-number awareness. "
        "We now have 10 full minutes for audience questions and discussion, after which I am delighted to hand the stage over to Pak Hilman, "
        "who will share real-world field case studies using Illumina short-read sequencing for fish eDNA metabarcoding. Thank you very much! [Time: 2 min]"
    )

    prs.save(PPTX_PATH)
    print(f"Successfully updated and saved {PPTX_PATH}")

if __name__ == '__main__':
    main()
