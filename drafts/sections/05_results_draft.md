# Chapter 5: Results

## 5.1 Classification Performance

### Overall Results

| Task | Algorithm | Accuracy | F1 Score |
|------|-----------|----------|----------|
| Reading | SVM | 71.5% ± 6.8% | 0.73 |
| Reading | Random Forest | 72.3% ± 7.2% | 0.74 |
| Interview | SVM | 82.0% ± 5.2% | 0.85 |
| Interview | Random Forest | **87.0%** ± 4.8% | **0.88** |

### Key Finding: Interview Outperforms Reading

The most striking result is the **~15 percentage point** performance gap between tasks:

- **Reading task:** 71.5–72.3% accuracy
- **Interview task:** 82.0–87.0% accuracy

This suggests spontaneous speech contains richer depression markers than controlled reading—likely because it captures a broader range of cognitive and emotional processes.

### Classifier Comparison

Random Forest marginally outperformed SVM:
- Reading: RF 72.3% vs SVM 71.5% (+0.8%)
- Interview: RF 87.0% vs SVM 82.0% (+5.0%)

Larger advantage on interview data may reflect RF's ability to capture complex feature interactions in naturalistic speech.

---

## 5.2 Feature Importance Analysis

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

- **Spectral Slope Features:** Top feature (slopeUV0-500) measures spectral tilt in unvoiced regions. Reflects energy distribution—flatter slopes indicate breathier, less energetic voice. Consistent with reduced vocal effort in depression.

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

- **Spectral Flux Variability:** Most important feature! Measures frame-to-frame spectral change variability. Reduced variability → monotonous speech characteristic of depression.

- **Voice Quality Measures:** Hammarberg index and alpha ratio reflect breathiness and vocal strain. Their *variability* is key—dynamic voice quality changes during speech are informative.

- **Pausing Behaviour:** Mean and stddev of unvoiced segment length (pauses/hesitations). Clinically meaningful: depression associated with psychomotor retardation, altered speech timing.

- **Loudness Dynamics:** Variability of loudness slopes indicates prosodic expression. Reduced modulation = flat affect.

---

## 5.3 Task Comparison

### Feature Overlap

Comparing top 10 features reveals **limited overlap**:

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

## 5.4 Visualisations

Feature importance plots reveal:

- Reading task: importance more evenly distributed across features
- Interview task: steeper gradient—top feature (spectral flux variability) substantially more important than rest

*See: figures/reading_feature_importance.png, figures/interview_feature_importance.png*

---

## 5.5 Statistical Significance

Cross-validation standard deviations (~5-7%) indicate reasonably stable results. The **15-point gap** between tasks substantially exceeds uncertainty bounds → difference is genuine.

---

## 5.6 Summary of Findings

1. **Interview speech is more informative:** 87% vs 72% accuracy
2. **Different features matter for each task:**
   - Reading: Spectral slope, MFCC, rhythm
   - Interview: Spectral dynamics, pausing, voice quality variability
3. **Variability measures are key for interview:** Most predictive features are *standard deviations*, not means
4. **Pausing behaviour is highly informative:** Unvoiced segment features rank prominently
5. **Both classifiers perform well:** Random Forest slightly better, especially on interview

These findings directly address the research question with interpretable insights into how depression manifests in speech.

---

*Estimated length: 6-8 pages*
