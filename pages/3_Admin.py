import streamlit as st
import sqlite3
import pandas as pd
from utils import is_admin_user

st.set_page_config(page_title="Login", page_icon="🛠️")

# Check if user is admin
if "user" not in st.session_state or not is_admin_user(st.session_state.user):
    st.error("❌ Admin access only")
    st.stop()

st.markdown("<h1 style='text-align: center;'>🛠 Admin Dashboard</h1>", unsafe_allow_html=True)

# Connect to DB
DB_PATH = "Database/conversation.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

# --- METRICS ---
users = c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
messages = c.execute("SELECT COUNT(*) FROM history").fetchone()[0]
sessions = c.execute("SELECT COUNT(DISTINCT session_id) FROM history").fetchone()[0]

# st.metric("👥 Users", users)
# st.metric("💬 Messages", messages)
# st.metric("📂 Sessions", sessions)

# Prepare data as a one-row table
metrics_df = pd.DataFrame([{
    "👥 Users": users,
    "💬 Messages": messages,
    "📂 Sessions": sessions
}])

st.table(metrics_df)
metrics_csv= metrics_df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download Metrics", metrics_csv, f"metrics_log.csv", "text/csv")


# --- USERS LIST ---
with st.expander("👤 View All Users"):
    # Display as table    
    users_data = c.execute("SELECT username, email, password, avatar_path, is_admin FROM users").fetchall()
    df_users = pd.DataFrame(users_data, columns=["Username", "Email", "Password", "Avatar", "Is Admin"])
    st.dataframe(df_users)
    user_csv = df_users.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Users", user_csv, f"user_log.csv", "text/csv")


# --- CHAT HISTORY FILTERING ---
with st.expander("📜 View All Chats"):
    # Fetch available usernames and models
    usernames = [row[0] for row in c.execute("SELECT DISTINCT user FROM history").fetchall()]
    models = [row[0] for row in c.execute("SELECT DISTINCT model FROM history").fetchall()]

    # Filters
    col1, col2 = st.columns(2)
    selected_user = col1.selectbox("👤 Filter by User", ["All"] + usernames)
    selected_model = col2.selectbox("🤖 Filter by Model", ["All"] + models)

    # Build query
    query = "SELECT user, session_id, model, user_input, ai_response, timestamp FROM history WHERE 1=1"
    params = []

    if selected_user != "All":
        query += " AND user=?"
        params.append(selected_user)

    if selected_model != "All":
        query += " AND model=?"
        params.append(selected_model)

    query += " ORDER BY timestamp DESC"

    # Execute and display
    chat_data = pd.read_sql_query(query, conn, params=params)
    st.dataframe(chat_data)

    # Export
    chat_csv = chat_data.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Chats", chat_csv, f"chat_log.csv", "text/csv")
