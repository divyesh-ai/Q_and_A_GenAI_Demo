from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os 
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini pro Model and get response

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# Initialize our streamlit app

st.set_page_config(page_title="GenAI Q&A")
st.header("LLM(Q&A) Demo App : ")

# Input field for the user's question
question = st.text_input("Enter your question:")

submit  = st.button("Submit")


# Placeholder for the answer
answer_placeholder = st.empty()


# when submit is clicked
if submit:
    if question:
        # Placeholder logic for generating an answer (Replace with your GenAI model logic)
        answer = get_gemini_response(question)
        
        # Display the answer
        answer_placeholder.write(f"**Answer:** {answer}")
    else:
        answer_placeholder.warning("Please enter a question.")