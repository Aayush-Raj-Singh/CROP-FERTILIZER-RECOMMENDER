# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
import base64
import time

#---------------------- Functions ----------------------#
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-family: 'Orbitron', monospace;
            color: #00ff9f;
        }}

        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.75);
            z-index: 0;
        }}

        .stApp > div {{
            position: relative;
            z-index: 1;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: #00ff9f !important;
            text-shadow: 0 0 2px #00ff9f, 0 0 4px #00ff9f;
        }}

        .stNumberInput > div {{
            background: rgba(0,0,0,0.4);
            padding: 15px;
            border-radius: 15px;
            color: #00ff9f;
            border: 1px solid #00ff9f;
        }}

        .stButton>button {{
            background: transparent;
            border: 2px solid #00ff9f;
            color: #00ff9f;
            border-radius: 12px;
            padding: 12px 25px;
            font-size: 18px;
            font-weight: bold;
            transition: all 0.3s ease;
            text-shadow: 0 0 2px #00ff9f;
        }}
        .stButton>button:hover {{
            background: #00ff9f;
            color: black;
            box-shadow: 0 0 10px #00ff9f, 0 0 20px #00ff9f;
            transform: scale(1.03);
        }}

        .stAlert {{
            border-radius: 15px;
            padding: 15px;
            font-size: 18px;
            background: rgba(0,0,0,0.4) !important;
            border: 1px solid #00ff9f !important;
            color: #00ff9f !important;
            text-shadow: 0 0 2px #00ff9f;
        }}

        .footer {{
            text-align: center;
            color: #00ff9f;
            padding: 10px;
            font-size: 14px;
            text-shadow: 0 0 1px #00ff9f;
        }}

        @keyframes slideInLeft {{
          0% {{opacity: 0; transform: translateX(-50px);}}
          100% {{opacity: 1; transform: translateX(0);}}
        }}
        @keyframes slideInRight {{
          0% {{opacity: 0; transform: translateX(50px);}}
          100% {{opacity: 1; transform: translateX(0);}}
        }}
        .slide-left {{
            animation: slideInLeft 1s ease-out;
        }}
        .slide-right {{
            animation: slideInRight 1s ease-out;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Animated gauge function
def animated_gauge(value, title, unit, min_val, max_val):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=0,
        title={'text': f"{title}", 'font': {'color': '#00ff9f', 'size': 16}},
        number={'font': {'color': '#00ff9f', 'size': 22}, 'suffix': f" {unit}"},
        gauge={
            'axis': {'range': [min_val, max_val], 'tickcolor': '#00ff9f'},
            'bar': {'color': "#00ff9f", 'thickness': 0.4},
            'bgcolor': 'rgba(0,0,0,0)',
            'borderwidth': 2,
            'bordercolor': '#00ff9f'
        }
    ))
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#00ff9f'
    )
    gauge_placeholder = st.empty()
    for i in np.linspace(0, value, 30):
        fig.data[0].value = i
        gauge_placeholder.plotly_chart(fig, use_container_width=True)
        time.sleep(0.03)

#---------------------- Assets ----------------------#
add_bg_from_local(r"D:\Crop-Fertiliser-Recommender\assets\background.png")
crop_model = joblib.load("models/crop_recommender.pkl")
st.set_page_config(page_title="🌾 Crop & Fertiliser Recommender", layout="wide")

# Title
st.markdown(""" 
<div style=" 
    position: sticky; 
    top: 0; 
    left: 0; 
    width: 100%; 
    background: rgba(0,0,0,0.7); 
    padding: 15px; 
    text-align: center; 
    font-size: 40px; 
    font-weight: bold; 
    color: #00A9f; 
    text-shadow: 0 0 3px #00A9f; 
    z-index: 999; 
"> 
 Smart Crop & Fertiliser Recommendation 
Platform 
</div> 
<div style=" 
    position: sticky; 
    top: 2.5; 
    left: 100; 
    width: 100%; 
    background: rgba(0,0,0,0.7); 
    padding: 15px; 
    text-align: center; 
    font-size: 20px; 
    font-weight: bold; 
    color: #FF0000; 
    text-shadow: 0 0 3px #00A9f; 
    z-index: 999; 
"> 
<p class='slide-left'>Provide soil & weather details to get the best crop and fertiliser suggestion.</p>
</div> 

<div style="padding-top:80px;"> <!-- Push 
content down --> 
""", unsafe_allow_html=True)

# Input Section
st.markdown("<h3 class='slide-left'>🛠 Enter Soil & Weather Parameters</h3>", unsafe_allow_html=True)
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

# Prediction
if st.button("🔍 Let's Find"):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = crop_model.predict(features)[0]
    proba = crop_model.predict_proba(features)[0]
    confidence = np.max(proba) * 100

    # Sliding prediction output
    st.markdown(f"""
    <div class='slide-right'>
        <div style="border-radius:15px; padding:15px; margin-top:10px; background: rgba(0,0,0,0.4); border:1px solid #00ff9f; color:#00ff9f;">
            <div style="font-size:20px;"> 🌱 Recommended Crop: <b>{prediction}</b></div>
            <div style="font-size:18px;"> 🦾 Model Confidence: <b>{confidence:.2f}%</b></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Charts Section
    st.markdown("<h3 class='slide-left'>📈 Soil & Weather Analysis</h3>", unsafe_allow_html=True)
    colA, colB = st.columns(2)
    with colA:
        nutrients = {"Nitrogen": N, "Phosphorus": P, "Potassium": K}
        fig = px.bar(
            x=list(nutrients.keys()), y=list(nutrients.values()),
            labels={'x': "Nutrients", 'y': "Level"},
            title="Soil Nutrient Levels",
            color=list(nutrients.values()),
            color_continuous_scale=px.colors.sequential.Turbo
        )
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#00ff9f')
        st.plotly_chart(fig, use_container_width=True)

    with colB:
        # Animated gauges
        colB1, colC1, colD1 = st.columns([1,1,1])
        with colB1:
            animated_gauge(rainfall, "Rainfall (mm)", "mm", 0, 500)
        with colC1:
            animated_gauge(temperature, "Temperature (°C)", "°C", 0, 50)
        with colD1:
            animated_gauge(humidity, "Humidity (%)", "%", 0, 100)

    # Confidence Bar
    st.markdown("<h3 class='slide-left'>🔎 Prediction Confidence Across Crops</h3>", unsafe_allow_html=True)
    conf_df = pd.DataFrame({"Crop": crop_model.classes_, "Confidence": proba})
    conf_fig = px.bar(
        conf_df.sort_values("Confidence", ascending=False),
        x="Crop", y="Confidence",
        title="Model Confidence for Each Crop",
        color="Confidence", color_continuous_scale=px.colors.sequential.Turbo
    )
    conf_fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='#00ff9f')
    st.plotly_chart(conf_fig, use_container_width=True)

# Footer
st.markdown("<div class='footer'>Developed by Aayush Raj Singh</div>", unsafe_allow_html=True)
