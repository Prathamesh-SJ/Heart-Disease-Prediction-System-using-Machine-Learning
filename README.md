❤️ Heart Disease Prediction System

A Machine Learning-powered web application that predicts the likelihood of heart disease based on patient health parameters. The project uses Logistic Regression for classification and Streamlit for an interactive user interface.

📌 Features
Predicts the presence of heart disease using medical attributes.
User-friendly Streamlit interface.
Trained using Logistic Regression.
Model persistence using Pickle.
Real-time predictions.
Handles user input safely.
Beginner-friendly and easy to extend.
🛠️ Tech Stack
Technology	Purpose
Python	Programming Language
Pandas	Data Processing
NumPy	Numerical Computations
Scikit-Learn	Machine Learning
Streamlit	Web Application
Pickle	Model Serialization
📂 Dataset Information

The dataset contains 1025 patient records with 13 medical features.

Features Used
Feature	Description
age	Age of patient
sex	Gender
cp	Chest pain type
trestbps	Resting blood pressure
chol	Cholesterol level
fbs	Fasting blood sugar
restecg	Resting ECG results
thalach	Maximum heart rate achieved
exang	Exercise-induced angina
oldpeak	ST depression induced by exercise
slope	Slope of peak exercise ST segment
ca	Number of major vessels
thal	Thalassemia status
Target Variable
0 → Heart Disease Present
1 → No Heart Disease
📊 Data Analysis
Dataset Shape
(1025,14)
Missing Values
0 Missing Values
Duplicate Records
723 Duplicate Rows Found
🤖 Machine Learning Model
Algorithm Used
Logistic Regression
Data Split
80% Training
20% Testing
Model Performance
Metric	Score
Training Accuracy	85.85%
Testing Accuracy	81.46%
💾 Model Saving

The trained model is stored using Pickle.

with open("heart.pkl","wb") as file:
    pickle.dump(model,file)
🖥️ Streamlit Application

The application allows users to enter patient details such as:

Age
Gender
Chest Pain Type
Cholesterol
Blood Pressure
ECG Results
Heart Rate
Exercise Induced Angina
Number of Major Vessels
Thalassemia Status

After clicking Predict, the model determines whether heart disease is likely to be present.
