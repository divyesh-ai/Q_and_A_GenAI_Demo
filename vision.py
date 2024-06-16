from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os 
import google.generativeai as genai
from PIL import Image


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini pro Model and get response

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(input, image):
    if input!="":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize our streamlit app

st.set_page_config(page_title="GenAI Image Description: ")

st.header("Image Description Generator Demo App : ")

# Input field for the user's question
question = st.text_input("Please Add some information Related to image if you want OR Skip :")

# Add a file uploader to allow the user to upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

# Check if a file has been uploaded
if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit  = st.button("Tell me about the image...")


# Placeholder for the answer
answer_placeholder = st.empty()


# when submit is clicked
if submit:
    if question:
        # Placeholder logic for generating an answer (Replace with your GenAI model logic)
        answer = get_gemini_response(question, image)
        
        # Display the answer
        answer_placeholder.write(f"**Answer:** {answer}")
    else:
        answer_placeholder.warning("Please upload a image.")
