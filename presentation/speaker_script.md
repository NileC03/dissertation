# Presentation Speaker Script
**Duration:** ~15 minutes (12-13 min talk + 2-3 min buffer)  
**Tip:** Practice with a timer. Speak slower than feels natural — nerves speed you up.

---

## Slide 1: Title (~30 seconds)

*[Take a breath. Don't rush the opening.]*

"Good morning/afternoon everyone. My name is Nile, and my dissertation is titled 'Identifying Depression Through Speech' — specifically, a comparative analysis of acoustic features in read and spontaneous speech.

The short version: I wanted to find out whether the *way* we collect speech changes what we can detect about depression — and it turns out, it really does."

---

## Slide 2: Why This Matters (~2 minutes)

"So, why speech and depression?

Depression affects over 280 million people worldwide. In the UK alone, 1 in 6 adults experience depression or anxiety in any given week. That's an enormous public health challenge.

But here's the problem with how we currently diagnose it: it relies almost entirely on self-report — questionnaires, clinical interviews. And these are subjective. Studies have shown inter-rater reliability for depression subtypes can be as low as 0.28 kappa, which is barely above chance agreement.

On top of that, many people simply don't have access to specialist care. There are waiting lists, stigma, geographic barriers.

So the question becomes: is there a more objective, accessible way to screen for depression?

And that's where speech comes in. Speech is something we produce naturally, every day. It can be recorded non-invasively, remotely — even over a phone call. No specialist equipment needed. And crucially, there's decades of clinical evidence showing that depression changes how people speak — slower tempo, flatter pitch, more pauses. The question is whether we can measure those changes reliably enough to be clinically useful."

---

## Slide 3: The Research Gap (~1.5 minutes)

"Now, there *is* existing work in this area. Deep learning models have achieved over 80% accuracy at detecting depression from speech. Sounds impressive, right?

The problem is they're black boxes. They tell you *that* someone might be depressed, but not *why*. Not which aspect of their voice gave it away. And if you're a clinician, that's not very helpful — you need to understand the signal, not just the prediction.

There's also a second gap. Most studies use a single type of speech — either reading aloud or a clinical interview — but rarely both. No one has systematically compared whether the *type* of speech task changes which features are important.

So my research question is: which acoustic features are most predictive of depression, and how do they differ between read and spontaneous speech?

This is a question about *understanding*, not just accuracy."

---

## Slide 4: Approach Overview (~2 minutes)

"Here's the pipeline.

**Data** — I used the ANDROIDS corpus. This is a dataset of 118 Italian speakers, each with a clinical psychiatric diagnosis — not self-report, actual clinical assessment. Crucially, the same participants performed *both* a reading task and a spontaneous interview task. That's what enables a direct, controlled comparison.

**Features** — I extracted 88 acoustic features using the eGeMAPS feature set. These are standardised, interpretable features covering prosody — things like pitch and loudness — spectral properties, voice quality, and timing. Each feature has a clear acoustic meaning, which is important because I wanted to be able to explain what the model is picking up on.

**Models** — I deliberately chose Support Vector Machines and Random Forests over deep learning. The goal was interpretability. I wanted to know *which* features matter, not just maximise a number on a leaderboard. Random Forests give you built-in feature importance rankings, which turned out to be the most interesting part of the whole project."

---

## Slide 5: The Headline Result (~2 minutes)

"So here's the headline result.

When classifying depression from reading speech, the best model achieved 72.3% accuracy. Not bad, but not clinically useful on its own.

From interview speech — same participants, same features, same model — **87.1% accuracy**.

That's a 15 percentage point improvement, and it's statistically significant with a p-value of 0.0055. This wasn't a fluke — it was consistent across all five cross-validation folds.

And here's what's particularly noteworthy: that 87.1% actually *beats* the best reported deep learning result on the same corpus, which was 81.6%. So an interpretable model, with handcrafted features, outperformed a black-box neural network.

That tells us something important: for this task, the right *features* matter more than the model complexity."

---

## Slide 6: Feature Divergence (~1.5 minutes)

"But the accuracy gap isn't even the most interesting finding. This is.

When I looked at the top 10 most important features for each task, only *one* feature appeared in both lists. One out of ten.

Reading speech relies on spectral slopes and MFCCs — these are essentially static properties of the voice signal. They tell you about the overall *quality* of the voice.

Interview speech relies on variability measures and temporal dynamics. These capture how the voice *changes over time*.

So it's not just that interview gives you better accuracy — it's giving you access to *qualitatively different information*. The two tasks are measuring different aspects of how depression manifests in speech. That has real implications for how we design screening tools."

---

## Slide 7: The Variability Finding (~1.5 minutes)

"Let me drill into this because I think it's the most important contribution.

For interview speech, 7 of the top 10 features are variability measures. The top three are spectral flux variability, Hammarberg index variability, and pause duration variability.

For reading, only 2 of 10 are variability measures.

What does this mean clinically? Clinicians have long described depressed speech as 'flat' or 'monotonous'. What the data is showing is that this flatness isn't just about pitch being lower — it's about the *dynamic range being compressed*. Depressed speakers don't modulate their voice as much over time. Their spectral flux doesn't vary as much. Their pauses are more uniform. Their voice quality stays more constant.

And you can only see this in spontaneous speech, because reading imposes its own rhythm through punctuation and sentence structure. The variability that depression suppresses is the *natural* modulation of unscripted conversation."

---

## Slide 8: Why Interview Works Better (~1.5 minutes)

"So why does interview speech capture these markers better? The clinical literature points to three mechanisms.

First, **cognitive load**. Spontaneous speech requires real-time planning — you're retrieving words, constructing sentences, monitoring what you're saying. Depression impairs executive function, and that manifests as hesitations, longer pauses, reduced fluency. Reading bypasses most of this because the content is provided for you.

Second, **emotional engagement**. Clinical interviews ask about mood, relationships, daily functioning — emotionally loaded topics. Depression specifically alters emotional expression, but you can only see that when emotions are actually being engaged. Reading a neutral passage doesn't trigger this.

Third, **prosodic freedom**. When you read aloud, your intonation is partly determined by punctuation — you go up at a question mark, you pause at a full stop. Conversation gives you full freedom over your prosody, and that freedom is exactly what depression compresses.

Interview speech captures all three channels. Reading suppresses them. That's why the gap is 15 percentage points."

---

## Slide 9: Implications (~1 minute)

"So what does this mean in practice?

For clinicians: task selection matters more than algorithm choice. If you're building a screening tool, use spontaneous speech, and measure *variability* — not just average pitch or average loudness.

For researchers: be careful about generalising feature importance across speech tasks. Saying 'MFCCs are the best features for depression detection' might only be true for reading speech. Single-task studies may be missing important markers entirely.

For system design: if you're building an app or a telehealth tool, elicit spontaneous speech. Ask open-ended questions. And prioritise temporal dynamics in your feature engineering."

---

## Slide 10: Limitations (~1 minute)

"I want to be upfront about the limitations.

The most serious one: this is Italian speech only. The ANDROIDS corpus was the only publicly available dataset where the same speakers performed both tasks with clinical diagnoses. Whether these features transfer to English or other languages is an open question — prosodic patterns can be language-dependent.

The sample size is modest — 118 speakers. That said, the results were statistically significant and stable across cross-validation folds.

On the moderate side: we only had binary labels — depressed or not — so we can't say anything about severity. And the gender split was 72% female, with women being misclassified slightly more often, which suggests there may be gender-specific patterns worth investigating.

The key takeaway: cross-corpus validation across languages and populations is essential before any of this could be used clinically."

---

## Slide 11: Conclusion (~1 minute)

"So to wrap up.

The core finding is this: spontaneous speech captures depression markers that reading misses — specifically, the reduced dynamic modulation that clinicians call 'flat affect.'

Four contributions. One: we quantified the task effect — 15 percentage points, statistically significant. Two: we showed that feature importance is task-specific, with only one feature in common between the top ten lists. Three: we demonstrated that interpretable methods can match or exceed deep learning accuracy. And four: we identified variability as the dominant signal in spontaneous speech — 7 of the top 10 features.

Thank you."

---

## Slide 12: Questions

*[Deep breath. You know this material better than anyone in the room.]*

**If you need a moment to think:** "That's a great question — let me think about that for a second."

**Key numbers to keep in your head:**
- 87.1% vs 72.3% (p = 0.0055)
- 1/10 feature overlap
- 7/10 variability measures for interview
- 118 speakers, 88 features, eGeMAPS
- Beats prior DL at 81.6%

---

## Total Timing Guide

| Section | Slides | Target Time |
|---------|--------|-------------|
| Setup | 1-3 | ~4 minutes |
| Results | 4-7 | ~7 minutes |
| Interpretation | 8-10 | ~3.5 minutes |
| Wrap-up | 11-12 | ~1.5 minutes |
| **Total** | | **~15 minutes** |

---

*Script created: March 14, 2026*
