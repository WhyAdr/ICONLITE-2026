# ICONLITE Slide Storyboard (Synchronized & Polished)

**Session Title:** From Sample to Species: Amplicon Sequencing Using Oxford Nanopore Technology  
**Context:** Technical workshop session at ICONLITE 2026, pairing with Pak Hilman's session (*Fish eDNA Metabarcoding in Anthropogenic Ecosystems*).  
**Time Allocation:** 50 minutes core presentation + 10 minutes interactive discussion/Q&A = 60 minutes total.

---

## 1 · 1 — From Sample to Species
- **Objective:** Establish the central narrative grounded in three fundamental biological questions: *Who is there? What might they be doing? Why is it necessary to know them?*
- **Takeaway:** Amplicon sequencing turns an environmental or clinical sample into high-resolution taxonomic profiles (genus and species level).
- **Visual / data:** Four-step pipeline (sample, DNA + marker PCR, nanopore sequencing, taxonomic report) on widescreen cover with clean, anonymous branding.
- **Data status:** Conceptual
- **Handbook:** Ch. 1
- **Time:** 1.5 min

## 2 · 2 — Why do we need amplicon sequencing?
- **Objective:** Introduce the ecological problem: identifying organisms in complex, uncultured communities.
- **Takeaway:** Targeted sequencing identifies organisms that culture (<1%) and microscopy miss, at scalable high throughput.
- **Visual / data:** Three stacked cards: culture-based, targeted molecular ID, community profiling; interactive audience question callout.
- **Data status:** Conceptual
- **Handbook:** Ch. 2
- **Time:** 2.0 min

## 3 · 3 — Barcoding vs. metabarcoding vs. metagenomics
- **Objective:** Prevent confusion between related high-throughput sequencing strategies.
- **Takeaway:** The three differ in biological input (single specimen vs. environmental mixture), whether targeted PCR is performed, and genomic scope recovered.
- **Visual / data:** Comparison table across question, input, target, strength, and limitation.
- **Data status:** Conceptual
- **Handbook:** Ch. 3
- **Time:** 2.0 min

## 4 · 4 — Choosing the right molecular marker
- **Objective:** Show how marker and primer selection dictate the taxonomic scope and phylogenetic resolution of an experiment.
- **Takeaway:** No single marker is universal; choice depends on biology, fragment preservation state, and reference database completeness.
- **Visual / data:** Marker-selection matrix (16S rRNA, fungal ITS, eukaryotic 18S, animal COI, fish 12S rRNA [163–185 bp MiFish; Miya et al. 2015], plant trnL) plus caveat bar.
- **Data status:** Conceptual matrix
- **Handbook:** Ch. 4
- **Time:** 2.0 min

## 5 · 5 — Short-read vs. long-read amplicons
- **Objective:** Contrast short hypervariable windows with full-length amplicons.
- **Takeaway:** Full-length amplicons capture complete variable suites to resolve species; shorter targets survive fragmented eDNA.
- **Visual / data:** Schematic bacterial 16S rRNA gene with hypervariable regions V1–V9, comparing short V3–V4 (~0.45 kb) vs. full-length 16S (~1.5 kb).
- **Data status:** Conceptual schematic
- **Handbook:** Ch. 5
- **Time:** 2.0 min

## 6 · 6 — How does nanopore sequencing work?
- **Objective:** Build a physical and biophysical understanding of single-molecule nanopore sensing.
- **Takeaway:** Single DNA strands moving through a pore modulate ionic current; deep neural network basecallers decode current shifts into sequence.
- **Visual / data:** Published review schematic from Wang et al., 2021 (*Nat. Biotechnol.*) showing motor protein, membrane, pore translocation, ASIC sensor chip, and ionic current recording.
- **Data status:** Published review schematic (Wang et al. 2021)
- **Handbook:** Ch. 6.1
- **Time:** 2.5 min

## 7 · 7 — ONT platforms and applications
- **Objective:** Introduce Oxford Nanopore instrumentation across throughput scales without a product catalogue.
- **Takeaway:** Shared nanopore sensing chemistry across all devices; platforms scale by active channels and compute capacity.
- **Visual / data:** Three-platform scale table (Flongle: 126 channels; MinION: 512 channels / 800-pore warranty; GridION: 5 flow cells; PromethION: 3,000 channels / 5,000-pore warranty) paired with official flow cell hardware photo.
- **Data status:** Conceptual table + official flow cell photo
- **Handbook:** Ch. 7
- **Time:** 2.0 min

## 8 · 8 — From sample to library: the big picture
- **Objective:** Bridge conceptual foundations to the guided practical.
- **Takeaway:** PCR amplifies marker amplicons first; the Native Barcoding library preparation itself is enzymatic and PCR-free.
- **Visual / data:** Six-step laboratory workflow from sample collection to sequencing, paired with essential experimental controls (extraction blank, PCR NTC, mock community).
- **Data status:** Conceptual workflow diagram
- **Handbook:** Ch. 8
- **Time:** 2.5 min

## 9 · H1 — Preparing and evaluating PCR amplicons
- **Objective:** Evaluate amplicon purity and understand stoichiometric molar input.
- **Takeaway:** Library input is governed by molarity (fmol), not mass (ng): equal mass does not imply equal molecules.
- **Visual / data:** Real agarose gel photograph of ~1.5 kb 16S amplicons (`16S-rRNA-PCR-gel-image.jpg`), mass-to-molarity formula card (200 fmol = 198 ng for 1.5 kb dsDNA), and equal-mass vs. equal-fmol table.
- **Data status:** Real laboratory gel photograph + protocol calculations
- **Handbook:** Ch. 9.1
- **Time:** 2.5 min

## 10 · H2 — End-prep: getting DNA ready for ligation
- **Objective:** Explain enzymatic end-repair and dA-tailing.
- **Takeaway:** End-prep repairs ragged DNA termini and appends a single 3′ dA-overhang required for barcode ligation.
- **Visual / data:** Reagent table (15 µL reaction), thermal cycler profile (20 °C 5 min, 65 °C 5 min), and 1.0× AMPure XP bead cleanup steps.
- **Data status:** Protocol-verified (`SQK-NBD114.24`)
- **Handbook:** Ch. 9.2
- **Time:** 2.0 min

## 11 · H3 — Native barcoding and multiplexing
- **Objective:** Explain molecular barcoding and sample pooling.
- **Takeaway:** Each biological sample receives a unique native barcode (`NB01`–`NB24`) before pooling; reactions are quenched with EDTA before combination.
- **Visual / data:** Six samples receiving unique native barcodes, pooling reaction arithmetic, 0.4× AMPure XP bead cleanup, and SFB washes.
- **Data status:** Protocol-verified (`SQK-NBD114.24`)
- **Handbook:** Ch. 9.3
- **Time:** 2.5 min

## 12 · H4 — Sequencing adapters and final clean-up
- **Objective:** Distinguish sample-identifying barcodes from sequencing adapters.
- **Takeaway:** Barcodes identify sample provenance; Native Adapters carry the motor protein that engages the pore; SFB retains amplicons while ethanol ruins motor proteins.
- **Visual / data:** Molecular library anatomy cartoon, adapter ligation reaction recipe (50 µL), and SFB vs. LFB decision cards.
- **Data status:** Protocol-verified (`SQK-NBD114.24`)
- **Handbook:** Ch. 9.4
- **Time:** 2.5 min

## 13 · H5 — Priming and loading the PromethION flow cell
- **Objective:** Master physical flow cell loading steps and identify critical failure modes.
- **Takeaway:** Proper bubble elimination, tether pre-treatment, and thorough bead mixing prevent pore loss and low occupancy.
- **Visual / data:** Annotated 3D PromethION flow cell architecture diagram, priming mix recipe (1,200 µL), loading mix recipe (200 µL), and six-step loading sequence.
- **Data status:** Protocol-verified PromethION procedure + 3D architecture visual
- **Handbook:** Ch. 9.5
- **Time:** 2.5 min

## 14 · H6 — MinKNOW: from library to data
- **Objective:** Walk through the transition from physical bench to digital data acquisition.
- **Takeaway:** Reproducible run parameters (kit selection, basecalling models, Q filters) ensure data traceability and downstream classification accuracy.
- **Visual / data:** Real MinKNOW interface screenshot (`MinKNOW-sequencing-run-configuration1.jpeg`) showing flow cell status, kit selection (`SQK-NBD114.24`), and real-time basecalling configuration.
- **Data status:** Real software screenshot from ONT acquisition platform
- **Handbook:** Ch. 9.6
- **Time:** 2.0 min

## 15 · H7 — From FASTQ to biological interpretation
- **Objective:** Walk through a reproducible bioinformatics workflow using EPI2ME `wf-16s`.
- **Takeaway:** Quality control, length filtering, and classifier choice (minimap2 vs. Kraken2) determine the final taxonomic abundance matrix.
- **Visual / data:** Five-step analysis pipeline paired with real EPI2ME `wf-16s` setup interface screenshot (`wf16s-run-start-page.jpeg`), highlighting parameter defaults and database selection.
- **Data status:** Real software screenshot from EPI2ME platform
- **Handbook:** Ch. 9.7
- **Time:** 2.5 min

## 16 · H8 — Mini lab exercise: five decisions
- **Objective:** Reinforce critical workflow decisions made throughout the practical with an interactive checkpoint.
- **Takeaway:** Every experimental decision directly traces back to a biophysical or enzymatic protocol rule.
- **Visual / data:** Five structured scenario cards covering: (1) Stoichiometry calculation (200 fmol = 198 ng for 1.5 kb); (2) Controls and pooling (quench with EDTA before pooling); (3) Wash buffer selection (SFB mandatory for amplicons); (4) Loading mix recipe & rest (rest ≥10 min); (5) Laboratory failure diagnosis (ethanol after adapter ligation drops occupancy to ~0%).
- **Data status:** Interactive exercise with full answer key in notes and handbook
- **Handbook:** Ch. 14 / Appendix
- **Time:** 3.0 min

## 17 · 9 — From raw signal to FASTQ reads
- **Objective:** Explain how continuous electrical measurements become discrete nucleotide sequences.
- **Takeaway:** Basecalling converts raw ionic current into reads and per-base Phred confidence scores; basecalling yields sequences, not species.
- **Visual / data:** Real-time signal-to-sequence transformation visual, Phred quality score definition ($Q = -10 \log_{10} P$), and Dorado neural network basecalling role.
- **Data status:** Conceptual + basecalling architecture visual
- **Handbook:** Ch. 10
- **Time:** 2.0 min

## 18 · 10 — Read QC and taxonomic classification
- **Objective:** Contrast alignment-based and k-mer-based classification strategies.
- **Takeaway:** Neither algorithm is universally "better": minimap2 provides finer species resolution, whereas Kraken2 provides maximum execution speed.
- **Visual / data:** Structured comparison table between minimap2 alignment and Kraken2 + Bracken k-mer matching across principles, strengths, and caveats.
- **Data status:** EPI2ME `wf-16s` documented defaults
- **Handbook:** Ch. 11
- **Time:** 2.5 min

## 19 · 11 — Reading community profiles critically
- **Objective:** Teach rigorous ecological interpretation of taxonomic profiles rather than uncritical display.
- **Takeaway:** Sequence read proportions represent compositional fractions, not absolute living organism counts, due to copy number variation (rrnDB v5: 1–21 copies) and primer bias.
- **Visual / data:** Stacked bar chart (simulated composition), alpha/beta diversity summary, and preserved audience question callout.
- **Data status:** Simulated composition chart (clearly labeled)
- **Handbook:** Ch. 12
- **Time:** 2.5 min

## 20 · 12 — Pore Architecture & Accuracy: R9.4.1 vs. R10.4.1
- **Objective:** Explain the biophysical and computational engineering that elevated nanopore accuracy to >Q20 (>99%).
- **Takeaway:** Dual reader heads break homopolymer ambiguity, and deep neural network basecallers eliminate historical accuracy bottlenecks.
- **Visual / data:** Three crisp bullets paired with R9 vs. R10 dual-reader pore structural comparison diagram and Dorado deep neural network basecalling pipeline schematic.
- **Data status:** Published pore engineering data & ONT architecture diagrams
- **Handbook:** Ch. 6.2 & 6.3
- **Time:** 2.5 min

## 21 · 13 — Adapting Workflows for Environmental DNA (eDNA)
- **Objective:** Evaluate critical experimental adaptations required when profiling short, degraded aquatic environmental DNA.
- **Takeaway:** A single protocol does not fit all targets: bead cleanup ratios (both cleanups), loading stoichiometry, and bioinformatic filters must match fragment biology.
- **Visual / data:** Three crisp bullets paired with vertebrate mitochondrial 12S MiFish marker schematic and direct session bridge card.
- **Data status:** Methodological comparison directly bridging to Pak Hilman's fish eDNA session
- **Handbook:** Ch. 4.5 & 14 (Synthesis)
- **Time:** 2.5 min

## 22 · 14 — Strengths, limitations and pitfalls
- **Objective:** Synthesize culture-independent strengths against methodological pitfalls and troubleshooting.
- **Takeaway:** Experimental controls (extraction blanks, NTCs) separate genuine biological signals from kitome contamination; functional prediction (PICRUSt2/FUNGuild) infers ecological roles.
- **Visual / data:** Two-column benefits vs. pitfalls summary paired with a negative control troubleshooting decision tree.
- **Data status:** Conceptual
- **Handbook:** Ch. 13
- **Time:** 2.5 min

## 23 · 15 — Key takeaways and discussion
- **Objective:** Consolidate workshop learning and bridge seamlessly to Pak Hilman's fish metabarcoding session.
- **Takeaway:** Amplicon sequencing is an integrated chain of decisions; experimental choices at each step shape the resulting biological story.
- **Visual / data:** Four core takeaway cards, sample-to-species decision pipeline, and prominent session handoff card.
- **Data status:** Conceptual
- **Handbook:** Ch. 14
- **Time:** 2.0 min
