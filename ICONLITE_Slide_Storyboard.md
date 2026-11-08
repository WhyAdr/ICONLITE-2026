# ICONLITE Slide Storyboard (Phase 2)

Position = displayed slide number; H-prefixes are authoring IDs. Total delivery time: 60 min.

## 1 · 1 — From Sample to Species
- **Objective:** Set the central narrative: sample → data → organism identification.
- **Takeaway:** Amplicon sequencing turns a biological sample into a taxonomic answer.
- **Visual / data:** Four-step pipeline (sample, DNA + marker PCR, nanopore sequencing, taxonomic report) on the cover.
- **Data status:** Conceptual
- **Handbook:** Ch. 1
- **Time:** 1.5 min

## 2 · 2 — Why do we need amplicon sequencing?
- **Objective:** Introduce the problem: identifying organisms in complex samples.
- **Takeaway:** Targeted sequencing identifies organisms that culture and microscopy miss, at scale.
- **Visual / data:** Three stacked cards: culture-based, targeted molecular ID, community profiling; audience question callout.
- **Data status:** Conceptual
- **Handbook:** Ch. 2
- **Time:** 2 min

## 3 · 3 — Barcoding vs. metabarcoding vs. metagenomics
- **Objective:** Prevent confusion between related approaches.
- **Takeaway:** The three differ in sample type and in whether a marker is amplified first.
- **Visual / data:** Comparison table across question, input, target, strength, limitation.
- **Data status:** Conceptual
- **Handbook:** Ch. 3
- **Time:** 2.5 min

## 4 · 4 — Choosing the right molecular marker
- **Objective:** Show that marker choice decides which groups can be studied.
- **Takeaway:** No single marker is universal; the question and the reference database decide.
- **Visual / data:** Marker-selection matrix plus a yellow caveat bar.
- **Data status:** Conceptual
- **Handbook:** Ch. 4
- **Time:** 2.5 min

## 5 · 5 — Short-read vs. long-read amplicons
- **Objective:** Explain why platform and amplicon length matter.
- **Takeaway:** Longer amplicons carry more informative sites; shorter ones survive fragmented DNA.
- **Visual / data:** Schematic 16S gene with V1–V9, a V3–V4 amplicon bar and a full-length bar.
- **Data status:** Conceptual
- **Handbook:** Ch. 5
- **Time:** 1.5 min

## 6 · 6 — How does nanopore sequencing work?
- **Objective:** Build a physical picture of nanopore sensing.
- **Takeaway:** DNA moving through a pore changes ionic current; software decodes that signal into bases.
- **Visual / data:** Pore cross-section with motor protein, schematic current trace, basecalling box.
- **Data status:** Conceptual (schematic, not real signal)
- **Handbook:** Ch. 6
- **Time:** 3 min

## 7 · 7 — ONT platforms and applications
- **Objective:** Introduce instruments without a product catalogue.
- **Takeaway:** One sensing principle; platforms differ in scale and compute.
- **Visual / data:** Three-platform scale table (instrument photos to be added from lab or ONT media kit).
- **Data status:** Conceptual
- **Handbook:** Ch. 7
- **Time:** 2 min

## 8 · 8 — From sample to library: the big picture
- **Objective:** Bridge concepts to the hands-on block.
- **Takeaway:** PCR makes the amplicons first; the barcoding kit itself is PCR-free.
- **Visual / data:** Six-step lab workflow plus a row of controls.
- **Data status:** Conceptual
- **Handbook:** Ch. 8
- **Time:** 3 min

## 9 · H1 — H1 · Preparing and evaluating PCR amplicons
- **Objective:** Evaluate amplicon suitability; understand molar input.
- **Takeaway:** Input is set in fmol, not ng: equal mass does not mean equal molarity.
- **Visual / data:** Placeholder for a real gel photo, formula card, equal-mass versus equal-fmol table.
- **Data status:** Protocol (verified); gel = real photo required
- **Handbook:** Ch. 9.1
- **Time:** 3 min

## 10 · H2 — H2 · End-prep: getting DNA ready for ligation
- **Objective:** Explain end-repair and dA-tailing.
- **Takeaway:** End-prep makes amplicon ends ready for the ligations that follow.
- **Visual / data:** Reagent table, before/after strip, thermal-cycler chips.
- **Data status:** Protocol (verified)
- **Handbook:** Ch. 9.2
- **Time:** 2.5 min

## 11 · H3 — H3 · Native barcoding and multiplexing
- **Objective:** Explain barcoding and demultiplexing.
- **Takeaway:** Each sample gets a unique barcode before pooling; identity must be tracked.
- **Visual / data:** Six samples receive barcodes then pool; reaction recipe; callout.
- **Data status:** Protocol (verified)
- **Handbook:** Ch. 9.3
- **Time:** 3 min

## 12 · H4 — H4 · Sequencing adapters and final clean-up
- **Objective:** Distinguish barcodes from sequencing adapters.
- **Takeaway:** Barcodes identify samples; adapters make DNA sequenceable; SFB suits 1.5 kb amplicons.
- **Visual / data:** Molecule cartoon, reaction table, SFB vs LFB cards.
- **Data status:** Protocol (verified)
- **Handbook:** Ch. 9.4
- **Time:** 2.5 min

## 13 · H5 — H5 · Priming and loading the PromethION flow cell
- **Objective:** Identify critical physical steps and risks.
- **Takeaway:** Air bubbles and skipped steps are the main ways to lose pores.
- **Visual / data:** Six-step sequence plus priming-mix and loading-mix tables.
- **Data status:** Protocol (verified); flow cell photo to add
- **Handbook:** Ch. 9.5
- **Time:** 3 min

## 14 · H6 — H6 · MinKNOW: from library to data
- **Objective:** Show the step from bench to digital data.
- **Takeaway:** Reproducible run settings make data interpretable later.
- **Visual / data:** Annotated real MinKNOW screenshot plus four setting chips.
- **Data status:** Real screenshot required
- **Handbook:** Ch. 9.6
- **Time:** 2 min

## 15 · H7 — H7 · From FASTQ to biological interpretation
- **Objective:** Show a compact analysis workflow.
- **Takeaway:** QC, filtering and classification choices shape the final table.
- **Visual / data:** Five-step analysis flow plus a placeholder for a real report.
- **Data status:** Real wf-16s report required
- **Handbook:** Ch. 9.7
- **Time:** 3 min

## 16 · H8 — H8 · Mini lab exercise: five decisions
- **Objective:** Reinforce workflow decisions.
- **Takeaway:** Each decision traces back to a protocol rule.
- **Visual / data:** Five question cards; answer key in notes.
- **Data status:** Conceptual (answers in notes)
- **Handbook:** Ch. 15 / answer key
- **Time:** 3 min

## 17 · 9 — From raw signal to FASTQ reads
- **Objective:** Explain how current becomes sequence.
- **Takeaway:** Basecalling produces reads, not species.
- **Visual / data:** Signal-to-reads flow and an annotated FASTQ record (generic, not real data).
- **Data status:** Conceptual
- **Handbook:** Ch. 10
- **Time:** 2.5 min

## 18 · 10 — Read QC and taxonomic classification
- **Objective:** Describe the parts of a reliable workflow.
- **Takeaway:** Method and database choices decide the output.
- **Visual / data:** Comparison table of alignment versus k-mer approaches.
- **Data status:** Conceptual; wf-16s documented defaults
- **Handbook:** Ch. 11
- **Time:** 3 min

## 19 · 11 — Reading community profiles critically
- **Objective:** Teach interpretation, not display.
- **Takeaway:** Reads are relative proportions, not cell counts.
- **Visual / data:** Native stacked bar chart (simulated, labelled) plus audience question.
- **Data status:** Simulated (labelled)
- **Handbook:** Ch. 12
- **Time:** 2.5 min

## 20 · 12 — Case study I: design and data
- **Objective:** Show a real experiment from question to data.
- **Takeaway:** Study design and QC come before any taxonomy.
- **Visual / data:** Field chips and two real QC plots from the presenter’s run.
- **Data status:** Real data required (none invented)
- **Handbook:** Ch. 13A
- **Time:** 3.5 min

## 21 · 13 — Case study II: results and interpretation
- **Objective:** Explain how classification becomes conclusions.
- **Takeaway:** Detection is not proof of viability, origin or absolute abundance.
- **Visual / data:** Real stacked bar, taxonomic summary table, three evidence-based findings.
- **Data status:** Real data required (none invented)
- **Handbook:** Ch. 13B
- **Time:** 3.5 min

## 22 · 14 — Strengths, limitations and pitfalls
- **Objective:** Encourage critical interpretation.
- **Takeaway:** Controls and context separate signal from artifact.
- **Visual / data:** Two cards plus a mini troubleshooting flow.
- **Data status:** Conceptual
- **Handbook:** Ch. 14
- **Time:** 3 min

## 23 · 15 — Key takeaways and discussion
- **Objective:** Consolidate and connect to fish eDNA.
- **Takeaway:** Amplicon sequencing is a chain of decisions; each can change the answer.
- **Visual / data:** Four takeaway cards, workflow with key decisions highlighted, discussion prompt.
- **Data status:** Conceptual
- **Handbook:** Ch. 15
- **Time:** 2 min

