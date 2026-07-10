import json
import streamlit as st


with open("data/base_conhecimento.json", "r", encoding="utf-8") as arquivo:
    base = json.load(arquivo)


st.title("🤖 HealthAssist AI")

pergunta = st.text_input("Digite sua dúvida:")


if pergunta:

    resposta = None

    pergunta = pergunta.lower()

    for categoria, dados in base.items():

        if categoria in pergunta:
            resposta = dados["resposta"]
            break


    if resposta:
        st.success(resposta)

    else:
        st.warning(
            "Não encontrei informações suficientes "
            "para responder essa pergunta."
        )