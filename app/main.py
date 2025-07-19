import streamlit as st

st.set_page_config(page_title="Embodied Integrity Ritual", layout="centered")

st.title("🧘 Embodied Integrity Ritual")
st.write("Welcome, Newen.")

if st.button("Start Ritual"):
    st.success("Ritual Started!")
