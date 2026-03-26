# Identifying Depression Through Speech

**A Comparative Analysis of Acoustic Features in Read and Spontaneous Speech**

Level 4 Dissertation — University of Glasgow, School of Computing Science

## Overview

This project investigates which acoustic features of speech are most predictive of depression, comparing read and spontaneous (interview) speech tasks. Using the ANDROIDS corpus (118 speakers with clinical diagnoses) and the eGeMAPS feature set (88 acoustic features), we demonstrate that:

- Interview speech (87.1% accuracy) significantly outperforms reading (72.3%, p = 0.0055)
- The most predictive features differ entirely between tasks (only 1/10 overlap)
- Variability measures dominate interview speech classification (7/10 top features)
- Interpretable models (Random Forest) match or exceed deep learning baselines

## Repository Structure

```
├── dissertation.tex          # Main LaTeX document
├── l4proj.cls                # Glasgow L4 project class file
├── drafts/sections/          # Individual chapter .tex files
│   ├── 01_introduction.tex
│   ├── 02_background.tex
│   ├── 03_methodology.tex
│   ├── 04_implementation.tex
│   ├── 05_results.tex
│   ├── 06_discussion.tex
│   └── 07_conclusion.tex
├── references/
│   └── dissertation.bib      # Bibliography
├── scripts/                  # Analysis code
│   ├── extract_features.py   # Feature extraction using openSMILE
│   ├── run_analysis.py       # Classification and feature importance
│   └── advanced_analysis.py  # Confusion matrices, significance tests, learning curves
├── features/                 # Extracted feature CSVs
├── results/                  # Classification results and importance rankings
├── figures/                  # Generated figures
└── presentation/             # Presentation slides and script
```

## Data

This project uses the **ANDROIDS corpus** (Androids Corpus of Depressed and Non-Depressed Speech). The raw audio data is not included in this repository due to size constraints.

The corpus can be accessed at: https://github.com/Android-Corpus/ANDROIDS

Pre-extracted features are included in the `features/` directory as CSV files.

## Dependencies

- Python 3.10+
- opensmile (Python package for eGeMAPS feature extraction)
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- scipy
- tqdm

Install all dependencies:

```bash
pip install opensmile scikit-learn pandas numpy matplotlib seaborn scipy tqdm
```

## Reproducing Results

See `manual.md` for detailed step-by-step instructions.

Quick start (if features are already extracted):

```bash
cd scripts
python run_analysis.py          # Main classification and feature importance
python advanced_analysis.py     # Confusion matrices, significance tests, learning curves
```

## Compilation

The dissertation is compiled using pdfLaTeX:

```bash
pdflatex dissertation.tex
bibtex dissertation
pdflatex dissertation.tex
pdflatex dissertation.tex
```

Or open in Overleaf and compile directly.

## Author

Nile — University of Glasgow, 2025-26
