# ICONLITE Scientific References: Audit Register (8 Nov 2026)

Method: each reference was searched and its bibliographic record checked against independent index records (PubMed/PMC, publisher pages, DOAJ and similar open-access aggregators). DOIs below are those shown in those records. I did not resolve DOIs through a resolver.

| # | Reference | Journal, year, vol(pages) | DOI | Result |
|---|---|---|---|---|
| 1 | Deamer, Akeson, Branton. Three decades of nanopore sequencing | Nat Biotechnol 2016;34(5):518-524 | 10.1038/nbt.3423 | Confirmed |
| 2 | Johnson et al. Evaluation of 16S rRNA gene sequencing for species and strain-level microbiome analysis | Nat Commun 2019;10:5029 | 10.1038/s41467-019-13036-1 | Confirmed; CC BY 4.0 |
| 3 | Hebert, Cywinska, Ball, deWaard. Biological identifications through DNA barcodes | Proc R Soc B 2003;270(1512):313-321 | 10.1098/rspb.2002.2218 | Confirmed |
| 4 | Schoch et al. Nuclear ribosomal internal transcribed spacer (ITS) region as a universal DNA barcode marker for Fungi | PNAS 2012;109(16):6241-6246 | 10.1073/pnas.1117018109 | Confirmed; **title corrected** (earlier draft shortened it) |
| 5 | Miya et al. MiFish, a set of universal PCR primers... | R Soc Open Sci 2015;2(7):150088 | 10.1098/rsos.150088 | Confirmed; amplicon is 163-185 bp (handbook table corrected from "~0.17 kb") |
| 6 | Taberlet, Coissac, Hajibabaei, Rieseberg. Environmental DNA | Mol Ecol 2012;21(8):1789-1793 | 10.1111/j.1365-294X.2012.05542.x | Confirmed; it is the **introduction to a special issue**, now labelled so |
| 7 | Kebschull & Zador. Sources of PCR-induced distortions... | Nucleic Acids Res 2015;43(21):e143 | 10.1093/nar/gkv717 | Confirmed |
| 8 | Salter et al. Reagent and laboratory contamination... | BMC Biol 2014;12:87 | 10.1186/s12915-014-0087-z | Confirmed; CC BY |
| 9 | McMurdie & Holmes. Waste not, want not: why rarefying microbiome data is inadmissible | PLoS Comput Biol 2014;10(4):e1003531 | 10.1371/journal.pcbi.1003531 | Confirmed. **Note:** it argues *against* rarefying; Ch.12 now says so, since wf-16s offers a rarefied table |
| 10 | Gloor et al. Microbiome datasets are compositional: and this is not optional | Front Microbiol 2017;8:2224 | 10.3389/fmicb.2017.02224 | Confirmed; CC BY 4.0 |
| 11 | Li. Minimap2: pairwise alignment for nucleotide sequences | Bioinformatics 2018;34(18):3094-3100 | 10.1093/bioinformatics/bty191 | Confirmed |
| 12 | Wood, Lu, Langmead. Improved metagenomic analysis with Kraken 2 | Genome Biol 2019;20:257 | 10.1186/s13059-019-1891-0 | Confirmed |
| 13 | Lu, Breitwieser, Thielen, Salzberg. Bracken: estimating species abundance in metagenomics data | PeerJ Comput Sci 2017;3:e104 | 10.7717/peerj-cs.104 | Confirmed; CC BY 4.0 |
| 14 | Quast et al. The SILVA ribosomal RNA gene database project: improved data processing and web-based tools | Nucleic Acids Res 2013;41(D1):D590-D596 | 10.1093/nar/gks1219 | Confirmed; **subtitle added** |
| 15 | O'Leary et al. Reference sequence (RefSeq) database at NCBI... | Nucleic Acids Res 2016;44(D1):D733-D745 | 10.1093/nar/gkv1189 | Confirmed as a paper. Used only as RefSeq background; I did not verify that it describes the exact wf-16s "NCBI targeted loci" collection |

Added during the audit (cited in the handbook as further reading and as figure sources):
- Jain, Olsen, Paten, Akeson. The Oxford Nanopore MinION... Genome Biol 2016;17:239, doi 10.1186/s13059-016-1103-0 (CC BY 4.0; an erratum for the Outlook section exists, doi 10.1186/s13059-016-1122-x).
- Rang, Kloosterman, de Ridder. From squiggle to basepair... Genome Biol 2018;19:90, doi 10.1186/s13059-018-1462-9 (CC BY 4.0).
- Wang, Zhao, Bollas, Wang, Au. Nanopore sequencing technology, bioinformatics and applications. Nat Biotechnol 2021;39(11):1348-1365, doi 10.1038/s41587-021-01108-x (no open licence seen).

## Page-verified sources (fetched 8 Nov 2026)
1. ONT SQK-NBD114.24 PromethION protocol, rev. NBA_9168_v114_revU_15Jul2026.
2. EPI2ME wf-16s documentation.
3. ONT media-resources page (press images listed; "All images to be credited to Oxford Nanopore Technologies").
4. ONT GridION brochure page: up to five MinION Flow Cells (confirms the "up to 5" in Ch.7).
5. ONT MinKNOW Technical Document MITD_5000_v1_revAK_25Nov2024 and Experiment Companion – MinKNOW (menu sequence used in handbook 9.6).
6. REDI-NET SW-4 SWAB TESTING SOP, protocols.io, doi 10.17504/protocols.io.n2bvj38mnlk5/v3 (CC BY): independent confirmation of the MinKNOW sequence; its MinION loading mix is 75 µL (37.5 SB + 25.5 LIB + 12 library) versus 200 µL on PromethION. It is for the 96-barcode kit, so its volumes were **not** imported.

## Still unverified (general knowledge)
16S V-region boundaries (approximate E. coli positions); NEB end-prep module chemistry wording; MinKNOW output folder layout; DNA translocation speed for R10.4.1 (Wang 2021 gives ~250 bases/s for an R9.4 pore; the handbook says "hundreds of bases per second").
