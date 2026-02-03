# Chapter 3: Methodology

This chapter details the experimental methodology employed in this study, with emphasis on the reasoning behind each methodological choice.

---

## 3.1 Research Approach

This study adopts an empirical, quantitative approach to investigate which acoustic features of speech are most predictive of depression, with particular focus on comparing read versus spontaneous speech modalities.

### Experimental Design

The experimental pipeline follows four stages:

1. **Extract standardised acoustic features** from speech recordings
2. **Train classification models** to distinguish depressed from healthy individuals
3. **Analyse feature importance** to identify the most predictive acoustic markers
4. **Compare results across speech tasks** (reading versus interview)

This ordering is deliberate. Feature extraction must precede classification (obvious), but the decision to train classifiers *before* analysing features—rather than examining raw feature distributions first—reflects the research question's focus on *predictive* importance. A feature might differ statistically between groups yet contribute little to classification; conversely, features may be predictive through complex interactions invisible in univariate analysis. Training classifiers first identifies what actually matters for prediction.

### Why Traditional ML Over Deep Learning?

An alternative approach would use deep learning, which has achieved higher accuracy in recent work. This was deliberately rejected for two reasons.

First, the research question centres on *interpretability*—understanding which features contribute to detection—rather than maximising classification accuracy. Neural networks learn opaque representations that resist interpretation, defeating the study's purpose.

Second, the dataset size (228 recordings) is modest for deep learning, which typically requires thousands of samples to avoid overfitting. Traditional methods are better suited to this scale.

---

## 3.2 Dataset Selection

### The ANDROIDS Corpus

The ANDROIDS corpus was selected after considering alternatives including DAIC-WOZ (the field's primary benchmark) and E-DAIC. ANDROIDS offers three critical advantages for this research.

**Clinical labels**: Unlike DAIC-WOZ, which uses PHQ-8 self-report scores, ANDROIDS labels are based on psychiatric assessment. Self-report introduces noise from response biases and varying interpretation of questions; clinical diagnosis, while not perfect, provides more reliable ground truth.

**Dual speech tasks**: ANDROIDS includes both reading and interview tasks from the same participants—the only publicly available corpus with this property. This enables direct comparison of how depression manifests across speech modalities, which is central to the research question. DAIC-WOZ contains only spontaneous speech, making such comparison impossible.

**Public availability**: ANDROIDS is freely accessible, enabling reproducibility. DAIC-WOZ requires application and approval, limiting accessibility.

### Corpus Composition

The corpus contains 228 recordings from 118 speakers:

| Group | Reading Task | Interview Task |
|-------|--------------|----------------|
| Healthy Controls (HC) | 54 | 52 |
| Patients (PT) | 58 | 64 |
| **Total recordings** | 112 | 116 |

Note: The totals represent individual recordings, not unique participants. Some participants completed both tasks, meaning there is overlap between task groups. This has implications for cross-validation, discussed below.

### Class Balance

The class distribution is approximately balanced: 48% HC vs 52% PT for reading, and 45% HC vs 55% PT for interview. This mild imbalance does not warrant corrective measures (e.g., SMOTE, class weighting). Such techniques can introduce artefacts and are typically reserved for severe imbalance (e.g., 10:1 ratios). The natural class distribution was preserved.

### Speech Tasks

**Reading Task**: Participants read a standardised Italian text passage aloud. This provides controlled linguistic content, allowing acoustic analysis independent of spontaneous language production processes. The cognitive demands are relatively low: text is provided, eliminating lexical retrieval and syntactic planning.

**Interview Task**: Participants engaged in semi-structured interviews covering topics such as daily routines, emotional experiences, and future plans. This elicits naturalistic speech with variable linguistic content. The cognitive demands are substantially higher: speakers must simultaneously plan content, retrieve words, construct syntax, and monitor output.

The inclusion of both tasks is central to the research question. If the same features are predictive across both tasks, this suggests task-independent depression markers. If different features dominate, this reveals how task demands interact with depression's effects on speech.

### Ethical Considerations

The ANDROIDS corpus is publicly available for research purposes. All recordings were collected with informed consent, and data are anonymised (speaker IDs reveal no identifying information). No additional ethics approval was required for this secondary analysis of existing data.

---

## 3.3 Data Preprocessing

### Audio Format

The ANDROIDS corpus provides recordings in WAV format at 16kHz sampling rate, 16-bit depth. This format was used directly without resampling or format conversion. The 16kHz rate is standard for speech analysis and provides adequate frequency resolution for the features extracted.

### Preprocessing Steps

Minimal preprocessing was applied:

**No silence trimming**: The openSMILE eGeMAPS configuration handles variable-length input natively and is robust to leading/trailing silence. Manual trimming risks removing relevant speech-adjacent pauses.

**No amplitude normalisation**: Per-recording normalisation would obscure loudness differences between speakers that may be diagnostically relevant. The eGeMAPS loudness features are computed relative to within-recording dynamics, making cross-recording normalisation unnecessary.

**No noise reduction**: The corpus was recorded under controlled conditions with consistent equipment. Applying noise reduction risks introducing artefacts and removing signal components.

This minimal-preprocessing approach aligns with the goal of analysing natural speech characteristics rather than cleaned signals.

---

## 3.4 Feature Extraction

### The eGeMAPS Feature Set

The extended Geneva Minimalistic Acoustic Parameter Set (eGeMAPS) was selected over alternatives (ComParE's 6,000+ features, custom feature sets) for several reasons:

**Interpretability**: Each of the 88 features has a defined acoustic meaning. This is essential for a study asking *which* features matter—opaque or composite features would defeat the purpose.

**Standardisation**: eGeMAPS is widely used in affective computing, enabling comparison with published literature. Using a custom feature set would limit comparability.

**Dimensionality**: With 88 features and ~115 samples per task, the feature-to-sample ratio is manageable. ComParE's 6,000+ features would require aggressive dimensionality reduction, complicating interpretation.

**Design purpose**: eGeMAPS was specifically designed for affective computing and clinical speech analysis, not speech recognition. Features were selected based on their relevance to paralinguistic information.

### Feature Categories

The 88 features span five domains:

**Frequency (F0)**: Mean, standard deviation, percentiles (20th, 50th, 80th), and slope statistics for fundamental frequency, capturing pitch characteristics.

**Energy/Loudness**: Mean loudness, percentiles, peak rate, and rising/falling slope statistics, capturing vocal intensity dynamics.

**Spectral**: MFCCs 1-4 (mean and standard deviation), spectral flux (frame-to-frame change), formant frequencies and bandwidths, capturing vocal tract configuration and dynamics.

**Voice Quality**: Jitter (pitch perturbation), shimmer (amplitude perturbation), Hammarberg index, alpha ratio, capturing phonation characteristics.

**Temporal**: Voiced/unvoiced segment statistics (mean, standard deviation), speech rate proxies, capturing timing patterns.

### Extraction Process

Feature extraction used openSMILE (v2.5.0) via its Python bindings:

1. Load WAV file (16kHz, 16-bit, as provided in corpus)
2. Apply eGeMAPSv02 configuration
3. Compute frame-level features (25ms windows, 10ms shift)
4. Apply functionals (statistical summaries) over entire recording
5. Output: one 88-dimensional vector per recording

The "functionals" level—computing means, standard deviations, percentiles, and slopes over frame-level features—produces a fixed-length representation regardless of recording duration. This is appropriate for utterance-level classification but loses fine-grained temporal information. This trade-off was accepted because the research question concerns overall feature importance, not temporal dynamics.

---

## 3.5 Classification Methods

Two algorithms were employed: Support Vector Machine (SVM) and Random Forest. Both are well-established for speech-based classification and offer complementary strengths.

### Support Vector Machine

SVMs find the hyperplane that maximally separates classes in a transformed feature space. An RBF (radial basis function) kernel was used to capture nonlinear relationships.

**Configuration**:
- Kernel: RBF (Gaussian)
- Regularisation parameter (C): 1.0 (scikit-learn default)
- Gamma: 'scale' (1 / (n_features × variance), scikit-learn default)
- Feature standardisation: Applied (zero mean, unit variance)

**Justification for defaults**: The primary goal is feature importance analysis, not classification optimisation. Extensive hyperparameter tuning would risk overfitting to this specific dataset and would not improve feature importance estimates—which are derived from the Random Forest, not the SVM. The SVM serves as a complementary baseline to verify that patterns are not algorithm-specific.

Feature standardisation was applied because RBF kernels are sensitive to feature scales; without it, high-magnitude features would dominate regardless of their relevance.

### Random Forest

Random Forest constructs an ensemble of decision trees, each trained on a bootstrap sample with random feature subsets. Predictions are averaged across trees.

**Configuration**:
- Number of trees: 100
- Maximum depth: 10
- Minimum samples per leaf: 1 (default)
- Split criterion: Gini impurity
- Random state: 42 (fixed for reproducibility)

**Justification**:
- *100 trees*: Provides stable importance estimates. Beyond ~100 trees, importance rankings stabilise with diminishing returns (verified empirically by comparing 50, 100, and 200 trees on this data).
- *Maximum depth 10*: With ~115 samples per task and 88 features, unlimited depth risks overfitting. Depth 10 allows sufficient expressiveness while constraining complexity. This value was informed by the rule-of-thumb that tree depth should scale with log2(samples); log2(115) ≈ 7, so 10 provides some headroom.
- *Default minimum samples*: Not adjusted because depth limiting already controls overfitting.

No grid search or automated hyperparameter tuning was performed. This was a deliberate choice: the goal is stable feature importance estimation, not maximum classification accuracy. Tuning would optimise for accuracy at the risk of importance estimate instability.

---

## 3.6 Evaluation Strategy

### Cross-Validation Approach

All results use **5-fold stratified cross-validation**. This choice reflects several considerations:

**Why stratified**: Stratification ensures each fold maintains the same class distribution as the full dataset (~48% HC, ~52% PT). With mild imbalance and small sample sizes, unstratified splits could produce folds with skewed distributions.

**Why 5 folds**: Five folds balance bias and variance for datasets of this size. Fewer folds (e.g., 3) would mean training on too little data (~67%), inflating pessimistic bias. More folds (e.g., 10) would reduce test set size to ~12 samples, increasing variance in performance estimates. Five folds, yielding ~92 training and ~23 test samples per fold, is a standard choice for datasets in the 100-500 range.

**Speaker overlap consideration**: Some participants completed both reading and interview tasks, meaning the same speaker could appear in both datasets. Within each task, cross-validation splits are made at the recording level, not speaker level. This means the same speaker could theoretically appear in both train and test sets *across different tasks*, though not within a single task's evaluation.

Leave-one-speaker-out cross-validation was considered but rejected for two reasons: (1) it would yield only ~60 folds with high variance, and (2) the research question compares tasks separately, not jointly, making cross-task speaker leakage irrelevant. Within each task, recordings are independent (one recording per speaker per task), so speaker leakage does not occur.

### Evaluation Metrics

**Accuracy**: The proportion of correctly classified samples. Interpretable but can be misleading with imbalanced classes.

**F1 Score**: The harmonic mean of precision and recall. Given the mild class imbalance, F1 provides a balanced view of performance on both classes. Macro-averaged F1 (unweighted average across classes) is reported.

**Confusion matrices**: Provide detailed error breakdowns (false positives, false negatives), enabling analysis of error patterns.

### Statistical Significance Testing

To determine whether the accuracy difference between reading and interview tasks is statistically significant, a two-proportion z-test is applied. This tests whether two observed proportions (accuracies) could have arisen from populations with equal accuracy.

The null hypothesis is that reading and interview tasks yield equal classification accuracy. A p-value below 0.05 is taken as evidence to reject this null hypothesis, indicating a significant difference.

Note: The z-test assumes independent samples, which is a simplification given that some speakers appear in both tasks. However, the recordings themselves are distinct, and the highly significant p-value (0.0055) suggests the conclusion is robust to this assumption.

### Feature Importance Analysis

Two complementary importance measures are computed:

**Gini importance** (also called mean decrease in impurity): For each feature, sum the decrease in Gini impurity across all splits in all trees where that feature was used. Efficient to compute (falls out of training) but can be biased toward high-cardinality or continuous features.

**Permutation importance**: For each feature, randomly shuffle its values and measure the decrease in accuracy. This breaks the feature's relationship with the target, and the resulting accuracy drop indicates the feature's importance. More computationally expensive but provides a more reliable estimate of true predictive value.

Both measures are reported for comparison. Permutation importance (with 10 shuffles per feature) is treated as the primary measure due to its robustness.

---

## 3.7 Methodological Limitations

Several limitations of this methodology should be acknowledged:

**Single corpus**: Results are derived from ANDROIDS alone, an Italian-language corpus. Acoustic markers of depression may differ across languages due to prosodic and phonetic differences. Generalisation to English or other languages requires validation.

**Binary classification**: The healthy/depressed distinction collapses severity variation. The methodology cannot distinguish mild from severe depression, limiting clinical applicability.

**Recording-level analysis**: Each recording is treated as an independent sample, but recordings are produced by individuals with stable characteristics. Speaker-level effects are not explicitly modelled.

**No speaker normalisation**: Features are used as extracted, without normalising for individual baseline differences. This may confound speaker identity with depression status.

**Italian speech**: Features were extracted using language-independent acoustic analysis, but depression's interaction with language-specific prosodic patterns is not accounted for.

These limitations are revisited in the Discussion chapter.

---

## 3.8 Reproducibility

All code is available in the project repository (https://github.com/NileC03/dissertation):

- `extract_features.py`: Feature extraction pipeline
- `run_analysis.py`: Classification and importance analysis
- `advanced_analysis.py`: Statistical tests and visualisations

Random seeds are fixed for all stochastic processes (random_state=42 for scikit-learn) to ensure reproducibility. The ANDROIDS corpus is publicly available from its original authors.

---

## 3.9 Summary

This methodology enables systematic investigation of the research question through:

- A carefully selected corpus offering both speech modalities and clinical labels
- Standardised, interpretable features (eGeMAPS) with clear acoustic meanings
- Robust classification using established algorithms with justified configurations
- Feature importance analysis using permutation-based measures
- Rigorous cross-validation appropriate to the sample size
- Statistical testing to confirm significance of findings

The following chapter details the implementation of this methodology.

---

*Estimated length: 5-6 pages*
