import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from PIL import Image

def load_model():
    pickle_in = open("model.pkl","rb")
    model=pickle.load(pickle_in)
    return model  # Add this line to return the model


def predict_hr_attrition(age, distance_from_home, monthly_income, percent_salary_hike, total_working_years, model):
    """
    Predict HR attrition based on input parameters.
    """
    prediction = model.predict_proba([[age, distance_from_home, monthly_income, percent_salary_hike, total_working_years]])
    attrition_probability = prediction[0][1] * 100
    return attrition_probability


def main():
    st.title("HR Attrition")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit HR Attrition ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    age = st.number_input("Age", value=0, min_value=0)
    distance_from_home = st.number_input("Distance From Home", value=0, min_value=0)
    monthly_income = st.number_input("Monthly Income", value=0, min_value=0)
    percent_salary_hike = st.number_input("Percent Salary Hike", value=0, min_value=0)
    total_working_years = st.number_input("Total Working Years", value=0, min_value=0)
    
    result = None  # Change this line to initialize result as None
    model = load_model()
    
    if st.button("Predict"):
        result = predict_hr_attrition(age, distance_from_home, monthly_income, percent_salary_hike, total_working_years, model)
    
    if result is not None:  # Add this line to only show the output when result is not None
        st.success(f"The probability of attrition is {result:.2f}%")
    
    if st.button("About"):
        st.text("Let's Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()
