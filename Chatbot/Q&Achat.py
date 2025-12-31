from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
from google import genai

# 1. Use cache_resource to keep the client alive across Streamlit reruns
@st.cache_resource
def get_client():
    return genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

client = get_client()

# 2. Use cache_resource for the chat session so history persists correctly
@st.cache_resource
def get_chat_session():
    return client.chats.create(history=[], model='gemini-2.5-flash-lite')

chat = get_chat_session()

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

if submit and input:
    # 3. Call the stream method directly for the typing effect
    response = chat.send_message_stream(input)

    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))

    st.subheader("The Response is")

    full_response = ""
    placeholder = st.empty()

    for chunk in response:
        full_response += (chunk.text or "")
        placeholder.markdown(full_response)

    st.session_state['chat_history'].append(("Bot", full_response))

st.write("---")
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")