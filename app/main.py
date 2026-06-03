import streamlit as st
import pandas as pd
import numpy as np
import time

from config import (
    CSS_PATH,
    IMAGE_PATH
)

from helpers import (
    get_base64,
    load_css
)

from loaders import (
    load_resources
)

from gemini_service import (
    get_ai_diet_plan
)

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ArogyaIQ",
    layout="wide"
)


# ---------------- IMAGE ----------------
bg_image = get_base64(
    IMAGE_PATH
)


# ---------------- SET BACKGROUND ----------------
st.markdown(
    f"""
    <style>

    .stApp {{

        background-image:
            url("data:image/png;base64,{bg_image}");

        background-size: cover;

        background-position: center;

        background-repeat: no-repeat;

        background-attachment: fixed;

    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- PAGE STATE ----------------
if "page" not in st.session_state:

    st.session_state.page = "home"


# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":

    # st.markdown(
    #     """
    #     <div class="hero-container">

    #         <div class="hero-title">

    #             Patient Intelligence

    #         </div>

    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

    if st.button(
        "Get Started"
    ):

        st.session_state.page = "dashboard"

        st.rerun()


# ---------------- LOAD CSS ----------------
st.markdown(
    f"<style>{load_css(CSS_PATH)}</style>",
    unsafe_allow_html=True
)


# ---------------- LOAD MODEL ----------------
try:

    model, scaler_X, scaler_y, feature_cols = load_resources()

except Exception as e:

    st.error(
        f"⚠️ System Error: {e}"
    )

    st.stop()


# ---------------- UI ----------------
st.title(
    "🥗  ArogyaIQ: Personal AI Nutritionist"
)

st.markdown("---")


# ---------------- SIDEBAR ----------------
with st.sidebar:

    st.header(
        "Patient Intelligence"
    )

    with st.expander(
        "Physical & Clinical",
        expanded=True
    ):

        age = st.number_input(
            "Age",
            18,
            100,
            30
        )

        height = st.number_input(
            "Height (cm)",
            120,
            220,
            170
        )

        weight = st.number_input(
            "Weight (kg)",
            30,
            200,
            70
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        sys_bp = st.number_input(
            "Systolic BP",
            80,
            200,
            120
        )

        dia_bp = st.number_input(
            "Diastolic BP",
            50,
            120,
            80
        )

        chol = st.number_input(
            "Cholesterol",
            100,
            400,
            200
        )

        sugar = st.number_input(
            "Blood Sugar",
            70,
            300,
            100
        )

    with st.expander(
        "Lifestyle & Medical History"
    ):

        disease = st.selectbox(
            "Chronic Disease",
            [
                "No Chronic Disease",
                "Diabetes",
                "Hypertension",
                "Heart Disease",
                "Obesity"
            ]
        )

        allergy = st.selectbox(
            "Allergies",
            [
                "No Allergies",
                "Gluten Intolerance",
                "Lactose Intolerance",
                "Nut Allergy"
            ]
        )

        diet_habit = st.selectbox(
            "Current Diet",
            [
                "Regular",
                "Vegetarian",
                "Vegan",
                "Keto"
            ]
        )

        cuisine = st.selectbox(
            "Preferred Cuisine",
            [
                "Indian",
                "Asian",
                "Mediterranean",
                "Western"
            ]
        )

        steps = st.number_input(
            "Daily Steps",
            0,
            30000,
            5000
        )

        sleep = st.slider(
            "Sleep Hours",
            0.0,
            12.0,
            7.0
        )

        smoke = st.selectbox(
            "Smoking?",
            ["No", "Yes"]
        )

        alcohol = st.selectbox(
            "Alcohol?",
            ["No", "Yes"]
        )


# ---------------- MAIN LOGIC ----------------
if st.button(
    "Generate My Personalized Plan"
):

    bmi = weight / (
        (height / 100) ** 2
    )

    input_data = {
        col: 0 for col in feature_cols
    }

    input_data.update({

        'Age': age,
        'Height_cm': height,
        'Weight_kg': weight,
        'BMI': bmi,

        'Blood_Pressure_Systolic': sys_bp,
        'Blood_Pressure_Diastolic': dia_bp,

        'Cholesterol_Level': chol,
        'Blood_Sugar_Level': sugar,

        'Daily_Steps': steps,
        'Sleep_Hours': sleep,

        'Age_BMI': age * bmi,

        'BMI_squared': bmi**2,

        'Weight_Height_Ratio': weight / height,

        'Log_Daily_Steps': np.log1p(
            steps
        )
    })

    mappings = {

        'Gender': gender,

        'Chronic_Disease': disease,

        'Allergies': allergy,

        'Dietary_Habits': diet_habit,

        'Preferred_Cuisine': cuisine,

        'Smoking_Habit': smoke,

        'Alcohol_Consumption': alcohol
    }

    for key, value in mappings.items():

        col_name = f"{key}_{value}"

        if col_name in input_data:

            input_data[col_name] = 1

    input_df = pd.DataFrame(
        [input_data]
    )[feature_cols]

    scaled_X = scaler_X.transform(
        input_df
    )

    prediction = model.predict(
        scaled_X
    )

    nutrients = scaler_y.inverse_transform(
        prediction
    )[0]

    st.subheader(
        "📊 Your Daily Nutritional Targets"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Target Calories",
        f"{nutrients[0]:.0f} kcal"
    )

    c2.metric(
        "Protein",
        f"{nutrients[1]:.1f} g"
    )

    c3.metric(
        "Fats",
        f"{nutrients[2]:.1f} g"
    )

    c4.metric(
        "Carbohydrates",
        f"{nutrients[3]:.1f} g"
    )

    st.divider()

    with st.spinner(
        "ArogyaIQ is crafting your meal plan..."
    ):

        profile = f"{age}yo {gender}, {disease}, {cuisine} {diet_habit}."

        meal_plan = get_ai_diet_plan(
            nutrients,
            profile,
            cuisine
        )

        st.subheader(
            "👨‍🍳 ArogyaIQ Personalized Nutrition Plan"
        )

        st.markdown(
            meal_plan
        )