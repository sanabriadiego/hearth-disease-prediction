import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

st.title("Welcome to the Heart Disease Prediction app :stethoscope:")
st.image('./imgs/hearth_cover.png', caption='Diagnosing a hearth disease is very important for a patient')
st.markdown('''  
            According to the British Heart Foundation, there are around 620 million people living with heart and circulatory diseases across the world, this number has been
            rising due to changing lifestyles, an ageing and growing population, and improved survival rates from heart attacks and
            strokes, and will continue to rise if these trends continue.  
            Each year around 60 million people across the world develop a heart or circulatory disease, that's almost the same as the entire
            population of the UK.  
            For that reason it would be easier for doctors to detect a hearth disease on their patients, that way they can provide them a better treatment, with more time for them.
            This is a Machine Learning project that was developed to try to predict if a person can suffer from a hearth disease based on some parameters. 
            You can see the whole process on my [Colab document](https://colab.research.google.com/drive/1KckOFTWpFDDxJoAZU9tgZoxpORtB_0FH?usp=drive_link).
            
''')