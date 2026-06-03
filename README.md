## AI-Powered Personalized Nutrition Intelligence Platform 🥗

Personalized Nutrition Intelligence is an end-to-end healthcare AI project that combines Machine Learning, Deep Learning, and Generative AI to provide personalized nutrition recommendations based on patient health metrics, clinical parameters, lifestyle habits, medical history, and dietary preferences.

The platform predicts personalized nutritional requirements using a trained deep learning model and generates a personalized 7-day meal plan based on the user's health condition and selected cuisine preference.

---

# Problem Statement

Many individuals follow generic diet plans that fail to consider:

- Individual health conditions
- Clinical biomarkers
- Lifestyle habits
- Dietary restrictions
- Cultural food preferences

ArogyaIQ solves this by transforming patient health data into personalized nutrition intelligence.

---

# Project Components

This project consists of two major components:

## 1. Machine Learning Development

File:

```text
Personalized_Diet_Recommendation.ipynb
```

This notebook includes:

### Data Analysis

- Data loading
- Data inspection
- Missing value handling
- Duplicate value removal
- Outlier detection

### Exploratory Data Analysis

- Feature distribution analysis
- Correlation analysis
- Health metric visualization

### Data Preprocessing

- Label encoding
- One-hot encoding
- Feature scaling
- Train-test split

### Feature Engineering

Created features:

- BMI
- Age × BMI
- BMI Squared
- Weight/Height Ratio
- Log(Daily Steps)

### Model Development

- Deep learning model training
- Model evaluation
- Performance validation

### Model Export

Generated files:

- wellness_model.h5
- scaler_X.pkl
- scaler_y.pkl
- feature_cols.json

---

## 2. Production Web Application

Folder:

```text
app/
```

This contains the production-ready Streamlit application.

---

# Features

✅ Patient Intelligence Dashboard  
✅ Personalized Nutritional Prediction  
✅ AI-Based Meal Planning  
✅ 7-Day Meal Plan Generation  
✅ Multi-Cuisine Support  
✅ Lifestyle Recommendations  
✅ Interactive Web Interface  

---

# Supported Cuisines

- Indian
- Asian
- Mediterranean
- Western

---

# Input Parameters

## Physical Metrics

- Age
- Height
- Weight
- BMI

## Clinical Parameters

- Systolic Blood Pressure
- Diastolic Blood Pressure
- Cholesterol Level
- Blood Sugar Level

## Lifestyle Parameters

- Daily Steps
- Sleep Hours
- Smoking Habit
- Alcohol Consumption

## Medical History

- Chronic Disease
- Allergies

## Dietary Preferences

- Dietary Habit
- Preferred Cuisine

---

# Generated Output

ArogyaIQ generates:

## Nutritional Targets

- Daily Calories
- Protein Requirement
- Fat Requirement
- Carbohydrate Requirement

## Personalized Wellness Plan

- 7-Day Meal Plan
- Portion Sizes
- Hydration Recommendations
- Physical Activity Recommendations
- Sleep Recommendations

---

# Tech Stack

## Programming Language

- Python

## Data Science and Machine Learning

- Pandas
- NumPy
- TensorFlow
- Joblib
- h5py
- Scikit-learn

## Data Visualization

- Matplotlib
- Seaborn

## Web Application

- Streamlit
- HTML
- CSS

## Generative AI

- Google Gemini API
- Google Generative AI SDK

---

# Project Structure

```text
ArogyaIQ/
│
├── Personalized_Diet_Recommendation.ipynb
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── helpers.py
│   ├── loader.py
│   ├── gemini_service.py
│   ├── style.css
│   │
│   ├── assets/
│   │   ├── wellness_model.h5
│   │   ├── scaler_X.pkl
│   │   ├── scaler_y.pkl
│   │   └── feature_cols.json
│   │
│   └── images/
│       └── pat.png
│
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone <https://github.com/DeepanshuKumar09/PERSONALIZED_DIET_RECOMMENDER>
cd PERSONALIZED_DIET_RECOMMENDER
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Requirements

```txt
streamlit
pandas
numpy
tensorflow
joblib
google-generativeai
h5py
matplotlib
seaborn
scikit-learn
```

---

# Run Application

```bash
cd app
streamlit run main.py
```

---

# Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Export
   ↓
Streamlit Deployment
   ↓
AI Meal Plan Generation
```

---

# Future Enhancements

- User Authentication
- Nutrition History Tracking
- PDF Report Generation
- Doctor Dashboard
- Cloud Deployment
- Mobile Application
- Real-Time Health Monitoring

---

# Author

Deepanshu Kumar

Data Science | Machine Learning | Artificial Intelligence 
