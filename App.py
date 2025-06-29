import streamlit as st
from utils import init_db

st.set_page_config("🏠 Home | AI Assistant", layout="centered")

st.markdown("<h1 style='text-align: center;'>🏠 Welcome to the AI 🎤 Voice Assistant</h1>", unsafe_allow_html=True)

st.markdown("""
### 👤 Created by: **Mohammad Wasiq**

---
""")

# --- About Section ---
st.subheader("🧠 About This Project")

st.markdown("""
This **🎤 AI Voice Assistant** is a powerful conversational app built using **Streamlit** and **Euriai's API**, designed to simulate a realistic AI chatbot experience with voice input and output capabilities.

### 🚀 Key Features:
- 🎤 **Voice input** using your microphone
- 🤖 **AI-powered responses** via Euriai (GPT / Gemini / LLaMA models)
- 🔊 **Real-time voice synthesis** using gTTS
- 💬 **Chat memory with search** and session history
- 📥 **Downloadable chat history** per user/session
- 🔐 **User authentication** (Login/Register)
- 🛠 **Admin dashboard** with logs & analytics
- 🌗 **Theme toggle** (Light/Dark)
- 🎭 **Avatars & personalization**

This project is modular, production-ready, and demonstrates end-to-end capabilities for building interactive AI interfaces with **Streamlit**.

---
""")

# --- Contact Info ---
st.subheader("📬 Contact")

st.markdown("""
- 📧 [**Email**](mailto:mohammadwasiq0786@gmail.com)  
- 💼 [**LinkedIn**](https://www.linkedin.com/in/mohammadwasiq0/)

---

🧡 Thank you for visiting! Click below button to login or try the assistant.
""")


st.set_page_config("🎤 Voice Assistant", layout="wide")
if st.button("Login"):
    init_db()
    st.switch_page("pages/1_Login.py")
    
    
st.markdown("""
---
<div style='text-align: center; color: grey; font-size: 0.9em;'>
    © 2025 <b>mohammadwasiq0786@gmail.com</b>. All rights reserved.
</div>
""", unsafe_allow_html=True)
