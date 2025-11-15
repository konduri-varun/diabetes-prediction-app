# Diabetes Prediction Web App
<img width="1885" height="855" alt="image" src="https://github.com/user-attachments/assets/db09bafc-233d-4d66-a016-de225dfbdc34" />

A machine learning web application for predicting diabetes risk based on medical data using Support Vector Machine (SVM).

## 🩺 Overview

This app uses a trained SVM model to predict whether a person is at risk of diabetes based on key health metrics. The model was trained on the Pima Indians Diabetes Dataset and achieves approximately 76% accuracy on test data.

## 🚀 Features

- **User-Friendly Interface**: Clean, professional UI built with Streamlit
- **Real-Time Predictions**: Input medical data and get instant predictions
- **Confidence Scores**: Provides decision function scores for prediction confidence
- **Responsive Design**: Works on desktop and mobile devices
- **Medical Disclaimer**: Includes important health advisory

## 📋 Requirements

- Python 3.7+
- Libraries listed in `requiremnets.txt`

## 🛠️ Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requiremnets.txt
   ```

## 🎯 Usage

### Local Development
Run the app locally:
```bash
streamlit run app.py
```
Access at `http://localhost:8501`

### Input Features
- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration (mg/dL)
- **Blood Pressure**: Diastolic blood pressure (mm Hg)
- **Skin Thickness**: Triceps skin fold thickness (mm)
- **Insulin**: 2-Hour serum insulin (μU/mL)
- **BMI**: Body mass index
- **Diabetes Pedigree Function**: Diabetes pedigree function value
- **Age**: Age in years

## 📊 Model Details

- **Algorithm**: Support Vector Machine with linear kernel
- **Preprocessing**: Feature standardization using StandardScaler
- **Training Data**: 80% of dataset
- **Test Accuracy**: ~76%

## 🌐 Deployment

### Streamlit Cloud (Recommended)
1. Upload files to a GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo and deploy

### Other Platforms
- **Heroku**: Use the included `Procfile`
- **AWS/Docker**: Containerize with Docker

## 📁 Project Structure

```
├── app.py                 # Main Streamlit application
├── Diabetes_Prediction.ipynb  # Jupyter notebook with model training
├── diabetes.csv           # Dataset (optional)
├── model.pkl              # Trained SVM model
├── scaler.pkl             # Feature scaler
├── requiremnets.txt       # Python dependencies
└── README.md              # This file
```

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements.

## 📄 License

This project is open-source. Feel free to use and modify as needed.
