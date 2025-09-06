import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

st.title("🔮 SaaS Churn Prediction Demo")

st.write("Enter customer usage details to predict churn:")

# Input fields
logins = st.number_input("Average logins per week", min_value=0, max_value=50, value=3)
tickets = st.number_input("Number of support tickets", min_value=0, max_value=20, value=1)
months = st.number_input("Months as customer", min_value=0, max_value=60, value=12)

if st.button("Predict Churn"):
    features = np.array([[logins, tickets, months]])
    prediction = model.predict(features)
    if prediction[0] == 1:
        st.error("⚠️ This customer is likely to churn!")
    else:
        st.success("✅ This customer is likely to stay.")
