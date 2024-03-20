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
            Take into consideration that our algorithm has an accuracy of 90%.
''')

set_sex = {'Female': 0, 'Male': 1}
set_cp = {'Typical angina': 1, 'Atypical angina': 2, 'Non-anginal pain': 3, 'Asymptomatic': 4}
set_fbs = set_exang = {'No': 0, 'Yes': 1}
set_restecg = {'Normal': 0, 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV': 1, 'Showing probable or definite left ventricular hypertrophy by Estes criteria': 2}
set_slope = {'Upsloping': 1, 'Flat': 2, 'Downsloping': 3}
set_thal = {'Normal': 3, 'Fixed defect': 6, 'Reversable defect': 7}

age = st.number_input('Age', min_value=0)
sex = st.selectbox('Sex', list(set_sex), index=None, placeholder='Please select an option...')
cp = st.selectbox('Chest pain type', list(set_cp), index=None, placeholder="Please select an option...")
trestbps = st.number_input('Resting blood pressure (mm Hg)')
chol = st.number_input('Serum cholesterol (mg/dl)')
fbs = st.selectbox('Is fasting blood sugar > 120 mg/dl?', list(set_fbs), index=None, placeholder='Please select an option...')
restecg = st.selectbox('Resting electrocardiographic results', list(set_restecg), index=None, placeholder="Please select an option...")
thalach = st.number_input('Maximum heart rate achieved (bpm)', min_value=0)
exang = st.selectbox('Was there exercise induced angina?', list(set_exang), index=None, placeholder="Please select an option...")
oldpeak = st.number_input('ST depression induced by exercise relative to rest')
slope = st.selectbox('The slope of the peak exercise ST segment', list(set_slope), index=None, placeholder="Please select an option...")
ca = st.selectbox('Number of major vessels (0-3) colored by flourosopy', [0, 1, 2, 3], index=None, placeholder="Please select an option...")
thal = st.selectbox('Thalassemia ', ['Normal', 'Fixed defect', 'Reversable defect'], index=None, placeholder="Please select an option...")

try:
  if st.button('Get Prediction', type='primary'):
    X = np.array([[age, set_sex[sex], set_cp[cp], trestbps, chol, set_fbs[fbs], set_restecg[restecg], thalach, set_exang[exang], oldpeak, set_slope[slope], ca, set_thal[thal]]])
    result = predict(X)
    if result[0] == 0:
        st.markdown('''There is NO evidence of a hearth disease''')
    else:
        st.markdown('''There IS evidence of the existence of a hearth disease''')
except:
  st.write('Please fill in all the fields')
   