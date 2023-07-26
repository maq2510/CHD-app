#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle

# Load the trained logistic regression model from the pickle file
with open('CHDmodel.pickle', 'rb') as file:
    model = pickle.load(file)

def predict_chd(age, diabetes, sysBP, diaBP, BMI, glucose, is_M, is_smoking_YES):
    # Prepare user input as a feature vector
    user_input = [[age, diabetes, sysBP, diaBP, BMI, glucose, is_M, is_smoking_YES]]

    print("User input before conversion:")
    print("age:", age, type(age))
    print("diabetes:", diabetes, type(diabetes))
    print("sysBP:", sysBP, type(sysBP))
    print("diaBP:", diaBP, type(diaBP))
    print("BMI:", BMI, type(BMI))
    print("glucose:", glucose, type(glucose))
    print("is_M:", is_M, type(is_M))
    print("is_smoking_YES:", is_smoking_YES, type(is_smoking_YES))

    # Convert user inputs to correct data types
    try:
        age = int(age)
        sysBP = int(sysBP)
        diaBP = int(diaBP)
        BMI = float(BMI)
        glucose = int(glucose)
    except ValueError as e:
        st.error("Error: Please ensure all input fields are filled correctly.")
        st.stop()

    # Make prediction
    prediction = model.predict(user_input)[0]

    return prediction

def main():
    st.title("Coronary Heart Disease (CHD) Prediction")
    st.write("Enter the following information to predict CHD:")

    age = st.slider("Age", 20, 100, 40)
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    diabetes = 1 if diabetes == "Yes" else 0
    sysBP = st.slider("Systolic Blood Pressure", 80, 250, 120)
    diaBP = st.slider("Diastolic Blood Pressure", 40, 150, 80)
    BMI = st.slider("BMI", 10, 60, 25)
    glucose = st.slider("Glucose Level", 50, 400, 100)
    is_M = st.radio("Gender", ["Male", "Female"])
    is_M = 1 if is_M == "Male" else 0  # Corrected initialization to 0 for Female
    is_smoking_YES = st.radio("Smoking", ["No", "Yes"])
    is_smoking_YES = 1 if is_smoking_YES == "Yes" else 0

    if st.button("Predict"):
        # Call predict_chd function
        prediction = predict_chd(age, diabetes, sysBP, diaBP, BMI, glucose, is_M, is_smoking_YES)

        if prediction == 0:
            st.write("Low risk of Coronary Heart Disease (CHD) in the next 10 years.")
        else:
            st.write("High risk of Coronary Heart Disease (CHD) in the next 10 years.")

if __name__ == "__main__":
    main()


# In[ ]:




