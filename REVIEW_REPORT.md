# Dissertation Review Report - A Grade Assessment

## Overall Assessment: Strong A (A2-A3 range)

The dissertation is well-written, methodologically sound, and presents genuinely novel findings. It meets or exceeds A-grade criteria across all marking categories. Below are the specific issues that could be improved.

---

## Issues Found (by priority)

### HIGH PRIORITY (could affect grade)

**1. Chapter naming inconsistency with outline**
- Introduction says Chapter 3 is "Design" and Chapter 5 is "Evaluation"
- But the actual chapters are titled "Methodology" (Ch3) and "Results" (Ch5)
- Location: `01_introduction.tex`, lines ~35-48
- Impact: Examiner will notice the mismatch between the outline and actual chapter titles

**2. Missing figure reference for accuracy comparison**
- The results chapter references feature importance, confusion matrices, and learning curves
- But there's no standalone figure for the accuracy comparison bar chart, despite it being a key visual
- The accuracy comparison figure IS generated and used in the slides
- Location: `05_results.tex` — no `\ref{fig:accuracy-comparison}` exists
- Impact: Minor, but the most important result deserves its own figure

**3. "SHAP analysis" mentioned as "planned" in Future Work**
- Discussion says "The planned SHapley Additive exPlanations analysis would provide..."
- "Planned" implies it was supposed to be done but wasn't — an examiner might question this
- Location: `06_discussion.tex`, Future Work section
- Impact: Should be reworded from "planned" to "proposed" or "a natural extension would be"

### MEDIUM PRIORITY (polish items)

**4. Inconsistent em-dash formatting**
- Some places use `---` (correct LaTeX em dash)
- Some places use commas or semicolons where em dashes would be more consistent
- Several places have `--` (en dash) where `---` (em dash) seems intended
- Location: Throughout, but notably in `06_discussion.tex`

**5. Missing "et al." period in some citations**
- Some narrative citations write "Cummins et al.'s" correctly
- But should verify all narrative citations have proper formatting
- Location: Scattered

**6. Confusion matrix figure placement**
- The confusion matrices figure shows BOTH SVM and RF matrices for each task
- But the text discusses only the RF matrices (Tables 5.2 and 5.3)
- The figure shows 4 matrices but the text references 2
- Location: `05_results.tex`, Figure 5.2
- Impact: Slightly confusing but not a major issue

**7. Gini importance vs permutation importance**
- The code computes BOTH Gini and permutation importance
- The results chapter says "Permutation importance was also computed as a robustness check"
- But all tables show Gini importance values
- The text should clarify which is being presented in the tables
- Location: `05_results.tex`, Section 5.3

### LOW PRIORITY (minor polish)

**8. Abstract says "228 recordings from 118 speakers"**
- But methodology shows 112 reading + 116 interview = 228 total recordings
- 118 is the corpus total, but actual usable recordings came from fewer unique speakers (~70)
- This isn't wrong per se, but could be questioned
- Location: Abstract in `dissertation.tex`

**9. The word "importantly" appears multiple times**
- Academic writing style guides often flag this as a filler word
- Location: Throughout

**10. Conclusion repeats discussion content substantially**
- Some paragraphs are near-identical between Ch6 summary and Ch7
- This is normal for dissertations but could be tightened
- Impact: Very minor — expected overlap between discussion and conclusion

---

## Marking Criteria Assessment

### Analysis (15%) — A1/A2
✅ Research question is clear, focused, and well-motivated
✅ Literature survey is comprehensive (spans clinical, computational, and methodological)
✅ Approach is well-justified with clear rationale for every decision
✅ Gap in literature clearly identified

### Research Product (40%) — A2/A3
✅ Methodology is rigorous (stratified CV, two classifiers, significance testing)
✅ Novel finding (feature importance divergence between tasks)
✅ Code is clean and well-structured
✅ Results are scientifically sound
⚠️ Could be strengthened with SHAP analysis (acknowledged as future work)

### Evaluation (10%) — A2
✅ Statistical significance testing present
✅ Learning curves for overfitting assessment
✅ Error analysis by gender
✅ Comprehensive limitations section
✅ Strong future work suggestions
⚠️ "Planned SHAP analysis" wording could be improved

### Dissertation (20%) — A2/A3
✅ Well-organised with clear chapter flow
✅ Highly literate writing
✅ Bibliography is comprehensive
✅ Figures are properly generated
⚠️ Chapter title mismatch with outline (Issue #1)
⚠️ Minor formatting inconsistencies

### Code Quality — A2
✅ Clean, well-commented Python
✅ Reproducible pipeline (extract → analyse → advanced analysis)
✅ Proper use of sklearn pipelines and cross-validation
✅ Results saved systematically

---

## Summary of Recommended Changes

1. Fix chapter names in introduction outline (HIGH)
2. Consider adding accuracy comparison figure to results (HIGH)  
3. Reword "planned SHAP analysis" to "proposed" (HIGH)
4. Minor formatting consistency (MEDIUM)
5. Clarify which importance metric tables show (MEDIUM)

Total changes needed: minimal. The dissertation is submission-ready with these small fixes.
