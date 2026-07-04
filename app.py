import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)

# Page config
st.set_page_config(page_title="RuleBot Web", page_icon="🤖", layout="centered")
st.title("🤖 RuleBot: Smart AI Assistant")
st.caption("powered By Decodelabs")

# Initialize Gemini API (Try env var first, then Streamlit secrets)
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        pass

if not api_key:
    st.error("API Key not found. Please add your GEMINI_API_KEY to the .env file or Streamlit Secrets.")
    st.stop()

genai.configure(api_key=api_key)

# Initialize the chat model and history in session state
if "chat_session" not in st.session_state:
    model = genai.GenerativeModel('gemini-2.5-flash')
    st.session_state.chat_session = model.start_chat(history=[])

# Display chat history from session state
for message in st.session_state.chat_session.history:
    role = "assistant" if message.role == "model" else "user"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

# Chat input
if user_input := st.chat_input("Type your message here..."):
    # Display user message immediately
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get response from Gemini
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_session.send_message(user_input)
                st.markdown(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
