import streamlit as st
import numpy as np
from prediction import predict

st.title("Welcome to the Hearth Disease Prediction app")
st.markdown('''
            This is a ML project that was developed to try to predict if a person can suffer from a hearth disease based on some characterisitcs.  
            This prediction is the result of the analysis of different algorithms.  
            You can see the whole process on my [Colab document](https://colab.research.google.com/drive/1KckOFTWpFDDxJoAZU9tgZoxpORtB_0FH?usp=drive_link).
            
''')

st.subheader("Prediction")
st.markdown('''
            Please select all the values for the different parameters to see the prediction of our algorithm.  
            Consider the following for the parameters:  
            - Sex: 0 - Female, 1 - Male  
            - Chest pain Type: 1 - typical angina, 2 - atypical angina, 3 - non-anginal pain, 4 - asymptomatic  
            - Fasting blood sugar: FBS > 120 mg/dl - 1, FBS < or  = to 120 mg/dl - 0
            - Resting electrocardiogram results: Normal - 0, having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) - 1, 
             showing probable or definite left ventricular hypertrophy by Estes' criteria - 2.  
            - Excercise indced angina: 1- Yes, 0- No.  
            - The slope of the peak exercise ST segment: 1 - upsloping, 2 - flat, 3 - downsloping.  
            - Thalassemia: 3 - normal,  6 - fixed defect, 7 - reversable defect.
''')

age = st.number_input('Age', min_value=0)
sex = st.selectbox('Sex', [0, 1])
cp = st.selectbox('Chest pain type', [1, 2, 3, 4])
trestbps = st.number_input('Resting blood pressure')
chol = st.number_input('Serum cholestoral in mg/dl')
fbs = st.selectbox('Fasting blood sugar > 120 mg/dl', [0, 1])
restecg = st.selectbox('Resting electrocardiographic results', [0, 1, 2])
thalach = st.number_input('Maximum heart rate achieved', min_value=0)
exang = st.selectbox('Exercise induced angina (1 = yes; 0 = no)', [0, 1])
oldpeak = st.number_input('ST depression induced by exercise relative to rest')
slope = st.selectbox('The slope of the peak exercise ST segment', [1, 2, 3])
ca = st.selectbox('Number of major vessels (0-3) colored by flourosopy', [0, 1, 2, 3])
thal = st.selectbox('Thalassemia ', [3, 6, 7])


X = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

if st.button('Obtener Prediccion'):
    result = predict(X)
    if result[0] == 0:
        st.text('There is NOT a hearth disease')
    else:
        st.text('There IS evidence of the existence of a hearth disease')

