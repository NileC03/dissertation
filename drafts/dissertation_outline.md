# Dissertation Outline
## "Identifying Depression Through Speech"

*Structure based on A-grade Glasgow dissertations (FATA, IDA, GIST)*

---

## Front Matter (~2 pages)
- Title page
- Abstract (~250 words)
- Acknowledgements (optional)
- Table of Contents

---

## Chapter 1: Introduction (~3-4 pages)

### 1.1 Motivation
- Depression prevalence and impact (global, UK)
- Limitations of current diagnosis methods
- Why speech as a biomarker?
- The gap: interpretability over accuracy

### 1.2 Aims
- Identify predictive acoustic features
- Compare read vs spontaneous speech
- Provide interpretable analysis

### 1.3 Outline
- Brief summary of each chapter

---

## Chapter 2: Background (~8-10 pages)

### 2.1 Depression and Speech Production
- Cognitive effects of depression
- How cognition affects speech
- Observable speech changes

### 2.2 Acoustic Feature Definitions
- Fundamental frequency (F0)
- Energy/intensity measures
- MFCCs and spectral features
- Temporal features
- Voice quality measures
- Standard feature sets (eGeMAPS)

### 2.3 Machine Learning Approaches
- Traditional methods (SVM, Random Forest)
- Deep learning approaches
- Evaluation metrics

### 2.4 Related Work
- AVEC challenges and DAIC-WOZ
- The ANDROIDS corpus
- Feature importance studies
- The gap this work addresses

### 2.5 Summary

---

## Chapter 3: Design (~4-5 pages)

### 3.1 Research Methodology
- Experimental approach
- Justification for methods

### 3.2 Data Selection
- Why ANDROIDS corpus
- Dataset characteristics
- Ethical considerations

### 3.3 Feature Extraction
- OpenSMILE pipeline
- eGeMAPS feature set
- Processing steps

### 3.4 Classification Approach
- Choice of classifiers (SVM, RF)
- Cross-validation strategy
- Evaluation metrics

### 3.5 Feature Importance Analysis
- SHAP values
- Permutation importance
- Statistical tests

---

## Chapter 4: Implementation (~4-5 pages)

### 4.1 Development Environment
- Tools and libraries
- Hardware specifications

### 4.2 Data Processing Pipeline
- Audio preprocessing
- Feature extraction process
- Data storage format

### 4.3 Model Training
- Hyperparameter selection
- Cross-validation implementation
- Training procedure

### 4.4 Analysis Pipeline
- SHAP implementation
- Visualisation generation
- Statistical analysis

---

## Chapter 5: Evaluation (~6-8 pages)

### 5.1 Classification Results
- Overall accuracy
- Per-task performance
- Confusion matrices
- Comparison with baselines

### 5.2 Feature Importance Results
- Top features (read speech)
- Top features (spontaneous speech)
- SHAP summary plots
- Statistical significance

### 5.3 Task Comparison
- Read vs spontaneous accuracy
- Feature overlap analysis
- Task-specific markers

### 5.4 Summary of Findings

---

## Chapter 6: Discussion (~5-6 pages)

### 6.1 Interpretation of Results
- What the features tell us
- Clinical implications
- Scientific insights

### 6.2 Comparison with Literature
- Agreement with prior work
- Novel findings
- Discrepancies and explanations

### 6.3 Limitations
- Dataset limitations (language, size)
- Methodological limitations
- Generalisability concerns

### 6.4 Future Work
- Directions for extension
- Recommended improvements

---

## Chapter 7: Conclusion (~1-2 pages)

### 7.1 Summary of Contributions
- Main findings
- Research question answered

### 7.2 Final Remarks

---

## Back Matter

### References
- All cited works (BibTeX)

### Appendices (if needed)
- Full feature list
- Additional plots
- Code snippets

---

## Page Estimates

| Section | Pages |
|---------|-------|
| Front matter | 2 |
| Introduction | 3-4 |
| Background | 8-10 |
| Design | 4-5 |
| Implementation | 4-5 |
| Evaluation | 6-8 |
| Discussion | 5-6 |
| Conclusion | 1-2 |
| References | 2-3 |
| **Total** | **35-45** |

*Target: 40 pages (matches Glasgow limit)*

---

## Key Differences from Original Draft

| Before | After (A-grade style) |
|--------|----------------------|
| Motivation as chapter | Motivation as section in Introduction |
| Background = everything | Background = existing work + theory |
| No clear aims section | Explicit Aims + Research Question |
| No outline section | Chapter outline included |

---

*Updated: February 2, 2026*
*Based on: FATA, IDA, GIST dissertation structures*
