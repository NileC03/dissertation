# Chapter 3: Methodology

## 3.1 Research Approach

This study adopts an empirical, quantitative approach to investigate which acoustic features of speech are most predictive of depression, with a particular focus on comparing read versus spontaneous speech modalities.

**Experimental Design:**

1. Extract standardised acoustic features from speech recordings
2. Train classification models to distinguish depressed from healthy individuals
3. Analyse feature importance to identify the most predictive acoustic markers
4. Compare results across speech tasks (reading versus interview)

This approach was chosen over deep learning methods specifically because the research question centres on *interpretability*—understanding which features contribute to depression detection—rather than maximising classification accuracy alone.

---

## 3.2 Dataset Selection

### The ANDROIDS Corpus

The ANDROIDS (ANDRoid corpus fOr Identification of Depression and Suicide risk) corpus was selected for this study. It contains speech recordings from 118 Italian speakers, comprising both individuals with clinical depression diagnoses and healthy controls.

**Corpus Composition:**

| Group | Reading Task | Interview Task | Total |
|-------|--------------|----------------|-------|
| Healthy Controls (HC) | 54 | 52 | 106 |
| Patients (PT) | 58 | 64 | 122 |
| **Total** | 112 | 116 | 228 |

**Why ANDROIDS?**

- **Dual speech tasks:** Both reading and interview recordings from same participants
- **Clinical diagnoses:** Depression labels based on psychiatric assessment, not self-report
- **Public availability:** Enables reproducibility
- **Controlled recording:** Minimises environmental acoustic variation

### Speech Tasks

**Reading Task:** Participants read a standardised Italian text aloud. Provides controlled linguistic content for pure acoustic analysis.

**Interview Task:** Semi-structured interviews on daily routines, emotions, and future plans. Elicits naturalistic speech with variable content.

The inclusion of both tasks is central to the research question—the cognitive demands differ substantially, potentially interacting differently with depression-related speech patterns.

### Ethical Considerations

The ANDROIDS corpus is publicly available for research. All recordings were collected with informed consent and are anonymised. No additional ethics approval required for this secondary analysis.

---

## 3.3 Feature Extraction

### The eGeMAPS Feature Set

Acoustic features were extracted using the **extended Geneva Minimalistic Acoustic Parameter Set (eGeMAPS)**—a standardised set designed for affective computing and clinical speech analysis.

**Why eGeMAPS?**

1. **Standardisation:** Enables comparison with published literature
2. **Interpretability:** Features have clear acoustic/physiological meanings
3. **Comprehensiveness:** Covers prosody, voice quality, spectral, and temporal domains
4. **Manageable dimensionality:** 88 features—rich but not excessive

### Feature Categories

| Category | Example Features |
|----------|------------------|
| Frequency (F0) | Pitch mean, std dev, percentiles, slopes |
| Energy/Loudness | Mean loudness, peak rate, slopes |
| Spectral | MFCCs (1-4), spectral flux, formants |
| Voice Quality | Jitter, shimmer, Hammarberg index |
| Temporal | Voiced/unvoiced segment duration, speech rate |

### Extraction Process

Feature extraction used the **openSMILE toolkit** via Python bindings:

1. Load WAV file (16-bit PCM)
2. Apply eGeMAPS configuration with functional statistics
3. Generate 88-dimensional feature vector per recording
4. Store features with metadata (speaker ID, condition, task)

The "functionals" level computes statistical summaries (mean, std dev, percentiles) across the entire recording, producing fixed-length representation regardless of duration.

---

## 3.4 Classification Methods

Two algorithms were employed—both well-established for speech-based depression detection.

### Support Vector Machine (SVM)

SVMs find the hyperplane that maximally separates classes. An RBF (radial basis function) kernel captures nonlinear relationships:

**Configuration:**
- Kernel: RBF
- Regularisation (C): 1.0
- Feature standardisation: Yes (zero mean, unit variance)

### Random Forest

Ensemble of 100 decision trees, each trained on bootstrap samples with random feature subsets. Averages predictions to reduce overfitting.

**Configuration:**
- Trees: 100
- Maximum depth: 10 (prevents overfitting on small dataset)
- Split criterion: Gini impurity

---

## 3.5 Evaluation Strategy

### Cross-Validation

All results use **5-fold stratified cross-validation**:

- Stratification maintains class distribution in each fold
- Each fold: train on 80%, test on held-out 20%
- Report mean ± standard deviation across folds

### Evaluation Metrics

**Accuracy:** Proportion correctly classified

**F1 Score:** Harmonic mean of precision and recall—important given mild class imbalance

### Feature Importance Analysis

Two complementary measures identify predictive features:

**Gini Importance:** Total decrease in node impurity across Random Forest trees. Efficient but can be biased.

**Permutation Importance:** Accuracy decrease when feature values are shuffled. More reliable estimate of true predictive value. Used 10 permutations per feature.

---

## 3.6 Reproducibility

All code available in project repository:

1. `extract_features.py` — Feature extraction pipeline
2. `run_analysis.py` — Classification and importance analysis

Random seeds fixed for all stochastic processes.

---

## 3.7 Summary

This methodology enables systematic investigation through:

- Carefully selected corpus with both speech modalities
- Standardised, interpretable features (eGeMAPS)
- Robust classification with established algorithms
- Feature importance analysis for clinical interpretability
- Rigorous cross-validation for reliable estimates

---

*Estimated length: 4-5 pages*
