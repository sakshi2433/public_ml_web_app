# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 22:35:24 2025

@author: BIT
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model= pickle.load(open('C:/Users/BIT/Desktop/ML/Multiple Disease Prediction Model/trained_model.sav','rb'))

heart_model= pickle.load(open('C:/Users/BIT/Desktop/ML/Multiple Disease Prediction Model/trained_heart_model.sav','rb'))

park_model= pickle.load(open('C:/Users/BIT/Desktop/ML/Multiple Disease Prediction Model/trained_park_model.sav','rb'))

with st.sidebar:
    
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
if (selected=='Diabetes Prediction'):
    
    st.title('Diabetes Prediction using ML')
    
    col1,col2,col3= st.columns(3)
    
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
        SkinThickness= st.text_input('Skin Thickness')
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function')
    
    with col2:
        Glucose= st.text_input('Glucose Level ')
        Insulin= st.text_input('Insulin level')
        Age= st.text_input('Age')
    
    with col3:
        BloodPressure= st.text_input('Blood Pressure Level')
        BMI= st.text_input('BMI')
    
    
    diab_diagnosis=''
    
    #creating a button
    
    if st.button('Diabetes Test Result'):
        diab_pred= diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if (diab_pred[0]==1):
            diab_diagnosis='The person is diabetic.'
        else:
            diab_diagnosis='The person is not diabetic.'
    
    st.success(diab_diagnosis)
    
if (selected=='Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    
    col1,col2,col3= st.columns(3)
    
    with col1:
        Age= st.text_input('Age')
        Sex= st.text_input('Sex')
        Cp= st.text_input('CP')
        oldpeak=st.text_input('OldPeak')
    
    
    with col2:
        trestbps= st.text_input('TrestBps')
        chol= st.text_input('Cholestrol')
        fbs= st.text_input('FBS')
        slope=st.text_input('Slope')
    
    with col3:
        restecg= st.text_input('RestECG')
        thalach= st.text_input('thalach')
        exang= st.text_input('exang')
        ca= st.text_input('ca')
        thal=st.text_input('thal') 
    
    heart_diagnosis=''
    
    #creating a button
    
    if st.button('Heart Disease Test Result'):
        heart_pred= heart_model.predict([[Age,Sex,Cp,oldpeak,trestbps,chol,fbs,slope,restecg,thalach,exang,ca,thal]])
        
        if (heart_pred[0]==1):
            heart_diagnosis='The person has heart disease.'
        else:
            heart_diagnosis='The person does not have heart disease.'
    
    st.success(heart_diagnosis)
    
if (selected=='Parkinsons Disease Prediction'):
    
    st.title('Parkinsons Disease Prediction using ML')
    
    col1,col2,col3,col4,col5= st.columns(5)
    
    with col1:
        fo= st.text_input('MDVP:Fo(Hz)')
        fhi=st.text_input('MDVP:Fhi(Hz)')
        flo=st.text_input('MDVP:Flo(Hz)')
        jitterp=st.text_input('MDVP:Jitter(%)')
            
            
            
    with col2:
        jittera=st.text_input('MDVP:Jitter(Abs)')
        rap=st.text_input('MDVP:RAP')
        ppq=st.text_input('MDVP:PPQ')
        jitterddp=st.text_input('Jitter:DDP')
        d2=st.text_input('D2')
            
            
    with col3:
        shimmer= st.text_input('MDVP:Shimmer')
        shimmerdb= st.text_input('MDVP:Shimmer(dB)')
        apq3= st.text_input('Shimmer:APQ3')
        apq5=st.text_input('Shimmer:APQ5')
        ppe=st.text_input('PPE')
            
            
    with col4:
        apq= st.text_input('MDVP:APQ')
        dda=st.text_input('Shimmer:DDA')
        nhr=st.text_input('NHR')
        hnr=st.text_input('HNR')
        
            
    with col5:
        rpde=st.text_input('RPDE')
        dfa=st.text_input('DFA')
        spread1=st.text_input('spread1')
        spread2=st.text_input('spread2')
            
            
    
    
    
    park_diagnosis=''
    
    #creating a button
    
    if st.button('Parkinson\'s Disease Test Result'):
        park_pred= park_model.predict([[fo,fhi,flo,jitterp,jittera,rap,ppq,jitterddp,shimmer,shimmerdb,apq3,apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]])
        
        if (park_pred[0]==1):
            park_diagnosis='The person has parkinson\'s disease.'
        else:
            park_diagnosis='The person does not have parkinson\'s disease.'
    
    st.success(park_diagnosis)
        
        