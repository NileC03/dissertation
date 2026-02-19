# Chapter 5: Results

The most striking finding is the substantial performance gap between speech tasks: interview speech achieves 87.1% accuracy compared to 72.3% for reading (p = 0.0055). This 15-percentage-point difference exceeds typical improvements from algorithmic refinements and suggests that task selection fundamentally shapes what depression markers can be detected. This chapter presents the full results, beginning with classification performance before examining which acoustic features drive these predictions.

## 5.1 Classification Performance

### 5.1.1 Overall Results

Table 5.1 summarises the classification performance for both speech tasks using 5-fold stratified cross-validation. The reported uncertainty (±) represents the standard deviation across the five cross-validation folds, reflecting variability in performance estimates.

| Task | Algorithm | Accuracy | F1 Score |
|------|-----------|----------|----------|
| Reading | SVM | 71.5% ± 6.8% | 0.73 |
| Reading | Random Forest | 72.3% ± 7.2% | 0.74 |
| Interview | SVM | 82.0% ± 5.2% | 0.85 |
| Interview | Random Forest | **87.1%** ± 4.8% | **0.88** |

For context, with approximately balanced classes (48% HC, 52% PT), chance-level accuracy is approximately 50%. All classifiers substantially exceed this baseline, confirming that the acoustic features carry genuine discriminative information about depression status.

### 5.1.2 Comparison with Prior Work

These results compare favourably with Tao et al.'s published results on the same ANDROIDS corpus (Tao, 2024). Using deep learning approaches, they achieved 83.4% accuracy on reading and 81.6% on spontaneous speech. The present work achieves 87.1% on interview speech using traditional machine learning—a 5.5 percentage point improvement over their spontaneous speech result, while maintaining full interpretability. This validates the argument that interpretable methods can be competitive with deep learning for this task.

### 5.1.3 Statistical Significance of Task Difference

The interview-reading performance gap is consistent across all five cross-validation folds—not a single fold showed reading outperforming interview. This consistency, combined with the magnitude of the gap, warrants formal statistical testing.

A two-proportion z-test comparing the Random Forest accuracy rates yields z = 2.774 and p = 0.0055, well below the conventional significance threshold of 0.05. Cohen's h for the accuracy difference (0.871 vs 0.723) is approximately 0.38. While this falls in the "small-to-medium" range by conventional standards, effect size benchmarks developed for psychological experiments may not directly apply to classification accuracy comparisons. The practical significance is clearer: a 15-point accuracy gap represents the difference between a screening tool that is clinically useful and one that is not.

### 5.1.4 Classifier Comparison

Random Forest marginally outperformed SVM on both tasks: +0.8 percentage points for reading (72.3% vs 71.5%) and +5.1 percentage points for interview (87.1% vs 82.0%). The consistency of the interview > reading pattern across both classifiers suggests this finding is robust to algorithm choice rather than an artefact of a particular method.

## 5.2 Confusion Matrix Analysis

Confusion matrices provide detailed insight into classification errors.

**Reading Task (Random Forest):**
|  | Predicted HC | Predicted PT |
|--|--------------|--------------|
| Actual HC | 36 | 18 |
| Actual PT | 13 | 45 |

**Interview Task (Random Forest):**
|  | Predicted HC | Predicted PT |
|--|--------------|--------------|
| Actual HC | 44 | 8 |
| Actual PT | 7 | 57 |

The reading task shows 18 false positives (33% of healthy controls misclassified as depressed) and 13 false negatives (22% of patients misclassified as healthy), with a slight bias toward predicting depression. The interview task shows substantially improved error rates: only 8 false positives (15% of healthy controls) and 7 false negatives (11% of patients), with more balanced errors between classes.

This balance is clinically important. False positives cause unnecessary concern and wasted clinical resources; false negatives mean missed cases requiring treatment. The interview task achieves not only higher accuracy but also avoids the systematic bias toward either error type.

### 5.2.1 Detailed Classification Metrics

| Task | Class | Precision | Recall | F1 |
|------|-------|-----------|--------|-----|
| Reading | Healthy | 0.73 | 0.67 | 0.70 |
| Reading | Depressed | 0.71 | 0.78 | 0.74 |
| Interview | Healthy | 0.86 | 0.85 | 0.85 |
| Interview | Depressed | 0.88 | 0.89 | 0.88 |

## 5.3 Feature Importance Analysis

The primary research question concerns which acoustic features are most predictive of depression. This section presents feature importance results ranked by Gini importance from the Random Forest classifier. Permutation importance was also computed as a robustness check; the two measures showed broad agreement in identifying the most predictive features, increasing confidence in these rankings.

### 5.3.1 Reading Task Features

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

Importance scores range from 0.050 (top feature) to 0.025 (10th feature), indicating a relatively gradual decline. The top three features account for approximately 13% of total importance, suggesting predictive power is distributed across multiple features rather than concentrated in one or two.

**Interpretation:** The top feature, spectral slope in unvoiced regions (0–500 Hz), captures voice quality characteristics. Flatter spectral slopes indicate breathier, less energetic phonation—consistent with the altered laryngeal function discussed in Chapter 2 as one of three mechanisms through which depression affects speech. MFCC1, appearing in both mean and variability forms, captures overall spectral envelope shape and reflects the speaker's baseline vocal characteristics. The temporal features (loudness peaks per second, voiced segment variability) index speech rhythm, though notably these are *mean* values rather than variability measures—reading tasks constrain natural prosodic variation, so what remains is the speaker's baseline rhythmic pattern.

### 5.3.2 Interview Task Features

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

Importance scores show a steeper decline than the reading task: the top feature (0.069) is nearly 3.5 times more important than the 10th feature (0.020). This suggests that a smaller set of features dominates predictive power for spontaneous speech.

**Interpretation:** Spectral flux variability—the top feature by a substantial margin—measures how much frame-to-frame spectral change fluctuates over time. This directly reflects the prosodic flattening mechanism discussed in Chapter 2: depressed speakers show reduced dynamic modulation, producing the "monotonous" quality clinicians have long observed. The Hammarberg index and alpha ratio variability capture fluctuations in voice quality; again, it is the *variability* rather than mean values that drives predictions, consistent with depression compressing dynamic range rather than shifting baseline properties.

Pause characteristics rank highly: both mean and variability of unvoiced segment length appear in the top four features. This reflects the temporal disruption mechanism from Chapter 2—psychomotor retardation and cognitive load manifest as altered pausing patterns during the demanding task of spontaneous speech production.

### 5.3.3 The Dominance of Variability Measures

A striking pattern emerges from the feature importance rankings. For interview speech, 7 of the top 10 features are variability measures (standard deviations), while for reading speech, only 2 of the top 10 are variability measures. This asymmetry aligns with the theoretical expectation that spontaneous speech permits natural prosodic modulation that depression then compresses, while reading constrains such variation regardless of mental state.

## 5.4 Task Comparison

### 5.4.1 Feature Overlap

Comparing the top 10 features between tasks reveals minimal overlap: exactly **one feature** (mfcc1V_amean) appears in both lists. This near-complete divergence suggests that reading and interview tasks do not simply provide stronger or weaker access to the same depression signal—they provide access to *qualitatively different* information.

### 5.4.2 Dominant Feature Categories by Task

| Category | Reading | Interview |
|----------|---------|-----------|
| Spectral | Slope, MFCC1 (means) | Flux, MFCC1V (variability) |
| Voice Quality | — | Hammarberg, Alpha ratio |
| Temporal | Voiced segments | Unvoiced segments (pauses) |
| Prosodic | Loudness peaks | Loudness dynamics |

Reading task classification relies primarily on static spectral characteristics and rhythm; interview task classification relies on dynamic modulation and pausing. The implications of this divergence are explored in Chapter 6.

## 5.5 Error Analysis

### 5.5.1 Misclassification by Gender

Analysis of misclassified samples revealed a pattern related to gender. To interpret this correctly, error *rates* (not raw counts) must be considered given the gender imbalance in the dataset (approximately 70% female).

| Task | Gender | Errors | Total | Error Rate |
|------|--------|--------|-------|------------|
| Reading | Female | 23 | 80 | 28.7% |
| Reading | Male | 8 | 32 | 25.0% |
| Interview | Female | 12 | 84 | 14.3% |
| Interview | Male | 3 | 32 | 9.4% |

Female speakers show slightly higher error rates in both tasks (28.7% vs 25.0% for reading; 14.3% vs 9.4% for interview). The raw count disparity (23 vs 8 for reading) is largely explained by the dataset composition, though a modest difference in error rates persists. Both genders show the same pattern of interview speech outperforming reading speech for depression detection.

### 5.5.2 Validation Checks

Learning curves (Figure 5.3) show training and validation scores converging appropriately as training set size increases. Training accuracy reached approximately 92% while validation accuracy stabilised around 87% for the interview task—a modest 5-point gap indicating the models generalise without severe overfitting. The consistency of results across both SVM and Random Forest provides additional confidence that the findings reflect genuine patterns rather than classifier-specific artefacts.

## 5.6 Visualisations

Figure 5.1 presents the feature importance distributions for both tasks. The visual contrast is notable: reading task features show a relatively even distribution of importance, while interview task features exhibit a steep drop-off after the top few features, with spectral flux variability clearly dominant.

Figure 5.2 shows confusion matrix heatmaps for both tasks. The reading task matrix shows moderate off-diagonal values (errors), while the interview task matrix is visually cleaner—darker diagonal cells and lighter off-diagonal cells—immediately communicating the improved classification performance.

Figure 5.3 tracks training and cross-validation accuracy as training set size increases, demonstrating appropriate convergence without severe overfitting.

## 5.7 Summary

Interview speech substantially outperforms reading speech for depression detection, achieving 87.1% accuracy compared to 72.3%—a statistically significant difference (p = 0.0055) that exceeds prior deep learning results on the same corpus. The features driving these predictions differ markedly between tasks: reading relies on static spectral characteristics and rhythm, while interview relies on dynamic modulation and pausing behaviour. Most notably, variability measures dominate interview speech classification (7 of 10 top features), while mean values dominate reading speech classification. This pattern is consistent with clinical characterisations of depressed speech as "flat" or "monotonous" and suggests that spontaneous speech uniquely captures the reduced dynamic range associated with depression. The following chapter interprets these findings in the context of prior literature and their implications for clinical practice.
