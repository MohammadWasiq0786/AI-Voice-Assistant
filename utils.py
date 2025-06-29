import sqlite3, os
import pandas as pd

DB_PATH = "Database/conversation.db"

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
c = conn.cursor()

def init_db():
    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        email TEXT,
        password TEXT,
        avatar_path TEXT,
        is_admin INTEGER DEFAULT 0
    )
    """)
    c.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        session_id TEXT,
        model TEXT,
        user_input TEXT,
        ai_response TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()

def save_user(username, email, password, avatar_path, is_admin=0):
    c.execute("INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?, ?)",
              (username, email, password, avatar_path, is_admin))
    conn.commit()

def get_user(email, password):
    return c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password)).fetchone()

def is_admin_user(username):
    result = c.execute("SELECT is_admin FROM users WHERE username=?", (username,)).fetchone()
    return result and result[0] == 1

def save_chat(user, session_id, model, user_input, ai_response):
    c.execute("INSERT INTO history (user, session_id, model, user_input, ai_response) VALUES (?, ?, ?, ?, ?)",
              (user, session_id, model, user_input, ai_response))
    conn.commit()

def load_sessions(user):
    c.execute("SELECT DISTINCT session_id FROM history WHERE user=? ORDER BY timestamp DESC", (user,))
    return [row[0] for row in c.fetchall()]


def load_history(user, session_id=None, search=""):
    query = "SELECT * FROM history WHERE user=?"
    params = [user]

    if session_id:
        query += " AND session_id=?"
        params.append(session_id)

    if search:
        query += " AND (user_input LIKE ? OR ai_response LIKE ?)"
        params.extend([f"%{search}%", f"%{search}%"])

    query += " ORDER BY timestamp DESC"
    return pd.read_sql_query(query, conn, params=params)
