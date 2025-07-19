import streamlit as st
import json
import os
from datetime import date
from app.logic.ritual_tracker import log_ritual_completion

steps_file = "data/ritual_steps.json"
tags_file = "data/ritual_tags.json"

# Carrega etapas
def load_steps():
    if os.path.exists(steps_file):
        with open(steps_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salva etapas
def save_steps(steps):
    with open(steps_file, "w", encoding="utf-8") as f:
        json.dump(steps, f, ensure_ascii=False, indent=2)

# Carrega tags sugeridas
def load_tags():
    if os.path.exists(tags_file):
        with open(tags_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salva tags
def save_tags(tags):
    with open(tags_file, "w", encoding="utf-8") as f:
        json.dump(tags, f, ensure_ascii=False, indent=2)

st.title("🧘 Embodied Integrity Ritual")
st.write(f"**Data:** {date.today().strftime('%d/%m/%Y')}")

steps = load_steps()
tags_suggestions = load_tags()
edited_steps = steps.copy()

st.subheader("Etapas do Ritual")

completed = []
for i, step in enumerate(steps):
    col1, col2, col3 = st.columns([6, 1, 1])
    with col1:
        checked = st.checkbox(f'{step["name"]} ({step["category"]})', key=f"check_{i}")
        if checked:
            tag_input = st.text_input("Tag para este registro (opcional)", key=f"tag_input_{i}",
                                      placeholder="Ex: dor, tédio, prazer…",
                                      help="Esta tag é registrada apenas para hoje.")
            step_copy = step.copy()
            step_copy["tag"] = tag_input.strip()
            completed.append(step_copy)

    with col2:
        if st.button("✏️", key=f"edit_{i}"):
            st.session_state[f"edit_mode_{i}"] = not st.session_state.get(f"edit_mode_{i}", False)

    with col3:
        if st.button("🗑️", key=f"delete_{i}"):
            del edited_steps[i]
            save_steps(edited_steps)
            st.rerun()

    if st.session_state.get(f"edit_mode_{i}", False):
        with st.expander("Editar etapa"):
            new_name = st.text_input("Editar nome", value=step["name"], key=f"name_input_{i}")
            new_category = st.text_input("Editar categoria", value=step["category"], key=f"cat_input_{i}")
            if st.button("Salvar edição", key=f"save_edit_{i}"):
                edited_steps[i] = {"name": new_name, "category": new_category}
                save_steps(edited_steps)
                st.success("Etapa atualizada!")
                st.rerun()

# ➕ Adicionar nova etapa
st.subheader("➕ Adicionar nova etapa")
new_name = st.text_input("Nome da nova etapa", key="new_step_name")
new_category = st.text_input("Categoria da nova etapa", key="new_step_category")

if st.button("Adicionar etapa"):
    if new_name and new_category:
        new_step = {"name": new_name, "category": new_category}
        steps.append(new_step)
        save_steps(steps)
        st.success("Etapa adicionada com sucesso!")
        st.rerun()
    else:
        st.warning("Preencha o nome e a categoria.")

# 🔘 Registro final
if st.button("Registrar ritual"):
    if completed:
        log_ritual_completion(completed)
        for step in completed:
            tag = step.get("tag", "")
            if tag and tag not in tags_suggestions:
                tags_suggestions.append(tag)
        save_tags(tags_suggestions)
        st.success("Ritual registrado com sucesso!")
    else:
        st.warning("Você precisa marcar pelo menos uma etapa para registrar.")
