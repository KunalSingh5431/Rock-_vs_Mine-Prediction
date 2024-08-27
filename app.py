import streamlit as st
import pandas as pd
import pickle
import numpy as np

model = pickle.load(open('C:/Users/LENOVO/Music/ML Projects/Rock_vs_Mine/rockmine_model.sav', 'rb'))

st.markdown(
    """
    <style>
    .stNumberInput>div {
        margin-bottom: 15px; /* Add space between input fields */
    }
    
    .input-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    .input-block {
        flex: 1 1 30%; /* Adjust this value to control the width of the input blocks */
        margin: 10px;
    }


    .stButton>button {
        color: #4CAF50; /* Green text */
        background-color: black; /* Black background */
        border: 2px solid #4CAF50; /* Green border */
        padding: 10px 24px; /* Some padding */
        text-align: center; /* Center the text */
        text-decoration: none; /* Remove underline */
        display: inline-block; /* Display inline */
        font-size: 16px; /* Increase font size */
        margin: 4px 2px; /* Some margin */
        cursor: pointer; /* Pointer/hand icon on hover */
        border-radius: 12px; /* Rounded corners */
    }

    .stButton>button:hover {
        background-color: #4CAF50; /* Green background on hover */
        color: white; /* White text on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h1 style="color:#4CAF50; text-align:center;">Rock vs Mine Prediction System</h1>
    <h3 style="text-align:center;">Using Sonar Signal Data</h3>
    """, 
    unsafe_allow_html=True
)


st.markdown(
    """
    <h4 style="color:white; text-align:center;">Enter the 60 features to predict whether it's a Rock or a Mine:</h4>
    """, 
    unsafe_allow_html=True
)

cols = st.columns(6) 
user_input = []

for i in range(60):
    with cols[i % 6]:  
        user_input.append(st.number_input(f'Feature {i+1}', min_value=0.0, max_value=1.0))

st.markdown("<br>", unsafe_allow_html=True)


if st.button('Predict 🚀'):
    user_data = np.array(user_input).reshape(1, -1)
    prediction = model.predict(user_data)
    
    result = 'Mine' if prediction[0] == 'M' else 'Rock'
    
   
    st.markdown(f"""
    <h2 style="text-align:center;">The object is predicted to be a:</h2>
    <h1 style="color:#FF6347; text-align:center;">{result}</h1>
    """, unsafe_allow_html=True)
