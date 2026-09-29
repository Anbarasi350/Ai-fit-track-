# AI FitTrack — Team 1

**Project Title:** AI FitTrack  
**Team:** Team 1  
**Team Members:** Anbarasi B, Praveen Raj P, Hemalatha N, Monisha M  
**Track:** AI / ML / GenAI project submission  
**Project Type:** Educational fitness recommendation web application

## 1. Project Overview

AI FitTrack is a simple machine-learning based fitness planning application. A user enters basic profile information such as age, height, weight, activity level, sleep, water intake and approximate daily calories.

The application calculates BMI and uses a K-Nearest Neighbors (KNN) model to suggest a broad fitness focus. It then displays simple habit and activity recommendations and a 7-day starter plan.

> **Important:** This is an educational software project. It is not a medical or clinical system and its recommendations should not be treated as medical advice.

## 2. Main Features

- BMI calculation
- BMI category display
- Machine-learning based fitness-focus prediction
- Personalized recommendation list
- Simple 7-day starter plan
- Responsive Streamlit interface
- Reproducible synthetic training data
- No external API key required

## 3. Technology Stack

- Python
- Streamlit
- NumPy
- Pandas
- Scikit-learn
- K-Nearest Neighbors (KNN)
- StandardScaler

## 4. How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

If your terminal has a path issue with the phase folder, run:

```bash
streamlit run "5. Project Development Phase/app.py"
```

The browser will open the local Streamlit application.

## 5. Repository Structure

```text
AI_FitTrack_Team1/
├── 1. Brainstorming & Ideation/
├── 2. Requirement Analysis/
├── 3. Project Design Phase/
├── 4. Project Planning Phase/
├── 5. Project Development Phase/
│   └── app.py
├── 6.Project Testing/
├── 7.Project Documentation/
├── 8.Project Demonstration/
├── data/
│   └── sample_fitness_data.csv
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 6. ML Workflow

```text
User Input
   ↓
BMI Calculation
   ↓
Feature Preparation
   ↓
StandardScaler
   ↓
KNN Model
   ↓
Fitness Focus Prediction
   ↓
Personalized Tips
   ↓
7-Day Starter Plan
```

## 7. Submission Checklist

- [ ] Replace any placeholder personal/college details in the documentation.
- [ ] Create a **public GitHub repository**.
- [ ] Upload all project folders and files.
- [ ] Verify the GitHub URL opens in an incognito/private browser.
- [ ] Run the project and record the demo.
- [ ] Upload the demo video to Google Drive.
- [ ] Set the Drive video to **Anyone with the link / Viewer**.
- [ ] Paste the public GitHub URL and public demo URL in the official submission form.
- [ ] Enter the registered University, College, College Code, full name, TN Skills email, course completion email and NM ID exactly as registered.

## 8. Team Details

| Field | Value |
|---|---|
| Team | Team 1 |
| Project | AI FitTrack |
| Member 1 | Anbarasi B |
| Member 2 | Praveen Raj P |
| Member 3 | Hemalatha N |
| Member 4 | Monisha M |

**Do not put passwords, API keys or other private credentials in the public repository.**
