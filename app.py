import streamlit as st
import joblib
import numpy as np
 
# Load the trained model
model = joblib.load('model.pkl') 
 
# Title
st.title("Heart Disease Prediction") 
 
# Input Features
st.header("Input Features")
age = st.number_input("Age", value=0.0)
sex = st.number_input("Sex (1=Male, 0=Female)", value=0.0)
cp = st.number_input("Chest Pain Type (0-3)", value=0.0)
trestbps = st.number_input("Resting Blood Pressure", value=0.0)
chol = st.number_input("Cholesterol", value=0.0)
fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", value=0.0)
restecg = st.number_input("Resting ECG Results (0-2)", value=0.0)
thalach = st.number_input("Maximum Heart Rate Achieved", value=0.0)
exang = st.number_input("Exercise Induced Angina (1=Yes, 0=No)", value=0.0)
oldpeak = st.number_input("ST Depression Induced by Exercise", value=0.0)
slope = st.number_input("Slope of the Peak Exercise ST Segment (0-2)", value=0.0)
ca = st.number_input("Number of Major Vessels Colored by Fluoroscopy (0-3)", value=0.0)
thal = st.number_input("Thalassemia (1-3)", value=0.0)
 
 
if st.button("Predict"):
    # Create input array
    inputs = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])  
    prediction = model.predict(inputs)
    st.success(f"Prediction: {prediction[0]}")  