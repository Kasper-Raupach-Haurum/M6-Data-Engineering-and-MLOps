import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("model.pkl","rb")
model=pickle.load(pickle_in)


def predict_HR(mae,rmse,r2):
    
    """Let's Authenticate the Attrition 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: mae
        in: query
        type: number
        required: true
      - name: rmse
        in: query
        type: number
        required: true
      - name: r2
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=model.predict([[mae,rmse,r2]])
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
    variance = st.text_input("mae","Type Here")
    skewness = st.text_input("rmse","Type Here")
    curtosis = st.text_input("r2","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_HR(0, 1, 0.5)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
