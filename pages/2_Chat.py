import os
import uuid
import sqlite3
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv
from euriai import EuriaiClient
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import streamlit as st
from utils import load_sessions, save_chat, load_history

st.set_page_config(page_title="Login", page_icon="💬")

st.markdown("<h1 style='text-align: center;'>💬 Chat with AI</h1>", unsafe_allow_html=True)

if "user" not in st.session_state:
    st.error("🔒 Please login first.")
    st.stop()
 
# ------------------- Load API Key -------------------
load_dotenv()
EURI_API_KEY = os.getenv("EURI_API_KEY")
if not EURI_API_KEY:
    st.error("EURI_API_KEY not found in .env")
    st.stop()

model = st.selectbox("Choose AI Model", ["gpt-4.1-nano", 
                                         "gpt-4.1-mini", 
                                        "gemini-2.0-flash",  
                                        "llama-4-scout-17b-16e-instruct", 
                                        "llama-3.3-70b-versatile",
                                        "deepseek-r1-distill-llama-70b",
                                        "qwen-qwq-32b"])

def generate_response(prompt, model):
    
    client = EuriaiClient(api_key=EURI_API_KEY, model=model)
    response = client.generate_completion(prompt=prompt, temperature=0.7, max_tokens=300)
    ai_text = response['choices'][0]['message']['content'] if isinstance(response, dict) and 'choices' in response else "Sorry, I couldn't generate a response."
    return ai_text

DB_PATH = "Database/conversation.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

def clear_history(user, session_id=None):
    if session_id:
        c.execute("DELETE FROM history WHERE user=? AND session_id=?", (user, session_id))
    else:
        c.execute("DELETE FROM history WHERE user=?", (user,))
    conn.commit()

def voice_assistance(user_input):
    prompt = f"You are an AI assistant. Respond clearly and concisely to:\n'{user_input}'"
    try:
        response = client.generate_completion(prompt=prompt, temperature=0.7, max_tokens=300)
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {e}"

# ------------------- Streamlit Setup -------------------

# Theme
if "theme" not in st.session_state:
    st.session_state.theme = "light"

with st.sidebar:
    if st.toggle("🌓 Dark Mode"):
        st.session_state.theme = "dark"
    else:
        st.session_state.theme = "light"

    if st.session_state.theme == "dark":
        st.markdown("<style>body { background-color: #111; color: white; }</style>", unsafe_allow_html=True)


# ------------------- Sidebar History -------------------
username= st.session_state.user

with st.sidebar.expander("📂 Session History", expanded=False):
    session_filter = st.selectbox("🧾 View session:", ["All"] + load_sessions(username))
    
    # load_history(st.session_state.user, st.session_state.session_id)
    selected_session_id = None if session_filter == "All" else session_filter

    search = st.text_input("🔍 Search chat:")
    history_df = load_history(username, selected_session_id, search)

    if not history_df.empty:
        for _, row in history_df.iterrows():
            st.markdown(f"**🧕 You:** {row['user_input']}")
            st.markdown(f"**🤖 AI:** {row['ai_response']}")
            st.markdown("---")

        now = datetime.now().strftime("%Y%m%d_%H%M")
        fname = f"{username}-{session_filter or 'all'}-{now}.csv"
        csv = history_df.to_csv(index=False).encode("utf-8")
        st.download_button("⬇️ Download Chat", csv, fname, "text/csv")

        if st.button("🗑️ Clear Chat"):
            clear_history(username, selected_session_id)
            st.rerun()
    else:
        st.info("No history yet.")

# ------------------- Chat Input & Response -------------------
user_input = st.text_input("💬 Write Your Question (OR 🎤 Use Mic):",
    placeholder="Write your query here...")

if st.button("🎤 Use Mic"):
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("🎙️ Listening...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            user_input = r.recognize_google(audio)
            st.success(f"🗣️ You said: {user_input}")
    except Exception as e:
        st.error(f"🎤 Error: {e}")

# model="gpt-4.1-nano"
if user_input:
    with st.spinner("🤖 Generating..."):
        ai_response = generate_response(user_input, model)
        st.session_state.last_ai_response = ai_response
        st.markdown(f"**🧕 You:** {user_input}")
        st.markdown(f"**🤖 AI:** {ai_response}")
        save_chat(username, selected_session_id, model, user_input, ai_response)
        # save_chat(user, session_id, model, user_input, ai_response)

# if "last_ai_response" in st.session_state:
if st.button("🔊 Speak this"):
    # tts = gTTS(st.session_state.last_ai_response)
    tts = gTTS(ai_response)
    AUDIO_FILE_SAVING_PATH = f"Media/{selected_session_id}-{user_input}.mp3"
    tts.save(AUDIO_FILE_SAVING_PATH)
    playsound(AUDIO_FILE_SAVING_PATH)
    # os.remove(AUDIO_FILE_SAVING_PATH)
    