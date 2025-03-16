import google.generativeai as genai # type: ignore
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_notes(topic):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Generate educational notes on {topic} in simple language.")
    return response.text

def list_models():
    models = genai.list_models()
    for model in models:
        print(model.name)

import streamlit as st # type: ignore

st.title("AI Study Hub 📚")
topic = st.text_input("Enter topic:")
if st.button("Generate Notes"):
    notes = generate_notes(topic)
    st.write(notes)

def generate_quiz(subject):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(f"Generate 5 multiple-choice questions for {subject}.")
    return response.text