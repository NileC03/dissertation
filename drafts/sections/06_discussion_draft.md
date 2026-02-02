# Chapter 6: Discussion

## 6.1 Interpretation of Results

### Why Interview Speech Performs Better

The **15-percentage-point** accuracy advantage of interview over reading speech is the study's most significant finding. Several factors contribute:

**Cognitive Load:** Spontaneous speech requires concurrent planning, lexical retrieval, and articulation. Depression impairs executive function—these impairments manifest more clearly when cognitive demands are high. Reading minimises these demands.

**Emotional Engagement:** Interview questions about daily life, emotions, and future plans elicit affective content. Depression alters emotional processing—more apparent when discussing emotionally relevant topics.

**Pause Behaviour:** The prominence of pause features (unvoiced segment duration) reflects cognitive processes of word-finding and response formulation. Depressed individuals exhibit longer response latencies—patterns that cannot emerge in fluent reading.

**Natural Variability:** Spontaneous speech permits greater variation in prosody, timing, and voice quality. The importance of *standard deviation* features suggests reduced dynamic range is a key depression marker.

---

### The Importance of Variability Measures

Consistent finding: **variability measures (std devs) outperform means** for interview speech.

Top 3 interview features are ALL variability measures:
1. Spectral flux variability
2. Hammarberg index variability
3. Unvoiced segment length variability

This aligns with clinical characterisation of depressed speech as "flat" or "monotonous"—not necessarily different in *average* properties, but **reduced in dynamic modulation**.

---

### Clinical Implications

**Voice Quality Indicators:** Hammarberg index and alpha ratio capture spectral balance/breathiness. Voice quality assessment could be incorporated into clinical interviews.

**Timing Analysis:** Pause duration and variability are highly informative. Automated pause detection is technically straightforward—could integrate into telehealth platforms.

**Task Selection:** For speech-based screening, eliciting spontaneous speech (e.g., "describe a typical day") appears more diagnostic than reading tasks.

---

## 6.2 Comparison with Literature

### Alignment with Prior Work

✓ **Reduced Prosodic Variation:** Numerous studies report reduced pitch/loudness variation in depression. Our variability measures corroborate this.

✓ **Psychomotor Retardation:** Prominence of pause features reflects psychomotor slowing—core symptom of melancholic depression.

✓ **Voice Quality Changes:** Breathiness and reduced vocal intensity documented in depressed speech. Hammarberg index captures these.

### Novel Contributions

1. **Direct Task Comparison:** Few studies systematically compare same participants across tasks. 15-point accuracy difference quantifies task selection effect.

2. **Feature Interpretability Focus:** Most recent work prioritises accuracy via deep learning. We demonstrate interpretable methods achieve competitive performance with clinical insight.

3. **Task-Specific Markers:** Divergent feature profiles suggest different mechanisms underlie detection in each context.

### Comparison with AVEC Challenges

The 87% accuracy compares favourably with published AVEC results (typically 70-85%).

---

## 6.3 Limitations

### Dataset Limitations

| Limitation | Impact |
|------------|--------|
| **Sample Size** | 228 recordings modest. Larger samples enable more robust estimates. |
| **Language** | Italian only. Markers may differ across languages. Needs English/multilingual replication. |
| **Clinical Diversity** | No stratification by severity or subtype. Different markers may characterise mild vs severe. |
| **Cross-Sectional** | Single time point. Longitudinal data could reveal treatment tracking. |

### Methodological Limitations

- **Feature Set:** eGeMAPS may not capture all relevant information. Alternative representations could improve performance.
- **Classifier Selection:** Only SVM and RF evaluated. Other methods might perform better (at interpretability cost).
- **No Speaker Normalisation:** Individual voice differences may confound detection.
- **No Temporal Modelling:** Features aggregated over recordings. Time-varying models could capture conversation dynamics.

### Generalisability Concerns

Findings specific to ANDROIDS corpus. Requires validation for:
- Other languages
- Different recording equipment/environments
- Comorbid conditions
- Different demographics

---

## 6.4 Future Work

### Methodological Extensions

**SHAP Analysis:** Individual-level feature explanations. Could identify depression subtypes with distinct profiles.

**Cross-Corpus Validation:** Testing on DAIC-WOZ would assess generalisability. Transfer learning could adapt models.

**Multimodal Integration:** Combining acoustic + linguistic + visual features could improve detection.

### Clinical Applications

**Longitudinal Monitoring:** Track speech markers over time for objective treatment response measures.

**Screening Tools:** Integration with telehealth or smartphone apps for passive/active screening at scale.

**Personalised Baselines:** Individual baselines during healthy periods could improve sensitivity to subtle changes.

### Theoretical Investigations

**Mechanism Understanding:** Controlled studies manipulating cognitive load/emotional content could clarify why certain features are informative.

**Depression Subtypes:** Stratified analysis could reveal subtype-specific markers (melancholic vs atypical vs anxious).

---

## 6.5 Summary

This study demonstrates that interpretable acoustic features can effectively detect depression, with interview speech substantially outperforming reading tasks.

**Most predictive features:** Variability measures reflecting dynamic speech modulation—spectral flux, voice quality, pausing patterns.

**Despite limitations** (sample size, language specificity), findings provide clinically relevant insights and establish foundation for speech-based depression assessment tools.

---

*Estimated length: 5-6 pages*
