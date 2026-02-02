# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 08:47:33 2026

@author: sits
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# --------------------------------------------------
# APP CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Harvest Guard", layout="wide")

st.title("🌾 Harvest Guard – Smart Farming ")

# --------------------------------------------------
# FARMER / RESEARCHER PROFILE
# --------------------------------------------------
st.header("👨‍🌾 Researcher Overview")

name = "Mr Vincent Thole"
field = "Smart Agriculture & Precision Farming"
institution = "University of Limpopo"


col1, col2 = st.columns(2)
with col1:
    st.write(f"**Name:** {name}")
    st.write(f"**Field:** {field}")
    st.write(f"**Institution:** {institution}")
st.write("The objective of Harvest Guard is to develop a data-driven smart farming system that leverages weather analytics, machine learning–based yield prediction, pest risk assessment, and vegetation monitoring to enhance agricultural productivity and sustainability.")



with col2:
    st.image(
        "C:/Users/sits/Downloads/data visualization/streamlit_files/Smart Farming.jpg",
        caption="Smart farming improves productivity and sustainability",
        
    )

# --------------------------------------------------
# WEATHER TRENDS SECTION
# --------------------------------------------------
st.header("🌦 Crop Weather Trends")

weather_data = pd.DataFrame({
    "Date": pd.date_range(start="2025-01-01", periods=12, freq="M"),
    "Rainfall (mm)": np.random.randint(20, 180, 12),
    "Temperature (°C)": np.random.randint(15, 35, 12),
    "Humidity (%)": np.random.randint(40, 90, 12),
})

st.line_chart(
    weather_data.set_index("Date")[["Rainfall (mm)", "Temperature (°C)"]]
)

st.dataframe(weather_data)

# --------------------------------------------------
# YIELD PREDICTION (DUMMY ML MODEL)
# --------------------------------------------------
st.header("🌽 Crop Yield Prediction ")

st.write("Predict expected crop yield based on rainfall and temperature.")

# Dummy training data

train_data = pd.read_csv("crop_yield_data.csv")

X = train_data[["Rainfall", "Temperature", "Soil_Moisture"]]
y = train_data["Yield"]

model = LinearRegression()
model.fit(X, y)

col1, col2, col3 = st.columns(3)

with col1:
    rainfall_input = st.slider("Rainfall (mm)", 20, 250, 120)

with col2:
    temp_input = st.slider("Temperature (°C)", 15, 35, 25)

with col3:
    soil_moisture_input = st.slider("Soil Moisture (%)", 20, 80, 50)

predicted_yield = model.predict([[
    rainfall_input,
    temp_input,
    soil_moisture_input
]])[0]

st.metric(
    "🌾 Predicted Yield (tons/hectare)",
    f"{predicted_yield:.2f}"
)


# --------------------------------------------------
# PEST RISK INDICATOR
# --------------------------------------------------
st.header("🐛 Pest Risk Indicator")

def pest_risk(temp, humidity):
    if temp > 28 and humidity > 70:
        return "🔴 High Risk"
    elif temp > 22 and humidity > 55:
        return "🟠 Medium Risk"
    else:
        return "🟢 Low Risk"

current_temp = st.slider("Current Temperature (°C)", 15, 40, 30)
current_humidity = st.slider("Current Humidity (%)", 30, 100, 75)

risk = pest_risk(current_temp, current_humidity)

st.subheader(f"Pest Risk Level: {risk}")

if "High" in risk:
    st.warning("High chance of pest outbreaks. Consider early intervention.")
elif "Medium" in risk:
    st.info("Moderate pest activity expected. Monitor fields closely.")
else:
    st.success("Low pest risk. Conditions are stable.")

# --------------------------------------------------
# NDVI / VEGETATION INDEX (PLACEHOLDER)
# --------------------------------------------------
st.header("📊 NDVI – Vegetation Health (Placeholder)")

ndvi_data = pd.DataFrame({
    "Date": pd.date_range(start="2024-01-01", periods=10),
    "NDVI": np.round(np.random.uniform(0.2, 0.9, 10), 2)
})

st.area_chart(ndvi_data.set_index("Date"))

st.write("""
**NDVI Interpretation**
- 🟢 0.6 – 0.9 → Healthy vegetation  
- 🟡 0.3 – 0.6 → Moderate stress  
- 🔴 < 0.3 → Poor vegetation health  

*(This is simulated data – satellite integration can be added later.)*
""")

st.dataframe(ndvi_data)

# --------------------------------------------------
# CONTACT
# --------------------------------------------------
st.header("📞 Contact Information")

email = "tebogoselemela06@gmail.com"
phone = "0676620716"

st.write(f"📧 Email: {email}")
st.write(f"📱 Phone: {phone}")

st.caption("© 2026 Harvest Guard | Smart Farming for Sustainable Agriculture")
