import os
import pickle
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu

# Load models
diabetes_model = pickle.load(open('/Users/sudarshan/Documents/Code/Disease_Predictor/Models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('/Users/sudarshan/Documents/Code/Disease_Predictor/Models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('/Users/sudarshan/Documents/Code/Disease_Predictor/Models/parkinsons_model.sav', 'rb'))

# Create sidebar with logo
with st.sidebar:
    st.image("logo.png")
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           icons=["activity", "heart", "person"],
                           default_index=0)
    st.title("ChronicCare:")
    st.subheader("Disease Progression Monitoring Platform")
    st.info("This web app predicts your risk of diabetes, heart disease, or Parkinson's using machine learning from health metrics. "
            "Input your data to receive a risk assessment and track your health progression over time, aiding in early diagnosis and proactive management.")

# Function for prediction result display
def display_prediction(selected):
    if selected == 'Diabetes Prediction':
        st.title('Diabetes Prediction')

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

        diab_diagnosis = ''
        if st.button('Diabetes Test Result'):
            user_input = [float(x) for x in [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)

            # Load the data for visualization
            file_path = '/Users/sudarshan/Documents/Code/Disease_Predictor/CSV_Sample_Data/diabete_sample_patient_data.csv'
            diabetes_data = pd.read_csv(file_path)

            st.header("Diabetes Data Trends")
            st.markdown("Visualizing trends in the diabetes dataset.")

            # Streamline plots for each factor
            factors = ['Pregnancies', 'SkinThickness', 'DiabetesPedigreeFunction', 'Glucose', 'Insulin', 'Age', 'BloodPressure', 'BMI']
            titles = [
                'Number of Pregnancies', 'Skin Thickness value', 'Diabetes Pedigree Function value',
                'Glucose Level', 'Insulin Level', 'Age of the Person', 'Blood Pressure value', 'BMI value'
            ]

            for factor, title in zip(factors, titles):
                st.subheader(title)
                st.line_chart(diabetes_data[factor])

    elif selected == 'Heart Disease Prediction':
        st.title('Heart Disease Prediction')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')
        with col2:
            sex = st.text_input('Sex')
        with col3:
            cp = st.text_input('Chest Pain types')
        with col1:
            trestbps = st.text_input('Resting Blood Pressure')
        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
        with col3:
            exang = st.text_input('Exercise Induced Angina')
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')
        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        heart_diagnosis = ''
        if st.button('Heart Disease Test Result'):
            user_input = [float(x) for x in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = 'The person is having heart disease' if heart_prediction[0] == 1 else 'The person does not have any heart disease'
            st.success(heart_diagnosis)

            # Load the data for visualization
            file_path = '/Users/sudarshan/Documents/Code/Disease_Predictor/CSV_Sample_Data/heart_sample_data.csv'
            heart_data = pd.read_csv(file_path)

            st.header("Heart Disease Data Trends")
            st.markdown("Visualizing trends in the heart disease dataset.")

            # Streamline plots for each factor
            factors = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'slope', 'ca', 'thal']
            titles = [
                'Age', 'Resting Blood Pressure', 'Serum Cholestoral', 'Maximum Heart Rate achieved',
                'ST depression induced by exercise', 'Slope of the peak exercise ST segment', 'Major vessels colored by flourosopy', 'Thal'
            ]

            for factor, title in zip(factors, titles):
                st.subheader(title)
                st.line_chart(heart_data[factor])

    elif selected == "Parkinsons Prediction":
        st.title("Parkinson's Disease Prediction")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')
        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')
        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')
        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')
        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        with col1:
            RAP = st.text_input('MDVP:RAP')
        with col2:
            PPQ = st.text_input('MDVP:PPQ')
        with col3:
            DDP = st.text_input('Jitter:DDP')
        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')
        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')
        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')
        with col3:
            APQ = st.text_input('MDVP:APQ')
        with col4:
            DDA = st.text_input('Shimmer:DDA')
        with col5:
            NHR = st.text_input('NHR')
        with col1:
            HNR = st.text_input('HNR')
        with col2:
            RPDE = st.text_input('RPDE')
        with col3:
            DFA = st.text_input('DFA')
        with col4:
            spread1 = st.text_input('spread1')
        with col5:
            spread2 = st.text_input('spread2')
        with col1:
            D2 = st.text_input('D2')
        with col2:
            PPE = st.text_input('PPE')

        parkinsons_diagnosis = ''
        if st.button("Parkinson's Test Result"):
            user_input = [float(x) for x in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]]
            parkinsons_prediction = parkinsons_model.predict([user_input])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)

            # Load the data for visualization
            file_path = '/Users/sudarshan/Documents/Code/Disease_Predictor/CSV_Sample_Data/parkinsons_sample_data.csv'
            parkinsons_data = pd.read_csv(file_path)

            st.header("Parkinson's Disease Data Trends")
            st.markdown("Visualizing trends in the Parkinson's disease dataset.")

            # Streamline plots for each factor
            factors = ['MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 
                       'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 
                       'spread1', 'spread2', 'D2', 'PPE']
            titles = [
                'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 
                'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'RPDE', 'DFA', 
                'spread1', 'spread2', 'D2', 'PPE'
            ]

            for factor, title in zip(factors, titles):
                st.subheader(title)
                st.line_chart(parkinsons_data[factor])

# Display selected prediction
display_prediction(selected)

# Contact form
st.header(":male-doctor: Get In Touch With A Near By Doctor!")
contact_box_html = """
<div id="contact-box">
    <form action="https://formsubmit.co/chroniccare.help@gmail.com" method="POST">
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
</div>
"""
st.markdown(contact_box_html, unsafe_allow_html=True)

# Load CSS styles
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
