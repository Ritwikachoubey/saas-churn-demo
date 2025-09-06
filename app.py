import streamlit as st
import pickle

st.title("Display Pickle Data")

# Load the pickle file
with open("my_data.pkl", "rb") as f:
    data = pickle.load(f)

st.write("Here is the data from my_data.pkl:")
st.write(data)
st.success("Pickle file loaded successfully!")
