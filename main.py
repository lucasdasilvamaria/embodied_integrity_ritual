# app/screens/main.py
import streamlit as st
from app.logic.ritual_tracker import get_ritual_steps, log_ritual_completion
import datetime

st.set_page_config(page_title="Embodied Ritual", layout="centered")

st.title("🧘 Embodied Integrity Ritual")
st.subheader(f"Data: {datetime.date.today().strftime('%d/%m/%Y')}")

# Busca passos do ritual (da planilha)
steps = get_ritual_steps()

# Armazena status dos passos
checked = {}

st.markdown("---")
st.write("## Etapas do Ritual")

for step in steps:
    checked[step] = st.checkbox(step)

if st.button("✅ Finalizar Ritual"):
    completed = [step for step, done in checked.items() if done]
    log_ritual_completion(completed)
    st.success("Ritual registrado com sucesso!")

