import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)


def predict_HR(Age,DistanceFromHome,MonthlyIncome,PercentSalaryHike,TotalWorkingYears):
    
    """Let's Authenticate the Attrition 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: DistanceFromHome
        in: query
        type: number
        required: true
      - name: MonthlyIncome
        in: query
        type: number
        required: true
      - name: PercentSalaryHike
        in: query
        type: number
        required: true
      - name: TotalWorkingYears
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=model.predict([[Age,DistanceFromHome,MonthlyIncome,PercentSalaryHike,TotalWorkingYears]])
    print(prediction)
    return prediction



def main():
    st.title("HR Attrition")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit HR Attrition ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.text_input("Age","Type Here")
    DistanceFromHome = st.text_input("DistanceFromHome","Type Here")
    MonthlyIncome = st.text_input("MonthlyIncome","Type Here")
    PercentSalaryHike = st.text_input("PercentSalaryHike","Type Here")
    TotalWorkingYears = st.text_input("TotalWorkingYears","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_HR(0, 1, 2, 3, 4)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()