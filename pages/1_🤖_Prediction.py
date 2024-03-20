import streamlit as st
import numpy as np
from prediction import predict

st.set_page_config(
    page_title="Prediction",
    page_icon="🤖",
)


st.subheader("Prediction")
st.markdown('''
            Please select all the values for the different parameters to see the prediction of our algorithm.  
''')

age = st.number_input('Age', min_value=0)
sex = st.selectbox('Sex', ['Female', 'Male'], index=None, placeholder="Please select an option...")
cp = st.selectbox('Chest pain type', ['Typical angina', 'Atypical angina', 'Non-anginal pain', 'Asymptomatic'], index=None, placeholder="Please select an option...")
trestbps = st.number_input('Resting blood pressure (mm Hg)')
chol = st.number_input('Serum cholesterol (mg/dl)')
fbs = st.selectbox('Is fasting blood sugar > 120 mg/dl?', ['No', 'Yes'], index=None, placeholder='Please select an option...')
restecg = st.selectbox('Resting electrocardiographic results', ['Normal', 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'Showing probable or definite left ventricular hypertrophy by Estes criteria'], index=None, placeholder="Please select an option...")
thalach = st.number_input('Maximum heart rate achieved (bpm)', min_value=0)
exang = st.selectbox('Was there exercise induced angina?', ['No', 'Yes'], index=None, placeholder="Please select an option...")
oldpeak = st.number_input('ST depression induced by exercise relative to rest')
slope = st.selectbox('The slope of the peak exercise ST segment', ['Upsloping', 'Flat', 'Downsloping'], index=None, placeholder="Please select an option...")
ca = st.selectbox('Number of major vessels (0-3) colored by flourosopy', [0, 1, 2, 3], index=None, placeholder="Please select an option...")
thal = st.selectbox('Thalassemia ', ['Normal', 'Fixed defect', 'Reversable defect'], index=None, placeholder="Please select an option...")

set_sex = 0
set_cp = 0
set_fbs = 0
set_restecg = 0
set_exang = 0
set_slope = 0
set_thal = 0

if sex == 'Female':
    set_sex = 0
else:
    set_sex = 1

if cp == 'Typical angina':
    set_cp = 1
elif cp == 'Atypical angina':
    set_cp = 2
elif cp == 'Non-anginal pain':
    set_cp = 3
else:
    set_cp = 4

if fbs == 'No':
    set_fbs = 0
else:
    set_fbs = 1

if restecg == 'Normal':
    set_restecg = 0
elif restecg == 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV':
    set_restecg = 1
else:
    set_restecg = 2

if exang == 'No':
    set_exang = 0
else:
    set_exang = 1

if slope == 'Upsloping':
    set_slope = 1
elif slope == 'Flat':
    set_slope = 2
else:
    set_slope= 3

if thal == 'Normal':
    set_thal = 3
elif thal == 'Fixed defect':
    set_thal = 6
else:
    set_thal = 7
    

X = np.array([[age, set_sex, set_cp, trestbps, chol, set_fbs, set_restecg, thalach, set_exang, oldpeak, set_slope, ca, set_thal]])

if st.button('Obtener Prediccion'):
    result = predict(X)
    if result[0] == 0:
        st.markdown('''There is NO evidence of a hearth disease''')
    else:
        st.markdown('''There IS evidence of the existence of a hearth disease''')
