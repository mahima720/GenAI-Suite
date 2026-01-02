# 🚀 Gemini AI Suite
A collection of interactive AI applications powered by Google's Gemini 2.5 Flash Lite model and Streamlit. This repository contains two distinct tools: a persistent Q&A Chatbot and a Multimodal Image Analyzer.

## 🔗 Live Demo

**Chatbot Live Demo:**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemini-genai-chatbot.streamlit.app/)

**Image_Analyzer Live Demo:**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemini-genai-image-analyzer.streamlit.app/)

## 📂 Project Structure
This repository is organized into two main modules. Click the links below to navigate to their specific setup instructions:

**🤖 Q&A Chatbot:** A real-time conversational agent with session-based memory and streaming responses.

[![Chatbot](/images/image2.png)](/Chatbot/README.md)

[➡️ **View Full Q&A Chatbot Details (README)**](/Chatbot/README.md)

**🖼️ Image Analyzer:** A multimodal tool that generates text descriptions and insights from uploaded photos.

[![Image Analyzer](/images/image5.png)](/Image_Analyzer/README.md)

[➡️ **View Full Image Analyzer Details (README)**](/Image_Analyzer/README.md)

## 🛠️ Global Prerequisites
Before running either application, ensure you have the following installed:

**Python 3.9+**

**Google Gemini API Key** 🔑 (Available at Google AI Studio)

## Key Features Across the Suite

* **⚡ Real-time Streaming:** Experience low-latency AI responses with a word-by-word typing effect.

* **🧠 Intelligent Caching:** Uses @st.cache_resource to maintain API connections and chat history efficiently.

* **📁 Clean UI/UX:** Simple, intuitive interfaces built entirely in Python.

## 🚀 Quick Start Guide

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

**4. To run the Q&A Chatbot:**

    cd chatbot-folder-name
    streamlit run app.py

**4. To run the Image Analyzer:**

    cd image-analyzer-folder-name
    streamlit run app.py