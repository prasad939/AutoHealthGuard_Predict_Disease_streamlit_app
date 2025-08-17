# -*- coding: utf-8 
"""
Created on sunday may 22 12:24:25 2025

@author: prasad
"""
 

import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open("C:/Users/mrpra/OneDrive/Desktop/HealthGuard_Predict_ml_web_app/saved/trained_diabetic_model.sav", "rb"))
heart_model = pickle.load(open("C:/Users/mrpra/OneDrive/Desktop/HealthGuard_Predict_ml_web_app/saved/trained_heart_model.sav ", "rb"))
parkinson_model = pickle.load(open("C:/Users/mrpra/OneDrive/Desktop/HealthGuard_Predict_ml_web_app/saved/trained_parkinson_model.sav ", "rb"))

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        ['Diabetes Prediction', "Heart Disease Prediction", 'Parkinson Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', key="diab_preg")
    with col2:
        Glucose = st.text_input('Glucose Level', key="diab_glucose")
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value', key="diab_bp")
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value', key="diab_skin")
    with col2:
        Insulin = st.text_input('Insulin Value', key="diab_insulin")
    with col3:
        BMI = st.text_input('BMI value', key="diab_bmi")
    with col2:
        DiabetesPedigreeFunction = st.text_input('Diabetes pedigree Function Value', key="diab_pedigree")
    with col1:
        Age = st.text_input('Age of the Person', key="diab_age")
        
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

 
     
# Heart Disease Prediction Page
elif selected == 'Heart Disease Prediction':
    st.title("Heart Disease Prediction using ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age', key="heart_age")
    with col2:
        sex = st.text_input('Sex', key="heart_sex")
    with col3:
        cp = st.text_input('Chest pain types', key="heart_cp")
    with col1:
        trestbps = st.text_input('Resting blood Pressure', key="heart_bp")
    with col2:
        chol = st.text_input('Serum cholestrol in mg/dl', key="heart_chol")
    with col3:
        fbs = st.text_input('Fasting blood sugar', key="heart_fbs")
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results', key="heart_ecg")
    with col2:
        thalanch = st.text_input('Maximum heart rate achieved', key="heart_thalach")
    with col3:
        exang = st.text_input('Exercised induced angina', key="heart_exang")      
    with col1:
        oldpeak = st.text_input('ST depression Induced by exercise', key="heart_oldpeak")
    with col2:
        slope = st.text_input('Slope of peak exercise ST segment', key="heart_slope")
    with col3:
        ca = st.text_input('Major vessels colored by fluoroscopy', key="heart_ca") 
    with col1:
        thal= st.text_input('Thal: 0=normal; 1=fixed defect; 2=reversible defect', key="heart_thal")
    
 #code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalanch, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction =heart_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
    
    
    
# Parkinson's Prediction Page
elif selected == "Parkinson Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', key="park_fo")
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', key="park_fhi")
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', key="park_flo")
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', key="park_jitter_pct")
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', key="park_jitter_abs")
    with col1:
        RAP = st.text_input('MDVP:RAP', key="park_rap")
    with col2:
        PPQ = st.text_input('MDVP:PPQ', key="park_ppq")
    with col3:
        DDP = st.text_input('Jitter:DDP', key="park_ddp")
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', key="park_shimmer")
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', key="park_shimmer_db")
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', key="park_apq3")
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', key="park_apq5")
    with col3:
        APQ = st.text_input('MDVP:APQ', key="park_apq")
    with col4:
        DDA = st.text_input('Shimmer:DDA', key="park_dda")
    with col5:
        NHR = st.text_input('NHR', key="park_nhr")
    with col1:
        HNR = st.text_input('HNR', key="park_hnr")
    with col2:
        RPDE = st.text_input('RPDE', key="park_rpde")
    with col3:
        DFA = st.text_input('DFA', key="park_dfa")
    with col4:
        spread1 = st.text_input('spread1', key="park_spread1")
    with col5:
        spread2 = st.text_input('spread2', key="park_spread2")
    with col1:
        D2 = st.text_input('D2', key="park_d2")
    with col2:
        PPE = st.text_input('PPE', key="park_ppe")
        
    

# code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinson_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)