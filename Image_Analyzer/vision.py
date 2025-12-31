from dotenv import load_dotenv
load_dotenv() # loading all the environment variables

import streamlit as st
import os
from google import genai
from PIL import Image

# Initialize Client (New SDK automatically finds GOOGLE_API_KEY in .env)
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image):
    try:
        response = client.models.generate_content(
        model="gemini-2.5-flash-lite", 
        contents=[input,image] if input else [image]
        )
        return response.text
    except Exception as e:
        return f"Error: {e}"
    
## initialize our streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")

input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image....", type=["jpg","jpeg","png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.", width=720)

submit = st.button("Tell me about the image")

##if submit is clicked
if submit:
    if uploaded_file is not None:
        with st.spinner("Analyzing image..."):
            response_text = get_gemini_response(input, image)
        st.subheader("The Response is")
        st.write(response_text)
    else:
        st.warning("Please upload an image first!")