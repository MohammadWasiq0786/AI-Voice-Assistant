# 🎙️ AI Voice Assistant Web App 🚀

>A smart, conversational AI web assistant built using **Streamlit**, **Euriai API**, **SQLite**, and **Speech Recognition** — with user login, chat history, avatars, session tracking, voice replies, and a built-in admin dashboard!

## 🚀 Features

✅ Real-time AI replies using [Euriai](https://euron.com)  
🎤 Voice input (via microphone)  
🔊 Voice output using `gTTS`  
🧑 Personalized user login & avatar  
🗂️ Session tracking with chat history  
⬇️ Export chat to CSV (`user-session-date.csv`)  
🌙 Dark mode toggle  
📂 Admin dashboard with analytics  
📜 Persistent chat history via SQLite  
📄 Multipage navigation using Streamlit  
🔐 Login / Sign Up with session state  

---

## 🖼️ Demo UI Screens

| Home | Login / Register | Assistant Interface | Admin Dashboard |
|------|------------------|---------------------|-----------------|
| ![Home](https://github.com/MohammadWasiq0786/AI-Voice-Assistant/blob/main/image/home.png) | ![Login](https://github.com/MohammadWasiq0786/AI-Voice-Assistant/blob/main/image/auth.png) | ![Chat](https://github.com/MohammadWasiq0786/AI-Voice-Assistant/blob/main/image/chat.png) | ![Admin](https://github.com/MohammadWasiq0786/AI-Voice-Assistant/blob/main/image/admin.png) |


## 📁 Folder Structure

````

streamlit\_voice\_assistant/
├── app.py                   # Landing/About page
├── assistant\_utils.py       # All logic: AI, DB, utils
├── .env                     # Store your API key
├── conversation.db          # SQLite database (auto created)
├── pages/
│   ├── 1\_Login.py           # Login/Register page
│   ├── 2\_Chat.py             # AI Assistant main page
│   └── 3\_Admin.py           # Admin dashboard
└── README.md                # This file

````

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repo or download files:

```bash
git clone https://github.com/mohammadwasiq0786/streamlit-voice-assistant.git
cd streamlit-voice-assistant
```

### 2️⃣ Install dependencies

Make sure Python 3.8+ is installed.

```bash
pip install -r requirements.txt
```

**Dependencies include:**

* `streamlit`
* `gtts`
* `playsound`
* `speechrecognition`
* `euriai`
* `python-dotenv`
* `pandas`
* `uuid`

### 3️⃣ Setup your `.env`

Create a `.env` file in the root directory:

```
EURI_API_KEY=your_euriai_api_key_here
```

### 4️⃣ Run the app

```bash
streamlit run app.py
```

Use the sidebar to:

* 🔓 Login / Signup
* 🎤 Chat with the Assistant
* 🛠 Access the Admin Panel (login as `admin`)
* 💾 Export Chat
---

## 👑 Admin Access

To login as an admin, register a user with the username `admin`.
The Admin Panel will show stats, logs, and a chat viewer.

---

## ✨ Features To Explore

* 🧠 AI model switching: `gpt-4.1-nano`, `gemini`, `llama` (you can extend it)
* 💾 Export CSVs: filename as `username-sessionid-datetime.csv`
* 🔊 Speak AI reply (only once using saved response)
* 🌓 Dark/light toggle in sidebar
* 🧑‍💻 Built-in avatars to make users feel personal

---

## 📦 To-Do / Future Enhancements

* 🔐 Password-based login
* 🖼️ Avatar image uploads
* 🌍 Language support & translation
* 📊 Advanced admin insights (charts, user activity)
* ☁️ Cloud storage (PostgreSQL, Firebase, etc.)
* 🗣️ Multi-turn memory (conversation context)

---

## 🙌 Acknowledgments

* [Euriai](https://euron.one/euri/api) for AI APIs
* [Streamlit](https://streamlit.io/) for UI framework
* [gTTS](https://pypi.org/project/gTTS/) for speech output
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) for mic input

---

## 📬 Contact / Contribution

Have feedback or want to contribute?

* 📧 **Email**: [mohammadwasiq786@gmail.com](mailto:mohammadwasiq786@gmail.com)
* 💻 **GitHub**: [mohammadwasiq0786](https://github.com/mohammadwasiq0786)
* 💼 **LinkedIn**: [mohammadwasiq0](https://www.linkedin.com/in/mohammadwasiq0/)

Pull requests welcome! 🎉

---
