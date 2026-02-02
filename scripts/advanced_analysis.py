#!/usr/bin/env python3
"""
Advanced Analysis Script
- Confusion matrices
- Statistical significance tests
- Learning curves
- Error analysis
- Additional visualisations
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_predict, learning_curve
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Create output directories
import os
os.makedirs('results/advanced', exist_ok=True)
os.makedirs('figures/advanced', exist_ok=True)

print("="*60)
print("ADVANCED ANALYSIS")
print("="*60)

# Load data
df = pd.read_csv('features/all_features.csv')
print(f"\nLoaded {len(df)} samples")

# Separate features and labels
metadata_cols = ['filename', 'speaker_id', 'condition', 'gender', 'age', 'education', 'label', 'task', 'depression']
feature_cols = [c for c in df.columns if c not in metadata_cols]

results = {}

for task in ['reading', 'interview']:
    print(f"\n{'='*60}")
    print(f"TASK: {task.upper()}")
    print("="*60)
    
    task_df = df[df['task'] == task].copy()
    X = task_df[feature_cols].values
    y = task_df['depression'].values
    filenames = task_df['filename'].values
    
    print(f"Samples: {len(X)} (HC: {sum(y==0)}, PT: {sum(y==1)})")
    
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    # ============================================
    # 1. CONFUSION MATRICES
    # ============================================
    print("\n--- Confusion Matrices ---")
    
    # SVM predictions
    svm_pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('svm', SVC(kernel='rbf', C=1.0, random_state=42))
    ])
    svm_preds = cross_val_predict(svm_pipe, X, y, cv=cv)
    svm_cm = confusion_matrix(y, svm_preds)
    
    # RF predictions
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1, max_depth=10)
    rf_preds = cross_val_predict(rf, X, y, cv=cv)
    rf_cm = confusion_matrix(y, rf_preds)
    
    print(f"SVM Confusion Matrix:\n{svm_cm}")
    print(f"RF Confusion Matrix:\n{rf_cm}")
    
    # Plot confusion matrices
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.heatmap(svm_cm, annot=True, fmt='d', cmap='Blues', ax=axes[0],
                xticklabels=['Healthy', 'Depressed'], yticklabels=['Healthy', 'Depressed'])
    axes[0].set_title(f'SVM - {task.title()} Task')
    axes[0].set_xlabel('Predicted')
    axes[0].set_ylabel('Actual')
    
    sns.heatmap(rf_cm, annot=True, fmt='d', cmap='Blues', ax=axes[1],
                xticklabels=['Healthy', 'Depressed'], yticklabels=['Healthy', 'Depressed'])
    axes[1].set_title(f'Random Forest - {task.title()} Task')
    axes[1].set_xlabel('Predicted')
    axes[1].set_ylabel('Actual')
    
    plt.tight_layout()
    plt.savefig(f'figures/advanced/{task}_confusion_matrices.png', dpi=150)
    plt.close()
    print(f"Saved: figures/advanced/{task}_confusion_matrices.png")
    
    # ============================================
    # 2. CLASSIFICATION REPORTS
    # ============================================
    print("\n--- Classification Reports ---")
    
    svm_report = classification_report(y, svm_preds, target_names=['Healthy', 'Depressed'], output_dict=True)
    rf_report = classification_report(y, rf_preds, target_names=['Healthy', 'Depressed'], output_dict=True)
    
    print("\nSVM Report:")
    print(classification_report(y, svm_preds, target_names=['Healthy', 'Depressed']))
    
    print("\nRF Report:")
    print(classification_report(y, rf_preds, target_names=['Healthy', 'Depressed']))
    
    # Save reports
    pd.DataFrame(svm_report).transpose().to_csv(f'results/advanced/{task}_svm_classification_report.csv')
    pd.DataFrame(rf_report).transpose().to_csv(f'results/advanced/{task}_rf_classification_report.csv')
    
    # ============================================
    # 3. ERROR ANALYSIS
    # ============================================
    print("\n--- Error Analysis ---")
    
    # Find misclassified samples
    rf_errors = task_df[rf_preds != y].copy()
    rf_errors['predicted'] = rf_preds[rf_preds != y]
    rf_errors['actual'] = y[rf_preds != y]
    rf_errors['error_type'] = rf_errors.apply(
        lambda x: 'False Positive' if x['predicted'] == 1 else 'False Negative', axis=1
    )
    
    print(f"Total misclassified: {len(rf_errors)}")
    print(f"False Positives (HC predicted as PT): {sum(rf_errors['error_type'] == 'False Positive')}")
    print(f"False Negatives (PT predicted as HC): {sum(rf_errors['error_type'] == 'False Negative')}")
    
    # Save error analysis
    rf_errors[['filename', 'speaker_id', 'gender', 'age', 'actual', 'predicted', 'error_type']].to_csv(
        f'results/advanced/{task}_misclassified_samples.csv', index=False
    )
    
    # Analyze patterns in errors
    if len(rf_errors) > 0:
        print("\nError patterns:")
        print(f"  Gender distribution in errors: {rf_errors['gender'].value_counts().to_dict()}")
        if rf_errors['age'].notna().any():
            print(f"  Mean age of misclassified: {rf_errors['age'].mean():.1f}")
    
    # ============================================
    # 4. LEARNING CURVES
    # ============================================
    print("\n--- Learning Curves ---")
    
    train_sizes = np.linspace(0.2, 1.0, 5)
    
    # RF learning curve
    train_sizes_abs, train_scores, test_scores = learning_curve(
        rf, X, y, cv=cv, n_jobs=-1, train_sizes=train_sizes, scoring='accuracy'
    )
    
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)
    test_std = np.std(test_scores, axis=1)
    
    plt.figure(figsize=(10, 6))
    plt.fill_between(train_sizes_abs, train_mean - train_std, train_mean + train_std, alpha=0.1, color='blue')
    plt.fill_between(train_sizes_abs, test_mean - test_std, test_mean + test_std, alpha=0.1, color='orange')
    plt.plot(train_sizes_abs, train_mean, 'o-', color='blue', label='Training score')
    plt.plot(train_sizes_abs, test_mean, 'o-', color='orange', label='Cross-validation score')
    plt.xlabel('Training examples')
    plt.ylabel('Accuracy')
    plt.title(f'Learning Curve - {task.title()} Task (Random Forest)')
    plt.legend(loc='lower right')
    plt.grid(True, alpha=0.3)
    plt.ylim(0.5, 1.05)
    plt.tight_layout()
    plt.savefig(f'figures/advanced/{task}_learning_curve.png', dpi=150)
    plt.close()
    print(f"Saved: figures/advanced/{task}_learning_curve.png")
    
    # Store results
    results[task] = {
        'svm_preds': svm_preds,
        'rf_preds': rf_preds,
        'y_true': y,
        'svm_cm': svm_cm,
        'rf_cm': rf_cm,
        'train_sizes': train_sizes_abs,
        'train_scores': train_mean,
        'test_scores': test_mean
    }

# ============================================
# 5. STATISTICAL SIGNIFICANCE TESTS
# ============================================
print(f"\n{'='*60}")
print("STATISTICAL SIGNIFICANCE TESTS")
print("="*60)

# Compare reading vs interview performance using McNemar's test
# For simplicity, we'll use a chi-square test on the accuracy differences

print("\n--- Task Comparison (Reading vs Interview) ---")

# Get accuracies from cross-validation for both tasks
reading_acc = np.mean(results['reading']['rf_preds'] == results['reading']['y_true'])
interview_acc = np.mean(results['interview']['rf_preds'] == results['interview']['y_true'])

print(f"Reading accuracy: {reading_acc:.1%}")
print(f"Interview accuracy: {interview_acc:.1%}")
print(f"Difference: {interview_acc - reading_acc:.1%}")

# Perform a proportion test (z-test for two proportions)
n1 = len(results['reading']['y_true'])
n2 = len(results['interview']['y_true'])
p1 = reading_acc
p2 = interview_acc
p_pooled = (p1*n1 + p2*n2) / (n1 + n2)

se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
z = (p2 - p1) / se
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print(f"\nTwo-proportion z-test:")
print(f"  Z-statistic: {z:.3f}")
print(f"  P-value: {p_value:.4f}")
if p_value < 0.05:
    print("  Result: SIGNIFICANT (p < 0.05) - Interview is significantly better than reading")
else:
    print("  Result: Not significant (p >= 0.05)")

# Save significance results
sig_results = {
    'comparison': ['Reading vs Interview'],
    'reading_acc': [reading_acc],
    'interview_acc': [interview_acc],
    'difference': [interview_acc - reading_acc],
    'z_statistic': [z],
    'p_value': [p_value],
    'significant': [p_value < 0.05]
}
pd.DataFrame(sig_results).to_csv('results/advanced/statistical_significance.csv', index=False)

# ============================================
# 6. COMPARISON VISUALISATIONS
# ============================================
print(f"\n{'='*60}")
print("COMPARISON VISUALISATIONS")
print("="*60)

# Accuracy comparison bar chart
fig, ax = plt.subplots(figsize=(10, 6))

tasks = ['Reading', 'Interview']
svm_accs = [
    np.mean(results['reading']['svm_preds'] == results['reading']['y_true']),
    np.mean(results['interview']['svm_preds'] == results['interview']['y_true'])
]
rf_accs = [
    np.mean(results['reading']['rf_preds'] == results['reading']['y_true']),
    np.mean(results['interview']['rf_preds'] == results['interview']['y_true'])
]

x = np.arange(len(tasks))
width = 0.35

bars1 = ax.bar(x - width/2, svm_accs, width, label='SVM', color='steelblue')
bars2 = ax.bar(x + width/2, rf_accs, width, label='Random Forest', color='darkorange')

ax.set_ylabel('Accuracy')
ax.set_title('Classification Accuracy by Task and Algorithm')
ax.set_xticks(x)
ax.set_xticklabels(tasks)
ax.legend()
ax.set_ylim(0.5, 1.0)
ax.axhline(y=0.5, color='gray', linestyle='--', alpha=0.5, label='Chance level')

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1%}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1%}', xy=(bar.get_x() + bar.get_width()/2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

plt.tight_layout()
plt.savefig('figures/advanced/accuracy_comparison.png', dpi=150)
plt.close()
print("Saved: figures/advanced/accuracy_comparison.png")

# Feature importance comparison (top 10 side by side)
reading_imp = pd.read_csv('results/reading_gini_importance.csv').head(10)
interview_imp = pd.read_csv('results/interview_gini_importance.csv').head(10)

fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Reading features
axes[0].barh(range(10), reading_imp['importance'].values[::-1], color='steelblue')
axes[0].set_yticks(range(10))
axes[0].set_yticklabels([f[:35] for f in reading_imp['feature'].values[::-1]])
axes[0].set_xlabel('Importance')
axes[0].set_title('Top 10 Features - Reading Task')

# Interview features
axes[1].barh(range(10), interview_imp['importance'].values[::-1], color='darkorange')
axes[1].set_yticks(range(10))
axes[1].set_yticklabels([f[:35] for f in interview_imp['feature'].values[::-1]])
axes[1].set_xlabel('Importance')
axes[1].set_title('Top 10 Features - Interview Task')

plt.tight_layout()
plt.savefig('figures/advanced/feature_importance_comparison.png', dpi=150)
plt.close()
print("Saved: figures/advanced/feature_importance_comparison.png")

# ============================================
# 7. SUMMARY
# ============================================
print(f"\n{'='*60}")
print("ANALYSIS COMPLETE")
print("="*60)

print("\nFiles created:")
print("\nResults:")
for f in os.listdir('results/advanced'):
    print(f"  - results/advanced/{f}")

print("\nFigures:")
for f in os.listdir('figures/advanced'):
    print(f"  - figures/advanced/{f}")

print("\n✅ All advanced analysis complete!")
