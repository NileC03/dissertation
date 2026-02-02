#!/usr/bin/env python3
"""
Feature Extraction Script for ANDROIDS Corpus
Extracts eGeMAPS features from all audio files using OpenSMILE
"""

import os
import pandas as pd
import opensmile
from tqdm import tqdm
from pathlib import Path

# Paths
BASE_DIR = Path("/Users/moltbot/Documents/research-workspace/dissertation")
DATA_DIR = BASE_DIR / "data" / "Androids-Corpus"
OUTPUT_DIR = BASE_DIR / "features"
OUTPUT_DIR.mkdir(exist_ok=True)

# Initialize OpenSMILE with eGeMAPS features
print("Initializing OpenSMILE...")
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)

def extract_features_from_directory(audio_dir, label, task_name):
    """Extract features from all WAV files in a directory."""
    features_list = []
    metadata_list = []
    
    wav_files = list(Path(audio_dir).glob("*.wav"))
    
    for wav_path in tqdm(wav_files, desc=f"{task_name} - {label}"):
        try:
            # Extract features
            features = smile.process_file(str(wav_path))
            
            # Parse filename: nn_XGmm_t.wav
            filename = wav_path.stem
            parts = filename.split('_')
            speaker_id = parts[0]
            condition_gender_age = parts[1] if len(parts) > 1 else ""
            education = parts[2] if len(parts) > 2 else ""
            
            # Extract metadata
            condition = condition_gender_age[0] if condition_gender_age else ""  # P or C
            gender = condition_gender_age[1] if len(condition_gender_age) > 1 else ""  # M or F
            age = condition_gender_age[2:] if len(condition_gender_age) > 2 else ""
            
            # Add to lists
            features_list.append(features.iloc[0])
            metadata_list.append({
                'filename': filename,
                'speaker_id': speaker_id,
                'condition': condition,
                'gender': gender,
                'age': age,
                'education': education,
                'label': label,  # HC or PT
                'task': task_name,
                'depression': 1 if label == 'PT' else 0
            })
            
        except Exception as e:
            print(f"Error processing {wav_path}: {e}")
    
    return features_list, metadata_list

# Process all audio files
all_features = []
all_metadata = []

print("\n" + "="*60)
print("EXTRACTING FEATURES FROM ANDROIDS CORPUS")
print("="*60)

# Reading Task
print("\n--- Reading Task ---")
for label in ['HC', 'PT']:
    audio_dir = DATA_DIR / "Reading-Task" / "audio" / label
    features, metadata = extract_features_from_directory(audio_dir, label, "reading")
    all_features.extend(features)
    all_metadata.extend(metadata)

# Interview Task
print("\n--- Interview Task ---")
for label in ['HC', 'PT']:
    audio_dir = DATA_DIR / "Interview-Task" / "audio" / label
    features, metadata = extract_features_from_directory(audio_dir, label, "interview")
    all_features.extend(features)
    all_metadata.extend(metadata)

# Create DataFrames
print("\n--- Creating DataFrames ---")
features_df = pd.DataFrame(all_features)
metadata_df = pd.DataFrame(all_metadata)

# Combine features and metadata
combined_df = pd.concat([metadata_df.reset_index(drop=True), features_df.reset_index(drop=True)], axis=1)

# Save to files
print("\n--- Saving Features ---")

# Save combined dataset
combined_df.to_csv(OUTPUT_DIR / "all_features.csv", index=False)
print(f"✓ Saved: {OUTPUT_DIR / 'all_features.csv'}")

# Save separate files for each task
reading_df = combined_df[combined_df['task'] == 'reading']
interview_df = combined_df[combined_df['task'] == 'interview']

reading_df.to_csv(OUTPUT_DIR / "reading_features.csv", index=False)
interview_df.to_csv(OUTPUT_DIR / "interview_features.csv", index=False)
print(f"✓ Saved: {OUTPUT_DIR / 'reading_features.csv'}")
print(f"✓ Saved: {OUTPUT_DIR / 'interview_features.csv'}")

# Save pickle for faster loading
combined_df.to_pickle(OUTPUT_DIR / "all_features.pkl")
print(f"✓ Saved: {OUTPUT_DIR / 'all_features.pkl'}")

# Print summary
print("\n" + "="*60)
print("EXTRACTION COMPLETE")
print("="*60)
print(f"\nTotal samples: {len(combined_df)}")
print(f"  - Reading task: {len(reading_df)} ({len(reading_df[reading_df['depression']==0])} HC, {len(reading_df[reading_df['depression']==1])} PT)")
print(f"  - Interview task: {len(interview_df)} ({len(interview_df[interview_df['depression']==0])} HC, {len(interview_df[interview_df['depression']==1])} PT)")
print(f"\nFeatures per sample: {len(features_df.columns)}")
print(f"\nFeature columns:")
for i, col in enumerate(features_df.columns[:10]):
    print(f"  {i+1}. {col}")
print(f"  ... and {len(features_df.columns) - 10} more")

print(f"\nFiles saved to: {OUTPUT_DIR}")
