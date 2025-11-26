import streamlit as st
from components.ai_engine import generate_chat_answer
from components.ai_prompt import CHATBOT_SYSTEM

def chatbot_ui(df):
   
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Wrapper
    st.markdown("<div class='chat-wrapper'>", unsafe_allow_html=True)

    # Render chat history
    for role, msg in st.session_state.chat_history:
        if role == "user":
            st.markdown(
                f"<div class='chat-bubble user-bubble'>{msg}</div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"<div class='chat-bubble bot-bubble'>{msg}</div>",
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)

    # Input user
    user_input = st.chat_input("Ketik pesan…")
    if user_input:
        st.session_state.chat_history.append(("user", user_input))
        answer = generate_chat_answer(df, user_input)
        st.session_state.chat_history.append(("assistant", answer))
        st.rerun()