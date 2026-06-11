import streamlit as st
import pickle
import pandas as pd

# Load model safely
try:
    with open("heart.pkl", "rb") as file:
        model = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# App title
st.title("❤️ Heart Disease Prediction")
st.write("Enter patient details below:")

# Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=30)

sex = st.selectbox("Gender", ["Female", "Male"])
sex = 0 if sex == "Female" else 1

cp = st.selectbox(
    "Chest Pain Type",
    [
        "0 - Typical Angina",
        "1 - Atypical Angina",
        "2 - Non-anginal Pain",
        "3 - Asymptomatic"
    ]
)
cp = int(cp[0])

trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)

fbs = st.selectbox("Fasting Blood Sugar High?", ["No", "Yes"])
fbs = 0 if fbs == "No" else 1

restecg = st.selectbox("Resting ECG", ["0", "1", "2"])
restecg = int(restecg)

thalach = st.number_input("Max Heart Rate", value=150)

exang = st.selectbox("Exercise Induced Angina?", ["No", "Yes"])
exang = 0 if exang == "No" else 1

oldpeak = st.number_input("Oldpeak", value=1.0)

slope = st.selectbox("Slope", ["0", "1", "2"])
slope = int(slope)

ca = st.selectbox("Number of Major Vessels (ca)", ["0", "1", "2", "3", "4"])
ca = int(ca)

thal = st.selectbox("Thal", ["0", "1", "2", "3"])
thal = int(thal)

# Prediction button
if st.button("Predict"):
    try:
        # Must match training columns exactly
        input_data = pd.DataFrame([{
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }])

        prediction = model.predict(input_data)

        if prediction[0] == 1:
               st.success("✅ No Heart Disease")
        else:
               st.error("⚠️ Heart Disease Detected")
    except Exception as e:
        st.error(f"Prediction error: {e}")