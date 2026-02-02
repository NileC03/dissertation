# Chapter 4: Implementation

## 4.1 Development Environment

### Hardware
- Standard personal computer (macOS)
- 8-16 GB RAM
- SSD storage (4GB+ for corpus)
- **No GPU required** — traditional ML methods

### Software Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| Python | 3.11+ | Programming language |
| openSMILE | 2.5.0 | Acoustic feature extraction |
| scikit-learn | 1.3+ | Machine learning algorithms |
| pandas | 2.0+ | Data manipulation |
| NumPy | 1.24+ | Numerical computing |
| matplotlib | 3.7+ | Visualisation |
| seaborn | 0.12+ | Statistical plots |

Virtual environment (`venv`) used for dependency isolation.

---

## 4.2 Data Processing Pipeline

### Corpus Organisation

```
data/Androids-Corpus/
├── Reading-Task/
│   └── audio/
│       ├── HC/     # Healthy controls (54 files)
│       └── PT/     # Patients (58 files)
└── Interview-Task/
    └── audio/
        ├── HC/     # Healthy controls (52 files)
        └── PT/     # Patients (64 files)
```

**Filename format:** `nn_XGmm_t.wav`
- `nn` — Speaker ID
- `X` — Condition (P=patient, C=control)
- `G` — Gender (M/F)
- `mm` — Age
- `t` — Education level

### Feature Extraction Implementation

The `extract_features.py` script:

1. Iterates through all WAV files
2. Extracts 88 eGeMAPS features per recording
3. Parses metadata from filenames
4. Combines features + metadata into DataFrame
5. Saves CSV and pickle formats

**Output files:**
- `all_features.csv` — Complete matrix (228 samples × 97 columns)
- `reading_features.csv` — Reading task (112 samples)
- `interview_features.csv` — Interview task (116 samples)
- `all_features.pkl` — Binary format for fast loading

---

## 4.3 Model Training Implementation

### Data Preparation

```python
# Separate features from metadata
metadata_cols = ['filename', 'speaker_id', 'condition',
                 'gender', 'age', 'education', 'label',
                 'task', 'depression']
feature_cols = [c for c in df.columns if c not in metadata_cols]

X = task_df[feature_cols].values  # Shape: (n_samples, 88)
y = task_df['depression'].values  # Shape: (n_samples,)
```

### Cross-Validation Setup

```python
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

- Stratified: maintains class balance in each fold
- Fixed seed: ensures reproducibility

### SVM Training

```python
svm_pipe = Pipeline([
    ('scaler', StandardScaler()),  # Zero mean, unit variance
    ('svm', SVC(kernel='rbf', C=1.0, random_state=42))
])
```

StandardScaler is **essential** for RBF kernel — sensitive to feature magnitudes.

### Random Forest Training

```python
rf = RandomForestClassifier(
    n_estimators=100,    # Sufficient for stable estimates
    max_depth=10,        # Prevents overfitting
    n_jobs=-1,           # Use all CPU cores
    random_state=42
)
```

---

## 4.4 Feature Importance Implementation

### Gini Importance

```python
rf.fit(X, y)

rf_importance = pd.DataFrame({
    'feature': feature_cols,
    'importance': rf.feature_importances_
}).sort_values('importance', ascending=False)
```

Measures contribution to reducing impurity across tree splits.

### Permutation Importance

```python
perm_result = permutation_importance(
    rf, X, y,
    n_repeats=10,        # Stable estimates
    random_state=42,
    n_jobs=-1
)
```

More robust: shuffles each feature, measures accuracy degradation.

---

## 4.5 Visualisation

```python
fig, ax = plt.subplots(figsize=(12, 8))
top20 = perm_importance.head(20)

ax.barh(range(len(top20)), top20['importance'].values)
ax.set_yticklabels(top20['feature'].values)
ax.invert_yaxis()  # Highest at top
plt.savefig(f'figures/{task}_feature_importance.png', dpi=150)
```

Horizontal bars for readability of long feature names.

---

## 4.6 Output Structure

```
results/
├── summary.csv
├── reading_gini_importance.csv
├── reading_perm_importance.csv
├── interview_gini_importance.csv
└── interview_perm_importance.csv

figures/
├── reading_feature_importance.png
└── interview_feature_importance.png
```

### Version Control

Git tracks code changes. Large files excluded:

```
# .gitignore
data/Androids-Corpus/
data/*.zip
.venv/
__pycache__/
```

---

## 4.7 Execution Workflow

```bash
# 1. Extract features (run once, ~2-3 minutes)
python scripts/extract_features.py

# 2. Run analysis (~1 minute)
python scripts/run_analysis.py
```

---

## 4.8 Summary

Implementation follows best practices:

- **Modularity:** Separate scripts for extraction/analysis
- **Reproducibility:** Fixed seeds, virtual environment, version control
- **Efficiency:** Parallel processing where possible
- **Documentation:** Clear variable names, inline comments

All code available in project repository.

---

*Estimated length: 4-5 pages*
