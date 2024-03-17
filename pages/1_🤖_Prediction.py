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
            Consider the following for the parameters:  
            - Sex:  
              - 0 :arrow_right: Female. 
              - 1 :arrow_right: Male.  
            - Chest pain type:  
              - 1 :arrow_right: Typical angina.  
              - 2 :arrow_right: Atypical angina.  
              - 3 :arrow_right: Non-anginal pain.  
              - 4 :arrow_right: Asymptomatic.  
            - Fasting blood sugar:  
              - 1 :arrow_right: FBS > 120 mg/dl.
              - 0 :arrow_right: FBS < = 120 mg/dl.
            - Resting electrocardiogram results:  
              - 0 :arrow_right: Normal.
              - 1 :arrow_right: Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV).  
              - 2 :arrow_right: Showing probable or definite left ventricular hypertrophy by Estes' criteria.  
            - Excercise induced angina:  
              - 1 :arrow_right: Yes.  
              - 0 :arrow_right: No.  
            - The slope of the peak exercise ST segment:  
              - 1 :arrow_right: Upsloping.  
              - 2 :arrow_right: Flat.  
              - 3 :arrow_right: Downsloping.  
            - Thalassemia:  
              - 3 :arrow_right: Normal.  
              - 6 :arrow_right: Fixed defect.  
              - 7 :arrow_right: Reversable defect.
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
        st.markdown('''There is NO evidence of a hearth disease''')
    else:
        st.markdown('''There IS evidence of the existence of a hearth disease''')
