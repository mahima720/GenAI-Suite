# 🖼️ Gemini Image-to-Text Generator

A powerful Multi-modal AI application built with Streamlit and the Google Gemini API. This tool allows users to upload images and receive detailed text descriptions, object identification, or answers to specific questions about the uploaded file.

## 🔗 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://gemini-genai-image-analyzer.streamlit.app/)


![Chatbot Image](/images/image3.png)

## Key Features

* **📸 Image Upload Support:** Handles multiple formats including JPG, JPEG, and PNG.
* **🧠 Multi-modal Analysis:** Combines text prompts with image data for precise AI reasoning.
* **🎨 Instant Preview:** Displays the uploaded image directly in the user interface before processing.
* **⚡ Real-time Processing:** Fast response times using the gemini-2.5-flash-lite model.
* **🛡️ Error Handling:** Robust error catching for API and upload issues.

## Skills Showcased

* **Python** Core programming language
* **Streamlit**	Frontend framework for the web interface
* **Google GenAI** Accessing the gemini-2.5-flash-lite model
* **Python-Dotenv** Secure management of API keys
* **Image Processing**	Pillow (PIL)

![Chatbot Image](/images/image4.png)
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

## 💡 How to Use

* **Enter a Prompt: (Optional)**  Ask something specific like "Identify the ingredients in this dish" or "Translate the text in this image".
* **Upload Image:** Click the "Choose an image" button to select a file from your device.
* **Analyze:** Click "Tell me about the image".
* **Result:** The AI's response will appear under "The Response is".

![Chatbot Image](/images/image5.png)