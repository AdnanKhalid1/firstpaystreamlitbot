# app.py
import streamlit as st
from gradio_client import Client

# Initialize Gradio client
client = Client("adnankhd/fpfaqbotdemo")

# Streamlit app
st.title("First Pay Customer Service Chatbot")
st.write("Ask me anything about HBL Microfinance or FirstPay Wallet!")

# Input box
user_input = st.text_input("Your query:")

# Button to submit
if st.button("Submit"):
    if user_input:
        with st.spinner("Fetching response..."):
            try:
                result = client.predict(query=user_input, api_name="/predict")
                st.success("Chatbot's response:")
                st.write(result)
            except Exception as e:
                st.error("Error fetching response. Please try again later.")
                st.write(e)
    else:
        st.warning("Please enter a query.")
