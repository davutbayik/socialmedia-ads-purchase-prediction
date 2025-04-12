import streamlit as st
import requests

# Streamlit page title
st.title("🌐 Social Network Ads Prediction")

# Collecting user input for prediction
st.header("Enter user details")

# Gender input
gender = st.selectbox("Gender", options=["Male", "Female"])

# Age input
age = st.slider("Age", min_value=18, max_value=100, value=30)

# Estimated Salary input
salary = st.slider("Estimated Salary", min_value=15000, max_value=150000, value=50000)

# Button to trigger prediction
predict_button = st.button("Predict Purchase")

# API URL for FastAPI

#API_URL = "http://localhost:8000/predict" # For local deploy
API_URL = "https://socialmedia-ads-predictor-fastapi.streamlit.app/predict" # For streamlit deploy

# If the button is clicked, send the data to the FastAPI model
if predict_button:
    # Prepare the data for prediction
    features = {
        "Gender": gender,
        "Age": age,
        "EstimatedSalary": salary
    }
    
    response = requests.post(API_URL, json=features)

    try:
        result = response.json()
        st.success(f"Social Media Ads --> {result['purchase']}")
    except Exception as e:
        st.error("Failed to decode JSON from API response.")
        st.error(str(e))