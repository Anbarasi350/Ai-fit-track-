import streamlit as st
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="AI FitTrack", page_icon="🏃", layout="wide")

# Synthetic training data is used to demonstrate the ML workflow.
# It is generated with a fixed seed so the demo is reproducible.
rng = np.random.default_rng(42)
n = 800

age = rng.integers(18, 61, n)
bmi = rng.uniform(17, 35, n)
activity = rng.integers(1, 8, n)
sleep = rng.uniform(4.5, 9.5, n)
water = rng.uniform(1.0, 4.0, n)
calories = rng.integers(1400, 3200, n)


def label_goal(a, b, act, sl, wat, cal):
    if b >= 27:
        return "Weight Management"
    if b <= 19:
        return "Healthy Weight Gain"
    if act <= 2:
        return "Beginner Fitness"
    if act >= 6 and sl >= 7:
        return "Strength & Performance"
    if sl < 6 or wat < 1.8:
        return "Lifestyle Improvement"
    return "General Fitness"


y = np.array(
    [label_goal(*row) for row in zip(age, bmi, activity, sleep, water, calories)]
)
X = np.column_stack([age, bmi, activity, sleep, water, calories])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = KNeighborsClassifier(n_neighbors=9)
model.fit(X_scaled, y)


def calculate_bmi(weight, height_cm):
    return weight / ((height_cm / 100) ** 2)


def bmi_category(bmi_value):
    if bmi_value < 18.5:
        return "Below typical adult BMI range"
    if bmi_value < 25:
        return "Typical adult BMI range"
    if bmi_value < 30:
        return "Above typical adult BMI range"
    return "High adult BMI range"


def recommendations(goal, activity_days, sleep_hours, water_litres):
    base = {
        "Weight Management": [
            "Choose balanced meals and track portions consistently.",
            "Aim for regular moderate activity and gradual progress.",
            "Prioritize sleep and hydration.",
        ],
        "Healthy Weight Gain": [
            "Focus on nutrient-dense meals with adequate protein.",
            "Add resistance training progressively.",
            "Track weekly trends instead of daily fluctuations.",
        ],
        "Beginner Fitness": [
            "Start with walking and simple full-body exercises.",
            "Increase activity gradually to avoid doing too much too soon.",
            "Build a consistent weekly routine.",
        ],
        "Strength & Performance": [
            "Use progressive resistance training with recovery days.",
            "Maintain adequate nutrition and hydration.",
            "Track strength, repetitions and recovery.",
        ],
        "Lifestyle Improvement": [
            "Create a consistent sleep and hydration routine.",
            "Add short activity breaks throughout the day.",
            "Build one sustainable habit at a time.",
        ],
        "General Fitness": [
            "Combine cardio, strength and mobility work.",
            "Keep meals balanced and stay hydrated.",
            "Review progress weekly and adjust gradually.",
        ],
    }

    tips = base[goal].copy()

    if activity_days < 3:
        tips.append("Current activity is low; begin with short, comfortable sessions.")
    if sleep_hours < 6:
        tips.append("Current sleep input is low; consider improving sleep consistency.")
    if water_litres < 2:
        tips.append(
            "Current water input is low; increase fluids gradually based on your needs."
        )

    return tips


st.title("🏃 AI FitTrack")
st.caption(
    "Personalized fitness planning demo using BMI + a simple machine-learning recommendation model"
)

with st.sidebar:
    st.header("Your Profile")
    name = st.text_input("Name", "Student")
    age_in = st.number_input("Age", 18, 80, 21)
    height = st.number_input("Height (cm)", 120.0, 220.0, 165.0)
    weight = st.number_input("Weight (kg)", 30.0, 200.0, 60.0)
    activity_in = st.slider("Activity days / week", 0, 7, 3)
    sleep_in = st.slider("Average sleep (hours)", 3.0, 12.0, 7.0, 0.5)
    water_in = st.slider("Water (litres / day)", 0.5, 5.0, 2.0, 0.1)
    calories_in = st.number_input(
        "Approx. daily calories", 1000, 5000, 2000, 50
    )

bmi = calculate_bmi(weight, height)
input_row = np.array(
    [[age_in, bmi, activity_in, sleep_in, water_in, calories_in]]
)

scaled_input = scaler.transform(input_row)
pred = model.predict(scaled_input)[0]
confidence = float(model.predict_proba(scaled_input).max())

c1, c2, c3 = st.columns(3)
c1.metric("BMI", f"{bmi:.1f}")
c2.metric("ML Goal", pred)
c3.metric("Model confidence", f"{confidence * 100:.0f}%")

st.info(
    "This is an educational project demo, not medical advice. BMI and model output "
    "are simplified indicators and should not replace professional guidance."
)

st.subheader(f"Hello, {name}! 👋")
st.write(f"**BMI category:** {bmi_category(bmi)}")
st.write(f"**Suggested focus:** **{pred}**")

st.subheader("📋 Personalized Plan")
for tip in recommendations(pred, activity_in, sleep_in, water_in):
    st.write("• " + tip)

st.subheader("📅 Simple 7-Day Starter Plan")
plan = pd.DataFrame(
    {
        "Day": [
            "Day 1",
            "Day 2",
            "Day 3",
            "Day 4",
            "Day 5",
            "Day 6",
            "Day 7",
        ],
        "Focus": [
            "Cardio + mobility",
            "Strength",
            "Light walk",
            "Strength + mobility",
            "Cardio",
            "Recovery / stretching",
            "Weekly review",
        ],
        "Duration": [
            "20–30 min",
            "25–35 min",
            "20 min",
            "25–35 min",
            "20–30 min",
            "15–20 min",
            "10 min",
        ],
    }
)
st.dataframe(plan, use_container_width=True, hide_index=True)

with st.expander("🔎 How the AI part works"):
    st.write(
        "The demo creates a reproducible synthetic dataset, standardizes six profile "
        "features, and trains a K-Nearest Neighbors classifier. The model maps similar "
        "profiles to a fitness-focus label. Recommendation text is then generated from "
        "the predicted goal."
    )
    st.write(
        "Features: age, BMI, activity days, sleep, water intake and approximate calories."
    )
