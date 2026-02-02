#!/usr/bin/env python3
"""
ML Analysis Script - Baseline classifiers and feature importance
(Simplified - using RF and permutation importance instead of SHAP)
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score, cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix
from sklearn.inspection import permutation_importance
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Create results directory
import os
os.makedirs('results', exist_ok=True)
os.makedirs('figures', exist_ok=True)

print("="*60)
print("DEPRESSION DETECTION ANALYSIS")
print("="*60)

# Load data
df = pd.read_csv('features/all_features.csv')
print(f"\nLoaded {len(df)} samples with {len(df.columns)} columns")

# Separate features and labels
metadata_cols = ['filename', 'speaker_id', 'condition', 'gender', 'age', 'education', 'label', 'task', 'depression']
feature_cols = [c for c in df.columns if c not in metadata_cols]
print(f"Features: {len(feature_cols)}")

# Analysis for each task
results = {}

for task in ['reading', 'interview']:
    print(f"\n{'='*60}")
    print(f"TASK: {task.upper()}")
    print("="*60)
    
    task_df = df[df['task'] == task].copy()
    X = task_df[feature_cols].values
    y = task_df['depression'].values
    
    print(f"Samples: {len(X)} (HC: {sum(y==0)}, PT: {sum(y==1)})")
    
    # Cross-validation setup
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    # SVM
    svm_pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('svm', SVC(kernel='rbf', C=1.0, random_state=42))
    ])
    svm_scores = cross_val_score(svm_pipe, X, y, cv=cv, scoring='accuracy')
    svm_f1 = cross_val_score(svm_pipe, X, y, cv=cv, scoring='f1')
    print(f"\nSVM:")
    print(f"  Accuracy: {svm_scores.mean():.1%} (+/- {svm_scores.std()*2:.1%})")
    print(f"  F1 Score: {svm_f1.mean():.2f} (+/- {svm_f1.std()*2:.2f})")
    
    # Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, max_depth=10)
    rf_scores = cross_val_score(rf, X, y, cv=cv, scoring='accuracy')
    rf_f1 = cross_val_score(rf, X, y, cv=cv, scoring='f1')
    print(f"\nRandom Forest:")
    print(f"  Accuracy: {rf_scores.mean():.1%} (+/- {rf_scores.std()*2:.1%})")
    print(f"  F1 Score: {rf_f1.mean():.2f} (+/- {rf_f1.std()*2:.2f})")
    
    # Train RF on full data for feature importance
    rf.fit(X, y)
    
    # Feature importance (RF built-in - Gini importance)
    rf_importance = pd.DataFrame({
        'feature': feature_cols,
        'importance': rf.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\nTop 10 Features (Gini Importance):")
    for idx, row in rf_importance.head(10).iterrows():
        rank = rf_importance.index.get_loc(idx) + 1
        print(f"  {rank:2d}. {row['feature'][:50]}: {row['importance']:.4f}")
    
    # Permutation importance (more reliable)
    print(f"\nCalculating permutation importance...")
    perm_result = permutation_importance(rf, X, y, n_repeats=10, random_state=42, n_jobs=-1)
    perm_importance = pd.DataFrame({
        'feature': feature_cols,
        'importance': perm_result.importances_mean,
        'std': perm_result.importances_std
    }).sort_values('importance', ascending=False)
    
    print(f"\nTop 10 Features (Permutation Importance):")
    for idx, row in perm_importance.head(10).iterrows():
        rank = perm_importance.index.get_loc(idx) + 1
        print(f"  {rank:2d}. {row['feature'][:50]}: {row['importance']:.4f}")
    
    # Save results
    results[task] = {
        'svm_acc': svm_scores.mean(),
        'svm_std': svm_scores.std(),
        'svm_f1': svm_f1.mean(),
        'rf_acc': rf_scores.mean(),
        'rf_std': rf_scores.std(),
        'rf_f1': rf_f1.mean(),
        'gini_importance': rf_importance,
        'perm_importance': perm_importance
    }
    
    # Save to CSV
    rf_importance.to_csv(f'results/{task}_gini_importance.csv', index=False)
    perm_importance.to_csv(f'results/{task}_perm_importance.csv', index=False)
    
    # Create feature importance plot
    fig, ax = plt.subplots(figsize=(12, 8))
    top20 = perm_importance.head(20)
    bars = ax.barh(range(len(top20)), top20['importance'].values)
    ax.set_yticks(range(len(top20)))
    ax.set_yticklabels([f[:40] for f in top20['feature'].values])
    ax.invert_yaxis()
    ax.set_xlabel('Permutation Importance')
    ax.set_title(f'Top 20 Features - {task.title()} Task')
    plt.tight_layout()
    plt.savefig(f'figures/{task}_feature_importance.png', dpi=150)
    plt.close()

# Summary comparison
print(f"\n{'='*60}")
print("SUMMARY COMPARISON")
print("="*60)
print(f"\n{'Task':<12} {'SVM Acc':<15} {'RF Acc':<15} {'RF F1':<10}")
print("-"*52)
for task in ['reading', 'interview']:
    r = results[task]
    print(f"{task:<12} {r['svm_acc']:.1%} +/- {r['svm_std']*2:.1%}    {r['rf_acc']:.1%} +/- {r['rf_std']*2:.1%}    {r['rf_f1']:.2f}")

# Compare top features between tasks
print(f"\n{'='*60}")
print("TOP 5 FEATURES COMPARISON (Permutation Importance)")
print("="*60)
print(f"\n{'Rank':<6}{'Reading Task':<40}{'Interview Task':<40}")
print("-"*86)
read_top = results['reading']['perm_importance'].head(5)['feature'].tolist()
int_top = results['interview']['perm_importance'].head(5)['feature'].tolist()
for i in range(5):
    r = read_top[i][:38] if i < len(read_top) else ""
    t = int_top[i][:38] if i < len(int_top) else ""
    print(f"{i+1:<6}{r:<40}{t:<40}")

# Check overlap in top features
read_top10 = set(results['reading']['perm_importance'].head(10)['feature'])
int_top10 = set(results['interview']['perm_importance'].head(10)['feature'])
overlap = read_top10 & int_top10
print(f"\nOverlap in top 10 features: {len(overlap)} features")
if overlap:
    print("Shared features:", list(overlap)[:5])

# Save summary
summary_df = pd.DataFrame([{
    'task': task,
    'svm_accuracy': results[task]['svm_acc'],
    'svm_f1': results[task]['svm_f1'],
    'rf_accuracy': results[task]['rf_acc'],
    'rf_f1': results[task]['rf_f1'],
} for task in ['reading', 'interview']])
summary_df.to_csv('results/summary.csv', index=False)

print(f"\n✅ Analysis complete!")
print(f"Results saved to: results/")
print(f"Figures saved to: figures/")
