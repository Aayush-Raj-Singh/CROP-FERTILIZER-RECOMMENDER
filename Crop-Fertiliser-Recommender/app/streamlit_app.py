import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px

# Load model
crop_model = joblib.load("models/crop_recommender.pkl")

# App title
st.set_page_config(page_title="🌾 Crop & Fertiliser Recommender", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #f9f9f9;}
    h1 {color: #2c6e49;}
    .stButton>button {
        background-color: #2c6e49;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌾 Smart Crop & Fertiliser Recommendation System")
st.write("Provide soil & weather details to get the best crop and fertiliser suggestion.")

# Input columns
col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 200, 50)
    P = st.number_input("Phosphorus (P)", 0, 200, 50)
    K = st.number_input("Potassium (K)", 0, 200, 50)

with col2:
    temperature = st.number_input("🌡 Temperature (°C)", 0.0, 50.0, 25.0)
    humidity = st.number_input("💧 Humidity (%)", 0.0, 100.0, 60.0)

with col3:
    ph = st.number_input("⚖️ pH Value", 0.0, 14.0, 6.5)
    rainfall = st.number_input("🌧 Rainfall (mm)", 0.0, 500.0, 120.0)

# Prediction button
if st.button("🔍 Recommend Crop & Fertiliser"):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = crop_model.predict(features)[0]
    proba = crop_model.predict_proba(features)[0]
    confidence = np.max(proba) * 100

    st.success(f"🌱 Recommended Crop: **{prediction}**")
    st.info(f"📊 Model Confidence: **{confidence:.2f}%**")

    # --- Visuals ---
    st.subheader("📈 Soil & Weather Analysis")

    colA, colB = st.columns(2)

    # Soil Nutrient Levels
    with colA:
        nutrients = {"Nitrogen": N, "Phosphorus": P, "Potassium": K}
        fig = px.bar(x=list(nutrients.keys()), y=list(nutrients.values()),
                     labels={'x': "Nutrients", 'y': "Level"},
                     title="Soil Nutrient Levels",
                     color=list(nutrients.values()),
                     color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

    # Weather Gauge
    with colB:
        fig = go.Figure()

        fig.add_trace(go.Indicator(
            mode="gauge+number",
            value=rainfall,
            title={'text': "Rainfall (mm)"},
            gauge={'axis': {'range': [0, 500]}}
        ))

        st.plotly_chart(fig, use_container_width=True)

    # Extra Gauges: Temperature & Humidity
    colC, colD = st.columns(2)

    with colC:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=temperature,
            title={'text': "Temperature (°C)"},
            gauge={'axis': {'range': [0, 50]}}
        ))
        st.plotly_chart(fig, use_container_width=True)

    with colD:
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=humidity,
            title={'text': "Humidity (%)"},
            gauge={'axis': {'range': [0, 100]}}
        ))
        st.plotly_chart(fig, use_container_width=True)

    # Confidence Bar
    st.subheader("🔎 Prediction Confidence Across Crops")
    conf_df = pd.DataFrame({"Crop": crop_model.classes_, "Confidence": proba})
    conf_fig = px.bar(conf_df.sort_values("Confidence", ascending=False),
                      x="Crop", y="Confidence",
                      title="Model Confidence for Each Crop",
                      color="Confidence", color_continuous_scale="Greens")
    st.plotly_chart(conf_fig, use_container_width=True)