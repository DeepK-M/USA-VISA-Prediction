import streamlit as st
import numpy as np
import pickle

# Load the retrained model (ensure this is the updated file)
with open("visa_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("USA Visa Prediction App")
st.write("Enter your visa application details to predict approval:")

# Input fields for visa application details
class_of_admission = st.number_input("Class of Admission", min_value=1, value=10)
country_of_citizenship = st.number_input("Country of Citizenship", min_value=1, value=79)
employer_city = st.number_input("Employer City Code", min_value=1, value=3000)
employer_name = st.number_input("Employer Name Code", min_value=1, value=40000)
employer_state = st.number_input("Employer State Code", min_value=1, value=40)
pw_soc_code = st.number_input("SOC Code", min_value=1, value=42)
pw_source_name_9089 = st.number_input("Wage Source", min_value=1, value=3)
year = st.number_input("Application Year", min_value=1, value=3)

if st.button("Predict"):
    input_data = np.array([[class_of_admission, country_of_citizenship, employer_city, 
                            employer_name, employer_state, pw_soc_code, pw_source_name_9089, year]])
    
    # Make prediction
    prediction = model.predict(input_data)
    result = "Approved ✅" if prediction[0] == 1 else "Denied ❌"
    st.subheader(f"Prediction: {result}")
    
    # Display probability of approval
    probabilities = model.predict_proba(input_data)
    st.write("Approval Probability:", np.round(probabilities[0][1] * 100, 2), "%")
