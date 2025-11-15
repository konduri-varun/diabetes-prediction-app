import streamlit as st
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

# Custom CSS for professional styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stTextInput, .stNumberInput {
        margin-bottom: 10px;
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and header
st.title('🩺 Diabetes Prediction Web App')
st.markdown("---")

# Sidebar for additional info
with st.sidebar:
    st.header('ℹ️ About')
    st.write('This app uses a machine learning model to predict diabetes based on medical data.')
    st.markdown("---")

# Main content
st.subheader('Enter Patient Details')
st.write('Please provide the following medical information for prediction:')

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, value=1, step=1, help='Number of times pregnant')
    glucose = st.number_input('Glucose Level (mg/dL)', min_value=0, max_value=200, value=120, step=1, help='Plasma glucose concentration')
    blood_pressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=150, value=70, step=1, help='Diastolic blood pressure')
    skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=100, value=20, step=1, help='Triceps skin fold thickness')

with col2:
    insulin = st.number_input('Insulin Level (μU/mL)', min_value=0, max_value=900, value=80, step=1, help='2-Hour serum insulin')
    bmi = st.number_input('BMI', min_value=0.0, max_value=70.0, value=25.0, step=0.1, help='Body mass index')
    diabetes_pedigree = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0, value=0.5, step=0.01, help='Diabetes pedigree function')
    age = st.number_input('Age (years)', min_value=0, max_value=120, value=30, step=1, help='Age in years')

# Prediction button
st.markdown("---")
if st.button('🔍 Predict Diabetes Risk'):
    # Prepare input data
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
    
    # Standardize the input
    standardized_input = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(standardized_input)
    prediction_proba = model.decision_function(standardized_input)  # For confidence
    
    # Display result with professional styling
    st.markdown("### Prediction Result")
    if prediction[0] == 1:
        st.error('⚠️ **High Risk:** The model predicts diabetes. Please consult a healthcare professional.')
        st.write(f'**Confidence Score:** {prediction_proba[0]:.2f} (higher values indicate stronger prediction)')
    else:
        st.success('✅ **Low Risk:** The model predicts no diabetes. Maintain a healthy lifestyle!')
        st.write(f'**Confidence Score:** {prediction_proba[0]:.2f} (lower values indicate stronger prediction)')

# Footer
st.markdown("---")
st.markdown("*Disclaimer: This is not a medical diagnosis. Always consult with a qualified healthcare provider for medical advice.*")