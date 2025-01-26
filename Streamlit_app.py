import streamlit as st
import pickle

# Load the saved model
loaded_model = pickle.load(open('/content/triained_model.sav', 'rb'))  # Assuming 'trained_model.sav' is your model file

# Create the Streamlit app
st.title("Salary Prediction App")

# Get user input for experience
experience = st.number_input("Enter Years of Experience:", min_value=0.0, step=0.1)

# Make prediction and display
if st.button("Predict Salary"):
    salary_prediction = loaded_model.predict([[experience]])
    st.success(f"Predicted Salary: {salary_prediction[0]:.2f} Rupees")

# Run the Streamlit app
# In your terminal: streamlit run app.py
