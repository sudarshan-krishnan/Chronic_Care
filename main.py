import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# # loading 3 saved model

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

    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')

if selected == 'Heart Disease Prediction':
   
    # page title
    st.title('Heart Disease Prediction using ML')

if selected == 'Parkinsons Prediction':
    
    # page title
    st.title('Parkinsons Prediction using ML')
