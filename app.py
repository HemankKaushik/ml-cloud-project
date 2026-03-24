import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open('model.pkl', 'rb'))

# Define the names in the correct order for the Iris dataset
target_names = ['Setosa', 'Versicolor', 'Virginica']

st.title("Flower Species Predictor")
st.write("Enter the measurements below to see what species of Iris it is.")

# User inputs
s_length = st.number_input("Sepal Length", 0.0, 10.0, 5.0)
s_width = st.number_input("Sepal Width", 0.0, 10.0, 3.5)
p_length = st.number_input("Petal Length", 0.0, 10.0, 1.4)
p_width = st.number_input("Petal Width", 0.0, 10.0, 0.2)

if st.button("Predict"):
    features = np.array([[s_length, s_width, p_length, p_width]])
    prediction = model.predict(features)
    
    # Map the numerical prediction (0, 1, or 2) to the name
    result = target_names[prediction[0]]
    
    st.success(f"The predicted species is: **{result}**")