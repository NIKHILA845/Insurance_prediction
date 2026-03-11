import streamlit as st
from src.prediction import Insurance_Prediction
st.title("Insurance Prediction")
st.write("Description about your project")

Age=st.number_input("Enter Age: ",min_value=0,max_value=120)
Annual_Income_LPA=st.number_input("Enter Annual_Income in LPA",min_value=0)
Policy_Term_Years=st.number_input("Enter policy terms in years",min_value=0)
Sum_Assured_Lakhs=st.number_input("Enter sum assured in lakhs",min_value=0)

if(st.button("Predict")):
    insurance_prediction=Insurance_Prediction()
    result=insurance_prediction.prediction(Age,Annual_Income_LPA,Policy_Term_Years,Sum_Assured_Lakhs)
    st.success(result)