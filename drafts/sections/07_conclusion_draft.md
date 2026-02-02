# Chapter 7: Conclusion

## 7.1 Summary of Contributions

### Research Question Answered

> *"Which acoustic features of speech are most predictive of depression, and how do they differ between read and spontaneous speech?"*

**For Reading Speech:**
- Spectral slope features (0–500 Hz range)
- MFCC1 (mean and variability)
- Loudness peaks per second
- Voiced segment timing variability

**For Interview Speech:**
- Spectral flux variability
- Voice quality measures (Hammarberg index, alpha ratio)
- Pause characteristics (unvoiced segment duration/variability)
- Loudness dynamics (rising/falling slopes)

**Critical finding:** Variability measures dominate for spontaneous speech; mean values more important for reading.

---

### Main Findings

1. **Interview speech substantially outperforms reading** (87% vs 72% accuracy)—spontaneous speech captures richer depression markers.

2. **Different features are predictive in different contexts**—task selection is a critical design decision.

3. **Interpretable methods achieve competitive performance** with deep learning while providing clinical insight.

4. **Dynamic speech modulation is key**—most predictive interview features are variability measures, consistent with "flat" depressed speech.

5. **Pause behaviour is highly informative**—reflects psychomotor retardation and cognitive slowing.

---

### Practical Implications

**For developers of speech-based mental health tools:**
- Elicit spontaneous speech rather than scripted reading
- Prioritise variability features in models
- Consider pause analysis as efficient, interpretable marker

**For clinicians:**
- Speech characteristics may provide objective biomarkers complementing self-report
- Reduced vocal dynamics and altered pausing are observable indicators

---

## 7.2 Limitations Acknowledged

- Findings from single corpus (ANDROIDS, Italian speakers)—needs cross-linguistic validation
- Modest sample size (228 recordings)
- Binary classification only—graded severity remains future work

---

## 7.3 Final Remarks

Depression remains a significant public health challenge, with diagnosis relying on subjective self-report and clinical observation. Speech-based assessment offers objective, non-invasive markers for earlier detection and more frequent monitoring.

This study demonstrates such markers exist and can be identified with interpretable methods. The finding that **spontaneous speech reveals richer depression signatures than reading** has immediate practical implications. The identification of **variability measures—spectral dynamics, voice quality, pausing—as key features** provides clinically meaningful insights for both automated systems and clinical practice.

Future work should:
- Validate across diverse populations and languages
- Explore integration with clinical workflows
- Investigate whether speech markers track treatment response

**The ultimate goal:** A future where speech analysis contributes to early, accurate, and accessible mental health assessment.

---

*Estimated length: 1-2 pages*
