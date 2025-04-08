import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open("visa_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page config
st.set_page_config(page_title="USA Visa Prediction", page_icon="🇺🇸", layout="centered")

# Sidebar
st.sidebar.title("ℹ️ About")
st.sidebar.info("""
This AI tool predicts whether a USA visa application will be **approved** or **denied**, based on historical patterns.

> **Note**: These results are for informational purposes only and do not guarantee any outcome.
""")

# Main Title
st.markdown(
    "<h1 style='text-align: center; color: #0c4a6e;'>USA Visa Prediction App</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("### 📝 Enter your visa application details below:")

# Layout with 2 columns
col1, col2 = st.columns(2)

with col1:
    class_of_admission = st.number_input("📘 Class of Admission", min_value=1, value=10, help="Visa class numeric code")
    employer_name = st.number_input("🏢 Employer Name Code", min_value=1, value=40000, help="Numeric code of the employer")
    employer_state = st.number_input("🌎 Employer State Code", min_value=1, value=40, help="State code where the employer is located")
    pw_source_name_9089 = st.number_input("📄 Wage Source Code", min_value=1, value=3, help="Source code used for wage determination")

with col2:
    country_of_citizenship = st.number_input("🌍 Country of Citizenship", min_value=1, value=79, help="Country code of applicant")
    employer_city = st.number_input("🏙️ Employer City Code", min_value=1, value=3000, help="City code of employer")
    pw_soc_code = st.number_input("💼 SOC Code", min_value=1, value=42, help="Standard Occupation Classification code")
    year = st.number_input("📅 Application Year", min_value=1, value=3, help="Year of the application")

st.markdown("")

# Predict button
predict_btn = st.button("🔍 Predict")

if predict_btn:
    input_data = np.array([[class_of_admission, country_of_citizenship, employer_city, 
                            employer_name, employer_state, pw_soc_code, pw_source_name_9089, year]])
    
    try:
        prediction = model.predict(input_data)
        probabilities = model.predict_proba(input_data)
        result = "✅ Approved" if prediction[0] == 1 else "❌ Denied"

        st.success(f"### 🎯 Prediction: {result}")
        st.info(f"**Approval Probability:** `{np.round(probabilities[0][1] * 100, 2)}%`")

    except Exception as e:
        st.error(f"An error occurred while making prediction: {e}")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center;'>Made with ❤️ using Streamlit | © 2025</div>", unsafe_allow_html=True)
