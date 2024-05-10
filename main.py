import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading 3 saved model

# diabetes_model = pickle.load(open('/Users/sudarshan/Documents/Code/Disease_Predictor/saved_models/diabetes_model.sav' , 'wb'))

# heart_model = pickle.load(open('/Users/sudarshan/Documents/Code/Disease_Predictor/saved_models/heart_disease_model.sav', 'wb'))

# parkinsons_model = pickle.load(open('/Users/sudarshan/Documents/Code/Disease_Predictor/saved_models/parkinsons_model.sav', 'wb'))

# creating sidebar

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System Using ML' , 
                           ['Diabetes Prediction' , 'Heart Disease Prediction' , 'Parkinsons Prediction'] ,
                           icons = ["activity" , "heart" , "person"] ,
                           default_index=0)
    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)



if selected == 'Heart Disease Prediction':
   
    # page title
    st.title('Heart Disease Prediction using ML')

if selected == 'Parkinsons Prediction':
    
    # page title
    st.title('Parkinsons Prediction using ML')
