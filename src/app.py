# app.py
import streamlit as st
from agente import perguntar # Importa a função que criamos no agente.py

st.title("🪐 Mestre Yodindin 🤑")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.session_state.messages.append({"role": "user", "content": pergunta})
    with st.chat_message("user"):
        st.markdown(pergunta)
    
    with st.spinner("Consultando os pergaminhos..."):
        resposta = perguntar(pergunta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
        with st.chat_message("assistant"):
            st.markdown(resposta)