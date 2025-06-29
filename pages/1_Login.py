import streamlit as st
import uuid
from utils import save_user, get_user

st.set_page_config(page_title="Login", page_icon="🔐")

st.markdown("<h1 style='text-align: center;'>🔐 Login or Register</h1>", unsafe_allow_html=True)

form = st.form("auth")
choice = form.radio("Select Action", ["Login", "Register"], horizontal=True)
email = form.text_input("Email")
password = form.text_input("Password", type="password")
username = form.text_input("Username") # if choice == "Register" else None
avatar = form.selectbox("Avatar", ["🧑", "👩", "👨", "🧕", "🧙", "🧛"])
submit = form.form_submit_button("Submit")

if submit:
    if choice == "Register":
        if email and password and username:
            save_user(username, email, password, avatar)
            st.success("✅ Registered! Please login.")
        else:
            st.error("❌ Fill all fields")
    else:
        user = get_user(email, password)
        if user:
            st.session_state.user = user[0]
            st.session_state.avatar = user[3]
            st.session_state.session_id = str(uuid.uuid4())[:8]
            st.success("✅ Logged in! Redirecting...")
            st.switch_page("pages/2_Chat.py")
        else:
            st.error("❌ Invalid credentials")