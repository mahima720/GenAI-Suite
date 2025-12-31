# 🤖 Gemini LLM Q&A Chatbot

![Chatbot Image](/images/image1.png)

A sleek, real-time Q&A application powered by the Google Gemini API and Streamlit. This chatbot features a streaming "typing" effect and maintains a persistent conversation history during your session.

## Features

* ⚡ Real-time Streaming: Watch the AI "think" and respond word-by-word.
* 🧠 Session Memory: Remembers previous questions and answers during the current session.
* 🚀 Optimized Performance: Uses Streamlit's @st.cache_resource to keep the API connection alive without reconnecting on every click.
* 📱 Clean UI: Built with Streamlit for a responsive and user-friendly experience.

## Skills Showcased

* **Python** Core programming language
* **Streamlit**	Frontend framework for the web interface
* **Google GenAI** Accessing the gemini-2.5-flash-lite model
* **Python-Dotenv** Secure management of API keys

![Chatbot Response](/images/image2.png)

## 🚀 Getting Started

Follow these steps to set up the project on your local machine:

**1. Clone the Repository** 

    git clone <your-repository-url>
    cd <your-project-folder>
**2. Install Dependencies**

    pip install -r requirements.txt

**3. Set Up Your API Key**

    Get an API key from Google AI Studio.
    Create a file named .env in your project root.
    Add your key to the file:
    Code snippet
    GOOGLE_API_KEY=your_secret_api_key_here

**4. Run the App**

    streamlit run your_filename.py

## 📖 Usage Guide

**Ask a Question:** Type your prompt into the input box at the top.

**Submit:** Click the "Ask the question" button.

**View Response:** The AI will stream its answer in the "The Response is" section.

**Review History:** Scroll down to see the "Chat History" log of your entire conversation.