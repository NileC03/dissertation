# Dissertation Project Plan
## "Identifying Depression Through Speech: A Feature Importance Analysis"

**Student:** Nile  
**University:** University of Glasgow  
**Deadline:** ~2 months (early April 2026)  
**Target:** Complete 1 week early

---

## Research Question

> "Which acoustic features of speech are most predictive of depression, and how do they differ between read and spontaneous speech?"

---

## Timeline Overview

| Week | Dates | Phase | Key Deliverables |
|------|-------|-------|------------------|
| 1 | Feb 2-8 | Foundation | Data downloaded, background drafted |
| 2 | Feb 9-15 | Technical Setup | Feature extraction pipeline working |
| 3 | Feb 16-22 | Analysis I | Baseline models, initial results |
| 4 | Feb 23-Mar 1 | Analysis II | Feature importance, comparison |
| 5 | Mar 2-8 | Writing I | Methodology, Results drafted |
| 6 | Mar 9-15 | Writing II | Analysis/Discussion drafted |
| 7 | Mar 16-22 | Integration | Full draft assembled |
| 8 | Mar 23-29 | Polish | Final edits, formatting |
| Buffer | Mar 30+ | Contingency | Presentation prep |

---

## Detailed Task Breakdown

### Week 1: Foundation (Current)
- [x] Literature review notes
- [x] Thesis summary (Tao PhD)
- [x] Dataset summaries (DAIC-WOZ, ANDROIDS)
- [x] Research angle decided
- [x] Advisor approval
- [ ] ANDROIDS corpus downloaded
- [ ] Data structure documented
- [x] Background chapter drafted

### Week 2: Technical Setup
- [ ] OpenSMILE installed and configured
- [ ] Feature extraction script working
- [ ] All audio files processed
- [ ] Features saved to CSV/pickle
- [ ] Data preprocessing pipeline
- [ ] Train/test split following Tao's protocol

### Week 3: Analysis I
- [ ] Baseline SVM classifier
- [ ] Baseline Random Forest classifier
- [ ] Cross-validation setup (5-fold, speaker-independent)
- [ ] Initial accuracy metrics
- [ ] Read vs spontaneous comparison (basic)

### Week 4: Analysis II
- [ ] SHAP value analysis
- [ ] Permutation importance
- [ ] Feature ranking (read task)
- [ ] Feature ranking (spontaneous task)
- [ ] Statistical significance tests
- [ ] Visualisations (feature importance plots)

### Week 5: Writing I
- [ ] Methodology chapter complete
- [ ] Results chapter drafted
- [ ] All figures generated
- [ ] Tables formatted

### Week 6: Writing II
- [ ] Analysis/Discussion chapter
- [ ] Critical evaluation
- [ ] Limitations section
- [ ] Future work section

### Week 7: Integration
- [ ] Introduction finalised
- [ ] Abstract written
- [ ] All chapters integrated
- [ ] References complete
- [ ] Formatting checked

### Week 8: Polish
- [ ] Proofreading
- [ ] Advisor review incorporated
- [ ] Final formatting
- [ ] PDF generated
- [ ] Submission preparation

---

## Technical Stack

### Data
- **Corpus:** ANDROIDS (118 participants, Italian)
- **Tasks:** Read speech + Interview (spontaneous)
- **Labels:** Binary (depressed vs control, psychiatric diagnosis)

### Tools
- **Feature extraction:** OpenSMILE
- **Analysis:** Python (scikit-learn, SHAP, pandas)
- **Statistics:** scipy, statsmodels
- **Visualisation:** matplotlib, seaborn
- **Writing:** LaTeX (Glasgow template)

### Key Libraries
```
opensmile
scikit-learn
shap
pandas
numpy
scipy
matplotlib
seaborn
```

---

## Expected Outputs

### Quantitative
- Classification accuracy (read vs spontaneous)
- Feature importance rankings
- Statistical comparisons (t-tests, effect sizes)
- Cross-validation results

### Visualisations
- Feature importance bar charts
- SHAP summary plots
- Confusion matrices
- ROC curves
- Read vs spontaneous comparison plots

### Qualitative
- Discussion of which features matter and why
- Clinical implications
- Comparison with literature
- Limitations and future directions

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Data issues | Low | High | ANDROIDS is well-documented |
| Poor accuracy | Medium | Medium | Focus is on interpretability, not SOTA |
| Time overrun | Medium | High | 1-week buffer built in |
| Technical issues | Low | Medium | Use established tools (OpenSMILE) |
| Writer's block | Medium | Medium | Drafts started early |

---

## Communication Plan

- **Daily:** Progress logged in memory files
- **Major milestones:** Slack update to Nile
- **Weekly:** Summary of completed/upcoming tasks
- **Advisor:** Check-ins as needed (Nile to schedule)

---

## File Structure

```
dissertation/
├── data/
│   └── androids_corpus/      # Raw audio data
├── features/                  # Extracted features
├── models/                    # Trained models
├── results/                   # Analysis outputs
├── figures/                   # Generated plots
├── drafts/
│   └── sections/             # Chapter drafts
├── pdfs/                      # Readable documents
├── references/
│   └── dissertation.bib      # Bibliography
└── final/                     # Submission-ready files
```

---

## Success Criteria

**For an A grade:**
1. Clear, well-defined research question ✓
2. Rigorous methodology
3. Meaningful results (even if accuracy isn't SOTA)
4. Critical analysis and discussion
5. Well-written, properly formatted
6. Addresses limitations honestly
7. Places work in context of literature

---

*Plan created: February 2, 2026*  
*Last updated: February 2, 2026*
