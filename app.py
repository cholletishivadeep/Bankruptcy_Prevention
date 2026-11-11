import numpy as np
import pandas as pd
import joblib
import streamlit as st

st.set_page_config(
    page_title='Bankruptcy Prevention System',
    page_icon='📊',
    layout='wide'
)
# Load model
model = joblib.load("bankruptcy_model.pkl")

# sidebar Navigation
st.sidebar.title('🏦 Bankruptcy Prevention System')
menu = st.sidebar.radio(
    "Navigation",
    ["Prediction", "About Project", "Model Information"])

# feature names
features = [
    "industrial_risk",
    "management_risk",
    "financial_flexibility",
    "credibility",
    "competitiveness",
    "operating_risk"
]
if menu == 'Prediction':
 st.title("🏦 BANKRUPTCY PREVENTION SYSTEM")
 st.markdown("""
  This application predicts whether a company is likely to face bankruptcy
  based on six business risk factors.
  """)
 
 st.divider()

 st.write("Enter company risk factors below:")

 st.divider()

 col1,col2=st.columns(2)

 with col1:
    industrial_risk = st.number_input(
        "Industrial Risk", min_value=0.0, max_value=1.0,step=0.5
    )
    management_risk = st.number_input(
        "Management Risk", min_value=0.0, max_value=1.0,step=0.5
    )
    financial_flexibility = st.number_input(
        "Financial Flexibility", min_value=0.0, max_value=1.0,step=0.5)
 with col2:
    credibility = st.number_input("Credibility", min_value=0.0,  max_value=1.0,step=0.5)
    competitiveness = st.number_input("Competitiveness", min_value=0.0,  max_value=1.0,step=0.5)
    operating_risk = st.number_input("Operating Risk", min_value=0.0,  max_value=1.0,step=0.5)

 st.divider()
 #   Prediction
 if st.button("🔍 Predict Bankruptcy",use_container_width=True):

    data = pd.DataFrame([{
        "industrial_risk": industrial_risk,
        "management_risk": management_risk,
        "financial_flexibility": financial_flexibility,
        "credibility": credibility,
        "competitiveness": competitiveness,
        "operating_risk": operating_risk
    }])

    prediction = model.predict(data)
    
    # Display the Results

    st.subheader('Prediction Result')

    if prediction[0] == 0:
        st.error("⚠️ Bankruptcy")
    else:
        st.success("✅ Non-Bankruptcy")

    st.divider()

    #7. Prediction Probability
    # --------------------------------

    if hasattr(model, "predict_proba"):

      probabilities = model.predict_proba(data)[0]

    bankruptcy_probability = probabilities[
        list(model.classes_).index(0)
    ]

    non_bankruptcy_probability = probabilities[
        list(model.classes_).index(1)
    ]

    st.metric(
        "Bankruptcy Probability",
        f"{bankruptcy_probability * 100:.2f}%"
    )

    st.metric(
        "Non-Bankruptcy Probability",
        f"{non_bankruptcy_probability * 100:.2f}%"
    )
   
    st.divider()

 # Input Summary

    st.subheader("Company Risk Factor Summary")

    summary = pd.DataFrame({
        "Risk Factor": features,
        "Selected Level": [
            industrial_risk,
            management_risk,
            financial_flexibility,
            credibility,
            competitiveness,
            operating_risk
        ]
    })

    st.dataframe(summary, use_container_width=True)

    st.divider()
    st.info("Bankruptcy Prevention System | Machine Learning Classification Project")

elif menu == 'About Project':

   st.title('About Project')
   st.write(""" The objective of this project is to predict whether
    a company is likely to face bankruptcy based on
    six business risk factors.
    """)
   st.write("**Dataset:** Bankruptcy Prevention Dataset")
   st.write("**Total Records:** 250")
   st.write("**Input Features:** 6")
   st.write("**Problem Type:** Binary Classification")

# Model Information
elif menu == "Model Information":

    st.title("Model Information")

    st.write("This application uses a trained Machine Learning model.")

    st.subheader("Target Encoding")

    st.write("0 = Bankruptcy")
    st.write("1 = Non-Bankruptcy")

    st.info("The model predicts the company's bankruptcy status using six risk factors.")