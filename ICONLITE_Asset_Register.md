# ICONLITE Asset Register (Updated & Verified)

All visual assets referenced below have been curated, placed in `/assets`, and embedded into the slide deck (`ICONLITE_ONT_Amplicon_Sequencing_Workshop.pptx`) and companion handbook (`ICONLITE_ONT_Amplicon_Sequencing_Handbook.md` / `.docx` / `.pdf`).

---

## 1. Laboratory & Experimental Visuals
| Asset File | Target Placement | Description / Source | Attribution / License |
|---|---|---|---|
| `assets/common-amplicon-markers/16S-rRNA-PCR-gel-image.jpg` | Slide 9 (H1), Handbook Section 9.1 (Fig. 9.1) | Real 1.5% agarose gel electrophoresis verifying sharp ~1.5 kb 16S rRNA PCR amplicon band | Laboratory archive / Research SOP |
| `assets/ampure-xp-beads-workflow.png` | Handbook Section 9.2 (Fig. 9.2) | Magnetic SPRI bead cleanup workflow (PEG/NaCl binding, wash, elution) | Molecular biology illustration |
| `assets/ONT-NBD-RBK-kit-reagent-layout.png` | Handbook Section 9.3 (Fig. 9.3) | Reagent tube layout for Native Barcoding Kit (SQK-NBD114.24) | Technical laboratory layout |

---

## 2. Nanopore Biophysics & Basecalling Architecture
| Asset File | Target Placement | Description / Source | Attribution / License |
|---|---|---|---|
| `assets/nanopore-sequencing-principle-Wang2021.png` | Slide 6, Handbook Section 6.1 (Fig. 6.1) | Nanopore biosensing overview: motor protein, synthetic membrane, ASIC sensor chip, and ionic current trace | Adapted from Wang et al., 2021 (*Nat Biotechnol* 39:1348–1365; doi:10.1038/s41587-021-01108-x) |
| `assets/ETH-Zurich-nanopore-sequencing-illustration.png` | Handbook Section 6.1 (Fig. 6.2) | Physical schematic of single-molecule translocation under constant voltage | ETH Zurich Single-Molecule Biophysics |
| `assets/ONTR9vsR10-nanopore-diagram.png` | Slide 20, Handbook Section 6.2 (Fig. 6.3) | Structural comparison between R9.4.1 (single constriction) and R10.4.1 (dual-reader head spaced ~1.4 nm apart) | ONT pore engineering technical schematic |
| `assets/ONT-basecalling-neural-network-diagram.png` | Slide 20, Handbook Section 6.3 (Fig. 6.4) | Deep neural network architecture: PyTorch CNN feature extraction + Transformer/CRF temporal sequence decoding | Dorado basecalling architecture schematic |
| `assets/ONT-signal-to-sequence-basecalling.png` | Slide 17, Handbook Section 6.3 (Fig. 6.5) | Real-time conversion of continuous ionic squiggles into basecalled FASTQ records with Phred scores | Basecalling signal transformation schematic |

---

## 3. Hardware & Flow Cell Architecture
| Asset File | Target Placement | Description / Source | Attribution / License |
|---|---|---|---|
| `assets/minion-promethion-flow-cells.png` | Slide 7 | Platform comparison: portable MinION flow cell vs high-density PromethION flow cell | Oxford Nanopore Technologies |
| `assets/promethion-flow-cell-annotated-3d.png` | Slide 13 (H5), Handbook Section 9.5 (Fig. 9.4) | PromethION flow cell 3D diagram showing inlet port, micro-channels, waste ports, and electrical contact pin arrays | Technical flow cell architecture model |
| `assets/promethion-flow-cell-anatomy.jpg` | Handbook Section 9.5 (Fig. 9.5) | Fluidic port architecture and loading port aperture | Technical flow cell anatomy |

---

## 4. Software & Analysis Interfaces
| Asset File | Target Placement | Description / Source | Attribution / License |
|---|---|---|---|
| `assets/software-screenshots/MinKNOW-sequencing-run-configuration1.jpeg` | Slide 14 (H6), Handbook Section 9.6 (Fig. 9.6) | MinKNOW run configuration interface: position, FLO-PRO114M chemistry, SQK-NBD114.24 kit, and real-time basecalling | MinKNOW acquisition software |
| `assets/software-screenshots/MinKNOW-sequencing-run-dashboard.jpeg` | Handbook Section 9.6 (Fig. 9.7) | MinKNOW sequencing dashboard: active pore occupancy, throughput, and Phred quality score distributions | MinKNOW acquisition software |
| `assets/software-screenshots/EPI2ME-workflow-selection.jpeg` | Handbook Section 9.7 (Fig. 9.8) | EPI2ME desktop application interface showing available Nextflow workflows | EPI2ME Desktop platform |
| `assets/software-screenshots/wf16s-run-start-page.jpeg` | Slide 15 (H7), Handbook Section 9.7 (Fig. 9.9) | Parameter configuration screen for `wf-16s`: classifier choice, database selection, and read length filters | EPI2ME `wf-16s` pipeline |

---

## 5. Common Amplicon Marker Schematics (`assets/common-amplicon-markers/`)
| Asset File | Target Placement | Description |
|---|---|---|
| `16S-rRNA-generated.png` | Handbook Section 4.1 (Fig. 4.1) | Bacterial 16S rRNA gene map showing V1–V9 hypervariable regions and universal primer binding sites |
| `16S-23S-bacteria-generated.png` | Handbook Section 4.1 (Fig. 4.2) | Bacterial 16S–ITS–23S ribosomal operon schematic for extended long-read amplicons |
| `fungal-ribosomal-DNA-generated.png` | Handbook Section 4.2 (Fig. 4.3) | Fungal ribosomal operon architecture showing 18S, ITS1, 5.8S, ITS2, and 28S genes |
| `fungal-ITS-primer-map-generated.png` | Handbook Section 4.2 (Fig. 4.4) | Detailed fungal ITS primer map highlighting ITS1F, ITS2, ITS3, and ITS4 sites |
| `18S-rRNA-generated.png` | Handbook Section 4.3 (Fig. 4.5) | Eukaryotic 18S rRNA gene structure illustrating V1–V9 hypervariable regions |
| `animal-COI-generated.png` | Handbook Section 4.4 (Fig. 4.6) | Mitochondrial COI gene showing standard Folmer region and internal Leray mini-barcode |
| `fish-12S-generated.png` | Slide 21, Handbook Section 4.5 (Fig. 4.7) | Vertebrate mitochondrial 12S rRNA gene schematic highlighting short MiFish amplicon |
| `plant-trnL-generated.png` | Handbook Section 4.6 (Fig. 4.8) | Chloroplast *trnL* (UAA) locus showing full c/d intron and ultra-short internal P6 loop |
