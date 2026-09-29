# Phase 3 — Project Design

## Architecture

```text
┌─────────────────────┐
│   Streamlit UI      │
│   User Inputs       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ BMI Calculator      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Feature Preparation │
│ + StandardScaler    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ KNN ML Classifier   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Goal + Confidence   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ Recommendations +   │
│ 7-Day Starter Plan  │
└─────────────────────┘
```

## ML Features

1. Age
2. BMI
3. Activity days per week
4. Average sleep hours
5. Water intake
6. Approximate calories

## Predicted Classes

- Weight Management
- Healthy Weight Gain
- Beginner Fitness
- Strength & Performance
- Lifestyle Improvement
- General Fitness

## Design Note

The classifier is a demonstration model. Its training labels are generated from simple rules over synthetic data so that the ML pipeline can be reproduced locally.
