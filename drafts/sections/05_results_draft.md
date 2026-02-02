# Chapter 5: Results

## 5.1 Classification Performance

### Overall Results

| Task | Algorithm | Accuracy | F1 Score |
|------|-----------|----------|----------|
| Reading | SVM | 71.5% ± 6.8% | 0.73 |
| Reading | Random Forest | 72.3% ± 7.2% | 0.74 |
| Interview | SVM | 82.0% ± 5.2% | 0.85 |
| Interview | Random Forest | **87.1%** ± 4.8% | **0.88** |

### Key Finding: Interview Outperforms Reading

The most striking result is the **~15 percentage point** performance gap between tasks:

- **Reading task:** 71.5–72.3% accuracy
- **Interview task:** 82.0–87.1% accuracy

This suggests spontaneous speech contains richer depression markers than controlled reading—likely because it captures a broader range of cognitive and emotional processes.

### Statistical Significance

| Metric | Value |
|--------|-------|
| Reading accuracy | 72.3% |
| Interview accuracy | 87.1% |
| Difference | 14.8% |
| Z-statistic | 2.774 |
| **P-value** | **0.0055** |

The p-value of 0.0055 is well below 0.05, meaning **interview speech is statistically significantly better than reading speech for depression detection**. This is not random chance.

---

## 5.2 Confusion Matrix Analysis

### Reading Task (Random Forest)

|  | Predicted HC | Predicted PT |
|--|--------------|--------------|
| **Actual HC** | 36 | 18 |
| **Actual PT** | 13 | 45 |

- False Positives (HC → PT): 18 (33% of healthy controls)
- False Negatives (PT → HC): 13 (22% of patients)
- Slight bias toward predicting depression

### Interview Task (Random Forest)

|  | Predicted HC | Predicted PT |
|--|--------------|--------------|
| **Actual HC** | 44 | 8 |
| **Actual PT** | 7 | 57 |

- False Positives: 8 (15% of healthy controls)
- False Negatives: 7 (11% of patients)
- **Much cleaner!** Errors balanced and substantially fewer overall

### Detailed Metrics

| Task | Class | Precision | Recall | F1 |
|------|-------|-----------|--------|-----|
| Reading | Healthy | 0.73 | 0.67 | 0.70 |
| Reading | Depressed | 0.71 | 0.78 | 0.74 |
| Interview | Healthy | 0.86 | 0.85 | 0.85 |
| Interview | Depressed | 0.88 | 0.89 | 0.88 |

---

## 5.3 Feature Importance Analysis

### Reading Task Top 10 Features

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | slopeUV0-500_amean | 0.050 |
| 2 | mfcc1_amean | 0.042 |
| 3 | mfcc1_stddevNorm | 0.041 |
| 4 | loudnessPeaksPerSec | 0.036 |
| 5 | StddevVoicedSegmentLengthSec | 0.032 |
| 6 | mfcc1V_amean | 0.029 |
| 7 | slopeV500-1500_stddevNorm | 0.027 |
| 8 | VoicedSegmentsPerSec | 0.026 |
| 9 | slopeV500-1500_amean | 0.025 |
| 10 | F2amplitudeLogRelF0_amean | 0.025 |

**Interpretation - Reading Task:**

- **Spectral Slope:** Top feature measures spectral tilt—flatter slopes indicate breathier, less energetic voice. Consistent with reduced vocal effort in depression.
- **MFCC1:** Captures overall spectral envelope shape. Both mean and variability in top 10 → depressed speech shows altered spectral characteristics.
- **Temporal Features:** Loudness peaks/sec and voiced segment variability indicate rhythm and prosodic differences.

---

### Interview Task Top 10 Features

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | spectralFluxV_stddevNorm | 0.069 |
| 2 | hammarbergIndexV_stddevNorm | 0.043 |
| 3 | StddevUnvoicedSegmentLength | 0.038 |
| 4 | MeanUnvoicedSegmentLength | 0.035 |
| 5 | alphaRatioV_stddevNorm | 0.035 |
| 6 | mfcc1V_amean | 0.033 |
| 7 | mfcc1V_stddevNorm | 0.032 |
| 8 | loudness_stddevRisingSlope | 0.030 |
| 9 | loudness_stddevFallingSlope | 0.026 |
| 10 | logRelF0-H1-A3_amean | 0.020 |

**Interpretation - Interview Task:**

- **Spectral Flux Variability:** Most important feature! Measures frame-to-frame spectral change variability. Reduced variability → monotonous speech.
- **Voice Quality Measures:** Hammarberg index and alpha ratio reflect breathiness and vocal strain. Their *variability* is key.
- **Pausing Behaviour:** Mean and stddev of unvoiced segment length (pauses/hesitations). Clinically meaningful: depression = psychomotor retardation.
- **Loudness Dynamics:** Variability of loudness slopes = prosodic expression. Reduced modulation = flat affect.

---

## 5.4 Task Comparison

### Feature Overlap

- **Shared:** Only mfcc1V (mean and variability)
- **Overlap:** 2-3 features in both top-10 lists

Different acoustic markers are salient depending on speech context.

### Dominant Feature Categories by Task

| Category | Reading | Interview |
|----------|---------|-----------|
| Spectral | Slope, MFCC1 | Flux, MFCC1V |
| Voice Quality | — | Hammarberg, Alpha ratio |
| Temporal | Voiced segments | Unvoiced segments (pauses) |
| Prosodic | Loudness peaks | Loudness dynamics |

### Clinical Interpretation

**Reading Task:** Reveals *voice production* characteristics (spectral slope, MFCC) and basic rhythm. Reflects physiological/motor aspects of depression.

**Interview Task:** Reveals *cognitive and affective* processes:
- Variable pausing → cognitive load, word-finding
- Reduced dynamics → flat affect
- Voice quality changes → emotional expression

Interview places greater demands on executive function, emotional regulation, language production—all impacted by depression. **This explains superior classification performance.**

---

## 5.5 Error Analysis

### Misclassification by Gender

| Task | Female Errors | Male Errors |
|------|---------------|-------------|
| Reading | 23 | 8 |
| Interview | 12 | 3 |

**Finding:** Female speakers more frequently misclassified in both tasks.

Possible explanations:
1. Sample imbalance in dataset
2. Acoustic features may capture depression differently across genders
3. Gender differences in depression expression

**Implication:** Future work should consider gender-specific models.

### Age Patterns

Mean age of misclassified samples (~47.9 years) similar to dataset mean—age not a significant confounding factor.

---

## 5.6 Learning Curve Analysis

Key observations:

- **No severe overfitting:** Training and validation scores converge
- **Potential for improvement:** Curves haven't fully plateaued—more data could help
- **Interview learns faster:** Achieves higher validation scores with same training data

---

## 5.7 Summary of Findings

1. **Interview speech is significantly more informative:** 87.1% vs 72.3% accuracy (p = 0.0055)

2. **Different features matter for each task:**
   - Reading: Spectral slope, MFCC, rhythm
   - Interview: Spectral dynamics, pausing, voice quality variability

3. **Variability measures are key for interview:** Most predictive features are *standard deviations*, not means—consistent with "flat" depressed speech

4. **Pausing behaviour is highly informative:** Unvoiced segment features rank prominently

5. **Confusion matrices show balanced errors for interview:** Both false positives and false negatives are low

6. **Gender bias in misclassification:** Female speakers more often misclassified—warrants investigation

7. **No overfitting detected:** Learning curves show good generalisation

These findings directly address the research question with interpretable insights into how depression manifests in speech.

---

*Estimated length: 6-8 pages*
