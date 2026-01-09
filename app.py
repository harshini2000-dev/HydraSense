# HydraSense: Dehydration Detection and WaterIntake Recommendation
# in cmd, streamlit run app.py
import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load trained models & respective scalers
# -----------------------------
lr = joblib.load('dehydration_cls_model.pkl')
scaler_cls = joblib.load('dehydration_scaler.pkl') # logistic regression

reg = joblib.load('water_intake_model.pkl')
scaler_reg = joblib.load('water_intake_scaler.pkl') # linear regression


# -----------------------------
# App UI
# -----------------------------
st.set_page_config(page_title="Smart Hydration System", layout="centered")

st.title("💧 HydraSense: Dehydration Detection System")
st.write("Predict dehydration risk and get personalized recommended amount of water to stay hydrated.")

st.header("👤 User Information")

age = st.number_input("Age", min_value=0, max_value=120, value= 20)
weight = st.number_input("Weight (kgs)", min_value=0, max_value=120, value= 50)
water_amt = st.number_input("Daily Water Intake (liters)", min_value=0.00, max_value=4.50, format="%.2f", value=2.1)
gender = st.selectbox("Gender", ["Female", "Male"])
activity = st.selectbox("Physical Activity Level", ["High", "Moderate", "Low"])
weather = st.selectbox("Weather", ["Normal", "Hot", "Cold"])

# -----------------------------
# Encode user input
# -----------------------------

def encode_input(modelNo):
    data_hydration = {
        'Age': age,
        'Weight (kg)': weight,
        'Daily Water Intake (liters)': water_amt,
        'Gender_Male': 1 if gender == 'Male' else 0,
        'Physical Activity Level_Low': 1 if activity == 'Low' else 0,
        'Physical Activity Level_Moderate': 1 if activity == 'Moderate' else 0,
        'Weather_Hot': 1 if weather == 'Hot' else 0,
        'Weather_Normal': 1 if weather == 'Normal' else 0
    }

    data_waterintake = {
        'Age': age,
        'Weight (kg)': weight,
        'Gender_Male': 1 if gender == 'Male' else 0,
        'Physical Activity Level_Low': 1 if activity == 'Low' else 0,
        'Physical Activity Level_Moderate': 1 if activity == 'Moderate' else 0,
        'Weather_Hot': 1 if weather == 'Hot' else 0,
        'Weather_Normal': 1 if weather == 'Normal' else 0
    }

    if modelNo == 1:
        return pd.DataFrame([data_hydration])
    return pd.DataFrame([data_waterintake])

# -----------------------------
# Prediction logic
# -----------------------------
if st.button("🔍 Analyze Hydration"):

    data_hydration = encode_input(1)
    data_waterIntake = encode_input(2)

    user_scaled_hyd = scaler_cls.transform(data_hydration) # Scale input
    dehydration = lr.predict(user_scaled_hyd)[0] # Predict dehydration risk

    user_scaled_reg = scaler_reg.transform(data_waterIntake)
    predicted_water = reg.predict(user_scaled_reg)[0] # Predict water intake

    st.subheader("📊 Results")

    if dehydration == 1:
        st.error("⚠️ High dehydration risk detected")
    else:
        st.success("✅ You are well hydrated")


    if water_amt < 2.0 and predicted_water < 2.0:
        predicted_water = predicted_water + 1.0

    st.metric("💧 Recommended Daily Water Intake (liters)", f"{predicted_water:.2f}")

    # Smart reminder logic
    if dehydration == 1:
        st.warning(f"🔔 Drink at least {predicted_water:.2f} liters of water today!")
    else:
        st.info("👍 Keep maintaining your hydration level")

st.markdown("---")
st.caption("Built using Machine Learning | Logistic Regression + Linear Regression")