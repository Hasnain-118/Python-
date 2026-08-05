"""
Hasnain AI — Professional Edition
==================================
Elegant, modern, conversational assistant with persistent chat history,
persona control, and Groq-backed responses.

SECURITY NOTE
-------------
This app expects your Groq API key via the GROQ_API_KEY environment
variable (or entered manually in the sidebar at runtime). Never hardcode
API keys in source files — if a key is ever committed or shared, revoke
it immediately at https://console.groq.com/keys and issue a new one.
"""

import os
import json
import difflib
import uuid
import re
from datetime import datetime

import streamlit as st

# ------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------
DATA_PATH = "Hasnain.json"
CHATS_DIR = "chat_histories"
os.makedirs(CHATS_DIR, exist_ok=True)

GROQ_MODELS = {
    "Fast": "llama-3.1-8b-instant",
    "Balanced": "gemma2-9b-instant",
    "Quality": "llama-3.3-70b-versatile",
}

DEFAULT_SYSTEM_PROMPT = (
    "You are Hasnain AI, a helpful, professional assistant.\n"
    "Respond in the same language as the user (Urdu or English).\n"
    "Give clear, concise, friendly answers."
)

WELCOME_MSG = (
    "👋 Hello! I'm Hasnain AI. How can I help you today?\n\n"
    "👋 السلام علیکم! میں حسنین اے آئی ہوں۔ آج میں آپ کی کس طرح مدد کر سکتا ہوں؟"
)

FALLBACK_RESPONSES = {
    "hi": "Hello! 👋 How can I help you today?",
    "hello": "Hi there! 😊 What brings you here?",
    "hey": "Hey! How's it going?",
    "how are you": "I'm doing great, thanks for asking! How about you?",
    "what's up": "Not much, just waiting for your questions! 😄",
    "good morning": "Good morning! ☀️ Hope you have a wonderful day.",
    "good night": "Good night! 🌙 Sleep well.",
    "thanks": "You're welcome! 😊 Happy to help.",
    "thank you": "My pleasure! 😊",
    "bye": "Goodbye! 👋 Take care.",
    "kia hal ha": "اللہ کا شکر ہے، میں ٹھیک ہوں! آپ کیسے ہیں؟",
    "kesy ho": "اللہ کا شکر ہے، میں ٹھیک ہوں! آپ کیسے ہیں؟",
    "assalam o alaikum": "وعلیکم السلام! آپ کیسے ہیں؟",
}

try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False

# ------------------------------------------------------------------
# PAGE SETUP
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Hasnain AI",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    * { font-family: 'Inter', sans-serif; box-sizing: border-box; }

    html, body, .stApp {
        background: radial-gradient(ellipse at 30% 20%, #1a1a2e 0%, #16213e 50%, #0f0f23 100%);
        color: #e8e8f0;
    }
    #MainMenu, footer, header { visibility: hidden; }

    section[data-testid="stSidebar"] {
        background: rgba(16, 16, 30, 0.92) !important;
        border-right: 1px solid rgba(255,255,255,0.06) !important;
        backdrop-filter: blur(12px);
    }
    section[data-testid="stSidebar"] * { color: #d0d4e8 !important; }
    section[data-testid="stSidebar"] .stButton button {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        color: #d0d4e8 !important;
        transition: all 0.3s;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: rgba(129, 140, 248, 0.15) !important;
        border-color: #818cf8 !important;
        box-shadow: 0 0 20px rgba(129, 140, 248, 0.15);
    }
    section[data-testid="stSidebar"] .stTextInput input,
    section[data-testid="stSidebar"] .stSelectbox select,
    section[data-testid="stSidebar"] textarea {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        color: #e8e8f0 !important;
    }
    section[data-testid="stSidebar"] .stTextInput input:focus,
    section[data-testid="stSidebar"] textarea:focus {
        border-color: #818cf8 !important;
        box-shadow: 0 0 15px rgba(129, 140, 248, 0.1);
    }

    [data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 20px !important;
        padding: 0.6rem 1rem !important;
        margin-bottom: 0.6rem !important;
        backdrop-filter: blur(4px);
        transition: all 0.2s;
    }
    [data-testid="stChatMessage"]:hover { border-color: rgba(255,255,255,0.15); }
    [data-testid="stChatMessage"][data-testid*="user"] {
        border-left: 3px solid #818cf8 !important;
        background: rgba(129, 140, 248, 0.06) !important;
    }
    [data-testid="stChatMessage"][data-testid*="assistant"] {
        border-left: 3px solid #a78bfa !important;
        background: rgba(167, 139, 250, 0.03) !important;
    }

    .stChatInput textarea {
        background: rgba(255,255,255,0.04) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 30px !important;
        color: #e8e8f0 !important;
        padding: 12px 20px !important;
        font-size: 1rem !important;
        transition: all 0.3s;
    }
    .stChatInput textarea:focus {
        border-color: #818cf8 !important;
        box-shadow: 0 0 30px rgba(129, 140, 248, 0.08) !important;
    }

    .action-btn-container { display: flex; gap: 10px; margin: 8px 0 12px 0; }
    .action-btn-container .stButton button {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 8px !important;
        color: #d0d4e8 !important;
        padding: 0.4rem 1.2rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        white-space: nowrap;
    }
    .action-btn-container .stButton button:hover {
        background: rgba(129, 140, 248, 0.15) !important;
        border-color: #818cf8 !important;
        box-shadow: 0 0 20px rgba(129, 140, 248, 0.12);
        transform: translateY(-1px);
    }

    .header-container { text-align: center; padding: 10px 0 5px 0; }
    .main-title {
        font-weight: 700;
        font-size: 2.8rem;
        background: linear-gradient(135deg, #818cf8, #a78bfa, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .subtitle { color: #8b8fc7 !important; font-size: 0.95rem; letter-spacing: 2px; font-weight: 300; margin-top: 2px; }
    .divider { height: 2px; background: linear-gradient(90deg, transparent, #818cf8, transparent); margin: 8px 0 20px 0; opacity: 0.3; }
    .footer { text-align: center; margin-top: 2rem; padding: 0.6rem; color: #5a5e8a !important; font-size: 0.8rem; border-top: 1px solid rgba(255,255,255,0.06); }

    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: rgba(0,0,0,0.2); }
    ::-webkit-scrollbar-thumb { background: #818cf8; border-radius: 10px; }
    ::-webkit-scrollbar-thumb:hover { background: #a78bfa; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# HELPERS
# ------------------------------------------------------------------
def detect_language(text: str) -> str:
    urdu_script = re.compile(r'[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF]')
    roman_urdu = {
        'kesy', 'kya', 'kaisa', 'hai', 'ho', 'hun', 'hain', 'main', 'tum', 'ap',
        'mujhe', 'tujhe', 'hum', 'woh', 'yeh', 'aap', 'kiya', 'karo', 'karte',
        'kahan', 'kaise', 'acha', 'theek', 'sahi', 'galat', 'nahi', 'han', 'ji',
        'assalam', 'alaikum', 'salam', 'khuda', 'allah', 'shukria',
    }
    text_lower = text.lower().strip()
    if urdu_script.search(text):
        return 'urdu'
    for word in text_lower.split():
        word = re.sub(r'[^\w\s]', '', word)
        if word in roman_urdu:
            return 'urdu'
    urdu_phrases = ['kesy ho', 'kya haal', 'kaisa hai', 'kya hal hai', 'kya kar rahy']
    if any(phrase in text_lower for phrase in urdu_phrases):
        return 'urdu'
    return 'english'


def save_chat_history(chat_id: str, messages: list, title: str = None):
    path = os.path.join(CHATS_DIR, f"{chat_id}.json")
    existing = load_chat_history(chat_id) or {}
    payload = {
        "id": chat_id,
        "created": existing.get("created", datetime.now().isoformat()),
        "updated": datetime.now().isoformat(),
        "title": title if title else existing.get("title"),
        "messages": messages,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)


def load_chat_history(chat_id: str):
    path = os.path.join(CHATS_DIR, f"{chat_id}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def get_all_chats():
    chats = []
    for fname in os.listdir(CHATS_DIR):
        if not fname.endswith(".json"):
            continue
        cid = fname[:-5]
        payload = load_chat_history(cid)
        if not payload:
            continue
        title = payload.get("title")
        if not title:
            title = "New Chat"
            for msg in payload["messages"]:
                if msg["role"] == "user":
                    title = msg["content"][:40] + ("..." if len(msg["content"]) > 40 else "")
                    break
        chats.append({
            "id": cid,
            "title": title,
            "created": payload.get("created", ""),
            "updated": payload.get("updated", ""),
            "count": len(payload["messages"]),
        })
    chats.sort(key=lambda x: x["updated"], reverse=True)
    return chats


def delete_chat(chat_id: str) -> bool:
    path = os.path.join(CHATS_DIR, f"{chat_id}.json")
    if os.path.exists(path):
        os.remove(path)
        return True
    return False


def export_chat_text(messages: list) -> str:
    lines = []
    for m in messages:
        speaker = "You" if m["role"] == "user" else "Hasnain AI"
        lines.append(f"{speaker}: {m['content']}\n")
    return "\n".join(lines)


@st.cache_data
def load_personal_data():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


PERSONAL_DATA = load_personal_data()
PERSONAL_INSTRUCTIONS = [item["instruction"] for item in PERSONAL_DATA]


def match_personal_answer(prompt: str, cutoff: float = 0.82):
    p = prompt.lower().strip()
    for item in PERSONAL_DATA:
        if p == item["instruction"].lower().strip():
            return item["output"]
    close = difflib.get_close_matches(
        p, [i.lower().strip() for i in PERSONAL_INSTRUCTIONS], n=1, cutoff=cutoff
    )
    if close:
        for item in PERSONAL_DATA:
            if item["instruction"].lower().strip() == close[0]:
                return item["output"]
    return None


def get_fallback_reply(prompt: str):
    key = prompt.strip().lower()
    if key in FALLBACK_RESPONSES:
        return FALLBACK_RESPONSES[key]
    if key.startswith("hi") or key.startswith("hello"):
        return FALLBACK_RESPONSES["hi"]
    if key.startswith("thank"):
        return FALLBACK_RESPONSES["thanks"]
    if "how are" in key:
        return FALLBACK_RESPONSES["how are you"]
    if "bye" in key or "goodbye" in key:
        return FALLBACK_RESPONSES["bye"]
    if "morning" in key:
        return FALLBACK_RESPONSES["good morning"]
    if "night" in key:
        return FALLBACK_RESPONSES["good night"]
    return None


def get_groq_reply(api_key: str, model_id: str, temperature: float, history: list, lang: str, system_prompt: str):
    if not GROQ_AVAILABLE:
        st.session_state.last_error = (
            "The 'groq' package isn't installed. Run: pip install groq"
        )
        return None
    try:
        client = Groq(api_key=api_key)
        lang_inst = "Respond in URDU." if lang == 'urdu' else "Respond in ENGLISH."
        messages = [{"role": "system", "content": f"{system_prompt}\n{lang_inst}"}] + history
        response = client.chat.completions.create(
            model=model_id,
            messages=messages,
            temperature=temperature,
            max_tokens=800,
            stream=False,
            timeout=15.0,
        )
        reply = response.choices[0].message.content.strip()
        st.session_state.last_error = None
        return reply or None
    except Exception as e:
        st.session_state.last_error = str(e)
        return None


# ------------------------------------------------------------------
# SESSION STATE INIT
# ------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": WELCOME_MSG}]
    st.session_state.current_chat_id = str(uuid.uuid4())
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = DEFAULT_SYSTEM_PROMPT
if "last_error" not in st.session_state:
    st.session_state.last_error = None
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

# ------------------------------------------------------------------
# SIDEBAR
# ------------------------------------------------------------------
with st.sidebar:
    st.markdown("### ✨ Chat History")

    if st.button("➕ New Chat", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": WELCOME_MSG}]
        st.session_state.current_chat_id = str(uuid.uuid4())
        st.rerun()

    search_term = st.text_input("🔍 Search chats", placeholder="Search by title...", label_visibility="collapsed")
    st.markdown("---")

    all_chats = get_all_chats()
    if search_term:
        all_chats = [c for c in all_chats if search_term.lower() in c["title"].lower()]

    if not all_chats:
        st.caption("No saved chats" if not search_term else "No matches")
    else:
        for chat in all_chats:
            active = st.session_state.get("current_chat_id") == chat["id"]
            col1, col2, col3 = st.columns([0.7, 0.15, 0.15])
            with col1:
                label = f"📄 {chat['title']}"
                if st.button(label, key=f"chat_{chat['id']}", use_container_width=True,
                             type="secondary" if active else "primary"):
                    loaded = load_chat_history(chat["id"])
                    if loaded:
                        st.session_state.messages = loaded["messages"]
                        st.session_state.current_chat_id = chat["id"]
                        st.rerun()
                created_str = chat["created"][:10] if chat["created"] else ""
                st.caption(f"{created_str} · {chat['count']} msgs")
            with col2:
                if st.button("✏️", key=f"ren_{chat['id']}", help="Rename"):
                    st.session_state[f"renaming_{chat['id']}"] = True
            with col3:
                if st.button("🗑️", key=f"del_{chat['id']}", help="Delete"):
                    if delete_chat(chat["id"]):
                        if active:
                            st.session_state.messages = [{"role": "assistant", "content": WELCOME_MSG}]
                            st.session_state.current_chat_id = str(uuid.uuid4())
                        st.rerun()

            if st.session_state.get(f"renaming_{chat['id']}"):
                new_title = st.text_input("New title", value=chat["title"], key=f"newtitle_{chat['id']}")
                rcol1, rcol2 = st.columns(2)
                with rcol1:
                    if st.button("Save", key=f"save_{chat['id']}", use_container_width=True):
                        loaded = load_chat_history(chat["id"])
                        if loaded:
                            save_chat_history(chat["id"], loaded["messages"], title=new_title)
                        st.session_state[f"renaming_{chat['id']}"] = False
                        st.rerun()
                with rcol2:
                    if st.button("Cancel", key=f"cancel_{chat['id']}", use_container_width=True):
                        st.session_state[f"renaming_{chat['id']}"] = False
                        st.rerun()
            st.markdown("---")

    st.markdown("### ⚙️ Settings")

    if not GROQ_AVAILABLE:
        st.warning("`groq` package not found. Run `pip install groq` to enable AI replies.")

    api_key = st.text_input(
        "API Key",
        value=os.environ.get("GROQ_API_KEY", ""),
        type="password",
        help="Get a free key at console.groq.com/keys. Never share or commit this key.",
    )
    model_label = st.selectbox("Model", list(GROQ_MODELS.keys()), index=0)
    temperature = st.slider("Creativity", 0.0, 1.5, 0.7, 0.05)

    with st.expander("🧠 Persona / System Prompt"):
        st.session_state.system_prompt = st.text_area(
            "System prompt", value=st.session_state.system_prompt, height=120,
            label_visibility="collapsed",
        )
        if st.button("Reset to default", use_container_width=True):
            st.session_state.system_prompt = DEFAULT_SYSTEM_PROMPT
            st.rerun()

    with st.expander("📤 Export current chat"):
        txt_export = export_chat_text(st.session_state.messages)
        json_export = json.dumps(st.session_state.messages, indent=2, ensure_ascii=False)
        st.download_button("Download as .txt", data=txt_export, file_name="chat.txt",
                            mime="text/plain", use_container_width=True)
        st.download_button("Download as .json", data=json_export, file_name="chat.json",
                            mime="application/json", use_container_width=True)

    status = "● Connected" if api_key else "● Offline"
    color = "#34d399" if api_key else "#f87171"
    st.markdown(f'<span style="color:{color};">{status}</span>', unsafe_allow_html=True)

    total_chars = sum(len(m["content"]) for m in st.session_state.messages)
    st.caption(f"Session length: {len(st.session_state.messages)} messages · ~{total_chars} chars")

    if st.session_state.last_error:
        st.error(f"Last error: {st.session_state.last_error}")

# ------------------------------------------------------------------
# MAIN AREA — HEADER
# ------------------------------------------------------------------
st.markdown("""
<div class="header-container">
    <div class="main-title">✨ Hasnain AI</div>
    <div class="subtitle">✦ Intelligent · Professional · Conversational ✦</div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "✨"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ---- Action buttons ----
st.markdown('<div class="action-btn-container">', unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": WELCOME_MSG}]
        st.rerun()
with col2:
    if st.button("🔄 Regenerate", use_container_width=True, disabled=len(st.session_state.messages) < 2):
        msgs = st.session_state.messages
        # Drop the trailing assistant reply(ies) back to the last user turn.
        while msgs and msgs[-1]["role"] == "assistant":
            msgs.pop()
        if msgs and msgs[-1]["role"] == "user":
            st.session_state.pending_prompt = msgs.pop()["content"]
            st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

# ---- Chat input ----
typed_prompt = st.chat_input("✍️ Type your message...")
prompt = st.session_state.pending_prompt or typed_prompt
st.session_state.pending_prompt = None

if prompt and prompt.strip():
    prompt = prompt.strip()
    lang = detect_language(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    full_reply = None
    with st.chat_message("assistant", avatar="✨"):
        with st.spinner("Thinking..."):
            personal = match_personal_answer(prompt)
            fallback = get_fallback_reply(prompt) if not personal else None

            if personal:
                full_reply = personal
            elif fallback:
                full_reply = fallback
            elif api_key and GROQ_AVAILABLE:
                history = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages[-8:-1]]
                reply = get_groq_reply(api_key, GROQ_MODELS[model_label], temperature, history, lang,
                                        st.session_state.system_prompt)
                full_reply = reply if reply else "Sorry, I couldn't process that just now. Please try again."
            elif not GROQ_AVAILABLE:
                full_reply = "The `groq` package isn't installed, so I can't reach the AI model. Add it to requirements.txt and reinstall."
            else:
                full_reply = "Please add your Groq API key in the sidebar Settings to enable AI replies."

        st.markdown(full_reply)

    st.session_state.messages.append({"role": "assistant", "content": full_reply})
    save_chat_history(st.session_state.current_chat_id, st.session_state.messages)
    st.rerun()

# ------------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------------
st.markdown("""
<div class="footer">
    Developed with ❤️ by Chaudhary Hasnain · © 2026
</div>
""", unsafe_allow_html=True)
