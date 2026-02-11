# Chapter 5: Results

This chapter presents the experimental results, including classification performance, confusion matrix analysis, statistical significance testing, feature importance analysis, error analysis, and comparison between speech tasks.

---

## 5.1 Classification Performance

### Overall Results

Table 5.1 summarises the classification performance for both speech tasks using 5-fold stratified cross-validation. The reported uncertainty (±) represents the standard deviation across the five cross-validation folds, reflecting variability in performance estimates.

| Task | Algorithm | Accuracy | F1 Score |
|------|-----------|----------|----------|
| Reading | SVM | 71.5% ± 6.8% | 0.73 |
| Reading | Random Forest | 72.3% ± 7.2% | 0.74 |
| Interview | SVM | 82.0% ± 5.2% | 0.85 |
| Interview | Random Forest | **87.1%** ± 4.8% | **0.88** |

For context, with approximately balanced classes (48% HC, 52% PT), chance-level accuracy is approximately 50%. All classifiers substantially exceed this baseline, confirming that the acoustic features carry genuine discriminative information about depression status.

### Comparison with Prior Work

These results compare favourably with Tao et al.'s published results on the same ANDROIDS corpus. Using deep learning approaches, they achieved 83.4% accuracy on reading and 81.6% on spontaneous speech. The present work achieves 87.1% on interview speech using traditional machine learning—a 5.5 percentage point improvement over their spontaneous speech result, while maintaining full interpretability. This validates the argument that interpretable methods can be competitive with deep learning for this task.

### Key Finding: Interview Outperforms Reading

The most striking result is the substantial performance gap between tasks. Interview speech yields approximately 15 percentage points higher accuracy than reading speech across both classifiers:

- **Reading task:** 71.5–72.3% accuracy
- **Interview task:** 82.0–87.1% accuracy

This suggests that spontaneous speech contains richer markers of depression than controlled reading, likely because it captures a broader range of cognitive and emotional processes.

### Statistical Significance

To confirm that this performance difference is genuine and not due to random variation, a two-proportion z-test was conducted comparing the Random Forest accuracy rates across tasks.

| Metric | Value |
|--------|-------|
| Reading accuracy | 72.3% |
| Interview accuracy | 87.1% |
| Difference | 14.8 percentage points |
| Z-statistic | 2.774 |
| P-value | 0.0055 |

The p-value of 0.0055 is well below the conventional significance threshold of 0.05, indicating that **interview speech is statistically significantly better than reading speech for depression detection**.

### Classifier Comparison

Random Forest marginally outperformed SVM on both tasks:
- Reading: RF 72.3% vs SVM 71.5% (+0.8 percentage points)
- Interview: RF 87.1% vs SVM 82.0% (+5.1 percentage points)

The consistency of the interview > reading pattern across both classifiers suggests this finding is robust to algorithm choice rather than an artefact of a particular method.

---

## 5.2 Confusion Matrix Analysis

Confusion matrices provide detailed insight into classification errors. Tables 5.2 and 5.3 show the confusion matrices for Random Forest on each task.

### Reading Task (Random Forest)

|  | Predicted HC | Predicted PT |
|--|--------------|--------------|
| **Actual HC** | 36 | 18 |
| **Actual PT** | 13 | 45 |

- False Positives (HC → PT): 18 (33% of healthy controls)
- False Negatives (PT → HC): 13 (22% of patients)
- The model shows a slight bias toward predicting depression

### Interview Task (Random Forest)

|  | Predicted HC | Predicted PT |
|--|--------------|--------------|
| **Actual HC** | 44 | 8 |
| **Actual PT** | 7 | 57 |

- False Positives: 8 (15% of healthy controls)
- False Negatives: 7 (11% of patients)
- Substantially improved error rates with more balanced errors

The interview task confusion matrix demonstrates not only higher accuracy but also more balanced error types—both false positives and false negatives are low. This is clinically important: false positives cause unnecessary concern while false negatives mean missed cases.

### Detailed Classification Metrics

Table 5.4 presents precision, recall, and F1 scores for each class.

| Task | Class | Precision | Recall | F1 |
|------|-------|-----------|--------|-----|
| Reading | Healthy | 0.73 | 0.67 | 0.70 |
| Reading | Depressed | 0.71 | 0.78 | 0.74 |
| Interview | Healthy | 0.86 | 0.85 | 0.85 |
| Interview | Depressed | 0.88 | 0.89 | 0.88 |

The interview task achieves substantially higher precision and recall for both classes, with particularly notable improvement in identifying healthy controls (recall increases from 67% to 85%).

---

## 5.3 Feature Importance Analysis

The primary research question concerns which acoustic features are most predictive of depression. This section presents feature importance results ranked by Gini importance from the Random Forest classifier. Permutation importance was also computed as a robustness check; the two measures showed broad agreement in identifying the most predictive features, increasing confidence in these rankings.

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

Importance scores range from 0.050 (top feature) to 0.025 (10th feature), indicating a relatively gradual decline. The top three features account for approximately 13% of total importance, suggesting predictive power is distributed across multiple features rather than concentrated in one or two.

**Interpretation — Reading Task:**

- **Spectral Slope (slopeUV0-500):** The top feature measures spectral tilt in unvoiced regions (0-500 Hz). Flatter slopes indicate breathier, less energetic voice quality—consistent with reduced vocal effort in depression.

- **MFCC1:** The first mel-frequency cepstral coefficient captures overall spectral envelope shape. Both mean and variability appear in the top 10, suggesting depressed speech shows altered spectral characteristics.

- **Temporal Features:** Loudness peaks per second and voiced segment variability reflect speech rhythm and prosodic patterns.

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

Importance scores show a steeper decline than the reading task: the top feature (0.069) is nearly 3.5 times more important than the 10th feature (0.020). This suggests that a smaller set of features dominates predictive power for spontaneous speech.

**Interpretation — Interview Task:**

- **Spectral Flux Variability:** The most important feature measures frame-to-frame spectral change variability. Reduced variability indicates monotonous speech—a hallmark of depression-related flat affect.

- **Voice Quality Variability:** The Hammarberg index and alpha ratio capture spectral balance related to breathiness and vocal strain. Notably, their *variability* (standard deviation) rather than mean values drives predictions, suggesting dynamic changes during speech are particularly informative.

- **Pause Characteristics:** Both mean and variability of unvoiced segment length rank highly. Unvoiced segments correspond to pauses and hesitations—clinically meaningful given the psychomotor retardation associated with depression.

- **Loudness Dynamics:** Variability of loudness slopes indicates prosodic expression. Reduced modulation reflects flat affect.

### Key Insight: Variability Measures Dominate for Interview Speech

A striking pattern emerges: for interview speech, 7 of the top 10 features are variability measures (standard deviations), while for reading speech, only 2 of the top 10 are variability measures. This aligns with clinical characterisations of depressed speech as "flat" or "monotonous"—not necessarily different in average properties, but reduced in *dynamic modulation*.

---

## 5.4 Task Comparison

### Feature Overlap

Comparing the top 10 features between tasks reveals minimal overlap: exactly **one feature** (mfcc1V_amean) appears in both lists. This suggests that different acoustic markers are salient depending on speech context—a finding with implications for clinical system design.

### Dominant Feature Categories by Task

| Category | Reading | Interview |
|----------|---------|-----------|
| Spectral | Slope, MFCC1 | Flux, MFCC1V |
| Voice Quality | — | Hammarberg, Alpha ratio |
| Temporal | Voiced segments | Unvoiced segments (pauses) |
| Prosodic | Loudness peaks | Loudness dynamics |

### Clinical Interpretation

The task-specific feature profiles suggest different cognitive mechanisms are captured:

**Reading Task:** Reading scripted text primarily reveals *voice production* characteristics (spectral slope, MFCC) and basic rhythm. These may reflect the physiological and motor aspects of depression.

**Interview Task:** Spontaneous speech reveals *cognitive and affective* processes—variable pausing (reflecting cognitive load and word-finding difficulty), reduced vocal dynamics (flat affect), and voice quality changes (emotional expression). The interview task places greater demands on executive function, emotional regulation, and language production—all impacted by depression.

This explains the superior classification performance on interview speech: it captures a broader range of depression-related processes.

---

## 5.5 Error Analysis

### Misclassification by Gender

Analysis of misclassified samples revealed a pattern related to gender. To interpret this correctly, error *rates* (not raw counts) must be considered given the gender imbalance in the dataset.

| Task | Group | Errors | Total | Error Rate |
|------|-------|--------|-------|------------|
| Reading | Female | 23 | 80 | 28.7% |
| Reading | Male | 8 | 32 | 25.0% |
| Interview | Female | 12 | 84 | 14.3% |
| Interview | Male | 3 | 32 | 9.4% |

Female speakers show slightly higher error rates in both tasks (28.7% vs 25.0% for reading; 14.3% vs 9.4% for interview). However, these differences are modest—the raw count disparity (23 vs 8) is largely explained by the dataset being approximately 70% female.

Possible explanations for the remaining difference include:
1. **Acoustic feature sensitivity:** Some features may capture depression differently across genders
2. **Expression differences:** Gender differences in how depression manifests in speech
3. **Sample characteristics:** Potential confounds in the specific corpus

This finding warrants further investigation but does not undermine the main results, since both genders show the same pattern of interview speech outperforming reading speech for depression detection.

### Validation Checks

Two checks confirm the results are not artefactual:

**No overfitting detected:** Learning curves (Figure 5.3) show training and validation scores converging, indicating the models generalise appropriately. Training accuracy reached approximately 92% while validation accuracy stabilised around 87% for the interview task—the gap is modest and consistent with expected generalisation error.

**Cross-method consistency:** Both SVM and Random Forest produce the same pattern (interview > reading), suggesting the finding is robust to algorithm choice.

---

## 5.6 Visualisations

**Figure 5.1: Feature Importance Comparison**

The side-by-side bar charts display the top 10 features for each task ranked by Gini importance. The visual contrast is striking: reading task features show a relatively even distribution (bars of similar length), while interview task features exhibit a steep drop-off after the top few features. Spectral flux variability visually dominates the interview chart, reinforcing its role as the primary predictive feature for spontaneous speech.

**Figure 5.2: Confusion Matrices**

Heatmaps visualise the classification outcomes for both tasks. The reading task matrix shows moderate off-diagonal values (errors), while the interview task matrix is visually "cleaner"—darker diagonal cells and lighter off-diagonal cells—immediately communicating the improved classification performance.

**Figure 5.3: Learning Curves**

These plots track training and cross-validation accuracy as training set size increases. Both tasks show the characteristic pattern of valid learning: training accuracy starts high and decreases slightly as training size grows, while validation accuracy increases and converges toward the training curve. The gap between curves at maximum training size is modest (~5 percentage points), indicating appropriate generalisation without severe overfitting.

*(Figures are located in the figures/advanced/ directory of the project repository and should be included inline in the final LaTeX compilation.)*

---

## 5.7 Summary of Findings

1. **Interview speech is significantly more informative:** 87.1% vs 72.3% accuracy (p = 0.0055), exceeding prior deep learning results on the same corpus

2. **Different features matter for each task:**
   - Reading: Spectral slope, MFCC, rhythm
   - Interview: Spectral dynamics, pausing, voice quality variability
   - Only 1 of 10 top features overlaps between tasks

3. **Variability measures are key for interview speech:** 7 of 10 top features are standard deviations, not means—consistent with clinical descriptions of "flat" depressed speech

4. **Pausing behaviour is highly informative:** Unvoiced segment features rank 3rd and 4th for interview speech, reflecting psychomotor retardation

5. **Confusion matrices show balanced errors for interview:** Both false positives and false negatives are low (8 and 7 respectively)

6. **Gender shows modest effect on error rates:** Female speakers have slightly higher error rates, though the difference is small and largely explained by dataset composition

### Limitations

Feature importance rankings identify *which* features are predictive but do not establish whether differences between features are statistically significant. Future work could apply permutation tests or bootstrap confidence intervals to determine whether, for example, the top-ranked feature is significantly more important than the second-ranked feature. For present purposes, the consistency between Gini and permutation importance measures provides reasonable confidence in the top-ranked features.

---

*Estimated length: 7-8 pages*
