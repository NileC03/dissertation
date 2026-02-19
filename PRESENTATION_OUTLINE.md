# Dissertation Presentation Outline
**Title:** Identifying Depression Through Speech  
**Duration:** 10-15 minutes  
**Author:** Nile

---

## Slide 1: Title
**Identifying Depression Through Speech:**  
*A Comparative Analysis of Acoustic Features in Read and Spontaneous Speech*

Nile  
University of Glasgow  
Level 4 Computer Science

---

## Slide 2: Why This Matters
**The Problem**

- Depression affects 280+ million people globally
- UK: 1 in 6 adults experience depression/anxiety weekly
- Diagnosis relies on self-report and clinical interviews
- Inter-rater reliability as low as 0.28 kappa for some subtypes
- Many people lack access to specialist care

**The Opportunity**

Speech can be recorded non-invasively, remotely, without specialist equipment

*[Visual: Simple infographic with depression stats]*

---

## Slide 3: The Research Gap

**What exists:**
- Deep learning models achieving 80%+ accuracy
- "Black box" predictions — high accuracy, no explanation

**What's missing:**
- *Which* acoustic features actually indicate depression?
- Does it matter *how* you collect speech?

**Research Question:**
> "Which acoustic features of speech are most predictive of depression, and how do they differ between read and spontaneous speech?"

---

## Slide 4: Approach Overview

**Data:** ANDROIDS corpus
- 118 Italian speakers (clinical diagnoses, not self-report)
- Same participants do BOTH reading AND interview tasks
- Enables direct comparison

**Features:** eGeMAPS (88 interpretable acoustic features)
- Prosody, spectral, voice quality, timing
- Each feature has a clear acoustic meaning

**Methods:** SVM + Random Forest
- Deliberately NOT deep learning
- Interpretability over maximum accuracy

*[Visual: Simple pipeline diagram]*

---

## Slide 5: The Headline Result

**Interview speech significantly outperforms reading**

| Task | Accuracy |
|------|----------|
| Reading | 72.3% |
| Interview | **87.1%** |

- Difference: **15 percentage points**
- Statistically significant: p = 0.0055
- Consistent across all 5 CV folds
- Beats prior deep learning on same corpus (81.6%)

*[Visual: Bar chart comparing the two]*

---

## Slide 6: But Here's What's Interesting...

**Different features predict depression in each task**

Of the top 10 features for each task:
- Only **1 feature overlaps**
- Reading relies on: spectral slopes, MFCCs (static properties)
- Interview relies on: variability measures (dynamic properties)

This isn't just "interview is better" — they capture **qualitatively different information**

*[Visual: Side-by-side top 5 features for each task]*

---

## Slide 7: The Variability Finding

**Interview speech: 7 of 10 top features are variability measures**

Top 3 interview features:
1. Spectral flux **variability**
2. Hammarberg index **variability** 
3. Pause duration **variability**

**Reading speech: Only 2 of 10 are variability measures**

**What this means:**
Depression doesn't just shift voice to a different register — it **compresses dynamic range**

The "flat" or "monotonous" quality clinicians describe = reduced modulation over time

*[Visual: Your feature importance comparison chart]*

---

## Slide 8: Why Interview Works Better

**Three mechanisms (from clinical literature):**

1. **Cognitive load** — Spontaneous speech requires planning, retrieval, monitoring. Depression impairs executive function → manifests in pauses, hesitations

2. **Emotional engagement** — Interview topics (mood, relationships) engage affect. Depression alters emotional expression → only visible when emotions are relevant

3. **Prosodic freedom** — Reading follows punctuation cadence. Conversation allows natural modulation → depression compresses this range

Interview captures all three channels. Reading suppresses them.

---

## Slide 9: Implications

**For clinical practice:**
- Task selection matters more than algorithm choice
- Spontaneous speech > reading for screening
- Measure variability, not just means

**For research:**
- Single-task studies may miss important markers
- Feature importance is task-contingent
- "MFCCs are best for depression" may only be true for reading

**For system design:**
- Elicit spontaneous speech (open-ended questions)
- Prioritise temporal dynamics over static summaries

---

## Slide 10: Limitations

**Most serious:**
- Italian speech only — features may not transfer to English
- Modest sample size (118 speakers)

**Moderate:**
- Binary labels (no severity information)
- Gender imbalance (72% female) — women misclassified slightly more often

**What this means:**
Cross-corpus validation essential before clinical deployment

---

## Slide 11: Conclusion

**One sentence:**
> Spontaneous speech captures depression markers that reading misses — specifically, the reduced dynamic modulation that clinicians call "flat affect."

**Contributions:**
1. Quantified the task effect (15 points, p=0.0055)
2. Showed features are task-specific (1/10 overlap)
3. Demonstrated interpretable methods match deep learning
4. Identified variability as the key signal for spontaneous speech

---

## Slide 12: Questions?

**Likely questions to prepare for:**

- "Why not use deep learning?" → Interpretability was the goal; we matched their accuracy anyway
- "Why Italian corpus?" → Only public corpus with both tasks from same speakers
- "Would this work in English?" → Unknown — cross-linguistic validation needed
- "What about severity prediction?" → Binary labels only; future work
- "Why Random Forest over other methods?" → Built-in feature importance; both classifiers showed same pattern

---

## Speaker Notes

**Timing guide:**
- Slides 1-3 (setup): ~3 minutes
- Slides 4-7 (results): ~5-6 minutes  
- Slides 8-10 (interpretation): ~3-4 minutes
- Slides 11-12 (wrap): ~1-2 minutes

**Key phrases to hit:**
- "15 percentage points — that's the difference between clinically useful and not"
- "Only 1 feature in common — qualitatively different information"
- "7 of 10 are variability measures — it's the dynamics, not the statics"
- "We matched deep learning accuracy while being able to explain why"

**Don't:**
- Read slides verbatim
- Apologise for limitations before they ask
- Rush the variability finding — it's your most interesting contribution

---

*Outline created: February 19, 2026*
