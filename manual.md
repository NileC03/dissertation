# Manual — Identifying Depression Through Speech

This document explains how to set up and run the analysis pipeline for this project.

## Prerequisites

- Python 3.10 or later
- pip (Python package manager)
- pdfLaTeX (for compiling the dissertation)

## Setup

### 1. Install Python dependencies

```bash
pip install opensmile scikit-learn pandas numpy matplotlib seaborn scipy tqdm
```

### 2. Obtain the ANDROIDS corpus

The raw audio data is not included in this repository. To reproduce feature extraction from scratch:

1. Download the ANDROIDS corpus from: https://github.com/Android-Corpus/ANDROIDS
2. Place the corpus in `data/Androids-Corpus/` with the following structure:

```
data/Androids-Corpus/
├── Reading-Task/
│   └── audio/
│       ├── HC/          # Healthy control .wav files
│       └── PT/          # Patient (depressed) .wav files
└── Interview-Task/
    └── audio/
        ├── HC/
        └── PT/
```

**Note:** If you do not need to re-extract features, you can skip this step. Pre-extracted features are already included in the `features/` directory.

## Running the Analysis

All scripts should be run from the project root directory.

### Step 1: Feature Extraction (optional)

Only required if you want to re-extract features from the raw audio files.

```bash
python scripts/extract_features.py
```

This will:
- Process all .wav files in the ANDROIDS corpus
- Extract 88 eGeMAPS features per recording using openSMILE
- Save results to `features/all_features.csv`, `features/reading_features.csv`, and `features/interview_features.csv`

**Runtime:** Approximately 5-10 minutes depending on hardware.

### Step 2: Main Analysis

```bash
python scripts/run_analysis.py
```

This will:
- Load the extracted features
- Train SVM and Random Forest classifiers using 5-fold stratified cross-validation
- Compute Gini and permutation feature importance rankings
- Generate feature importance plots
- Save results to `results/` and figures to `figures/`

**Output files:**
- `results/summary.csv` — accuracy and F1 scores for both tasks and classifiers
- `results/reading_gini_importance.csv` — feature rankings for reading task
- `results/interview_gini_importance.csv` — feature rankings for interview task
- `figures/reading_feature_importance.png`
- `figures/interview_feature_importance.png`

### Step 3: Advanced Analysis

```bash
python scripts/advanced_analysis.py
```

This will:
- Generate confusion matrices for both tasks
- Produce detailed classification reports (precision, recall, F1 per class)
- Run statistical significance tests (two-proportion z-test)
- Generate learning curves
- Perform error analysis by gender
- Create comparison visualisations

**Output files:**
- `results/advanced/statistical_significance.csv`
- `results/advanced/*_classification_report.csv`
- `results/advanced/*_misclassified_samples.csv`
- `figures/advanced/accuracy_comparison.png`
- `figures/advanced/feature_importance_comparison.png`
- `figures/advanced/*_confusion_matrices.png`
- `figures/advanced/*_learning_curve.png`

## Compiling the Dissertation

### Using Overleaf (recommended)

1. Import the repository into Overleaf via GitHub sync
2. Set the main document to `dissertation.tex`
3. Set the compiler to pdfLaTeX
4. Click Recompile

### Using command line

```bash
pdflatex dissertation.tex
bibtex dissertation
pdflatex dissertation.tex
pdflatex dissertation.tex
```

The double recompilation ensures all references and citations resolve correctly.

## Key Results

Running the full pipeline will reproduce the following key findings:

| Task | Best Accuracy | Best Model |
|------|--------------|------------|
| Reading | 72.3% | Random Forest |
| Interview | 87.1% | Random Forest |

- Statistical significance of task difference: p = 0.0055
- Feature overlap between tasks (top 10): 1 out of 10
- Interview top features: 7/10 are variability measures

## Troubleshooting

- **openSMILE installation issues:** Try `pip install opensmile` in a fresh virtual environment
- **Missing features files:** Run `extract_features.py` first, or ensure `features/` directory contains the CSV files
- **LaTeX compilation errors:** Ensure `l4proj.cls` is in the same directory as `dissertation.tex`
