# Chapter 1: Introduction

## 1.1 Motivation

Depression affects over 280 million people globally, making it one of the leading causes of disability worldwide (WHO, 2024). In the United Kingdom alone, approximately one in six adults experiences depression or anxiety in any given week, with an estimated economic burden of £105 billion annually (McManus et al., 2016; OECD, 2018).

Despite its prevalence, depression remains significantly underdiagnosed and undertreated. Current diagnostic methods rely primarily on clinical interviews and self-report questionnaires such as the Patient Health Questionnaire (PHQ-9) (Kroenke et al., 2001). These approaches face several critical limitations. Diagnostic agreement between clinicians can be inconsistent, with inter-rater reliability as low as 0.28 kappa for certain depression subtypes (Regier et al., 2013). Patients may underreport symptoms due to stigma, lack of insight, or difficulty articulating their experiences. Clinical assessments require trained mental health professionals, limiting scalability and accessibility. And many individuals, particularly in underserved communities, lack access to specialist care entirely.

These limitations have motivated research into objective, scalable biomarkers for depression. Candidate biomarkers include physiological signals, facial expressions, gait patterns, and speech. Among these, *speech* offers particular advantages: it can be recorded non-invasively, requires no specialised equipment beyond a microphone, and can be collected remotely through telephone or smartphone applications. Crucially, depression affects cognitive processes that directly influence speech production—changes that are often involuntary and difficult to consciously mask (Cummins et al., 2015). This makes speech an attractive candidate for large-scale screening.

Recent advances in machine learning have enabled automatic detection of depression from speech with accuracy comparable to general practitioners (Tao, 2024). However, most research has focused on maximising classification accuracy, treating models as "black boxes." This raises a critical question: *which aspects of speech actually indicate depression?*

Understanding which acoustic features predict depression is essential for:

1. **Clinical utility:** Clinicians cannot act on "83% accuracy"—they need interpretable markers.
2. **Scientific understanding:** Identifying robust biomarkers advances our understanding of how depression manifests in behaviour.
3. **System design:** Knowing which features matter informs what data to collect and how to deploy screening tools.

This dissertation addresses this gap by systematically analysing which acoustic features are most predictive of depression, and how their importance differs between controlled (read) and naturalistic (spontaneous) speech.

## 1.2 Aims

This project aims to:

1. **Identify predictive features:** Determine which acoustic and prosodic features are most strongly associated with depression, using interpretable machine learning techniques.

2. **Compare speech tasks:** Analyse whether the same features predict depression in read speech (controlled phonetic content) versus spontaneous speech (natural conversation), and which task yields more reliable detection.

3. **Provide interpretable analysis:** Move beyond accuracy metrics to explain *why* models predict depression, using feature importance methods that identify which acoustic properties drive classification.

The research question guiding this work is:

> *Which acoustic features of speech are most predictive of depression, and how do they differ between read and spontaneous speech?*

## 1.3 Outline

This dissertation is structured as follows:

- **Chapter 2: Background** — Reviews the relationship between depression and speech production, formally defines acoustic features used in analysis, surveys machine learning approaches to depression detection, and discusses related work including the ANDROIDS corpus.

- **Chapter 3: Design** — Describes the experimental methodology, including data selection, feature extraction pipeline, classification approach, and feature importance analysis techniques.

- **Chapter 4: Implementation** — Details the technical implementation, including tools used, data processing pipeline, and experimental setup.

- **Chapter 5: Evaluation** — Presents classification results, feature importance rankings, and comparison between read and spontaneous speech tasks.

- **Chapter 6: Discussion** — Critically analyses findings, discusses limitations, compares results with existing literature, and considers clinical implications.

- **Chapter 7: Conclusion** — Summarises contributions and suggests directions for future work.
