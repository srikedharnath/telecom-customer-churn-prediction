import streamlit as st
import pickle
import pandas as pd


with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)


st.markdown(
    "<h1 style='color:blue;'>📊 Customer Churn Prediction</h1>",
    unsafe_allow_html=True
)


senior = st.selectbox("Senior Citizen", [0, 1])

tenure = st.slider("Tenure", 0, 72)

monthly = st.number_input("Monthly Charges")

total = st.number_input("Total Charges")


if st.button("Predict"):

    
    input_data = pd.DataFrame({
        'SeniorCitizen': [senior],
        'tenure': [tenure],
        'MonthlyCharges': [monthly],
        'TotalCharges': [total]
    })

    
    prediction = model.predict(input_data)

    
    probability = model.predict_proba(input_data)

    
    if prediction[0] == 1:
        st.error("⚠ Customer Will Leave")
    else:
        st.success("✅ Customer Will Stay")

