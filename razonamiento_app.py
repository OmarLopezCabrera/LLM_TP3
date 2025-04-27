
import streamlit as st
from agent_module import query_razonamiento

st.title("🧠 Chatbot Modular de Razonamiento Avanzado - 6 Agentes")
st.write("Resuelve preguntas complejas combinando agentes especializados en 6 fases.")

pregunta = st.text_area("Escribe una pregunta compleja:")

if st.button("Enviar"):
    with st.spinner("Procesando..."):
        result = query_razonamiento(pregunta)
        
        st.subheader("Respuesta Final (Revisada)")
        st.write(result["answer"])

        st.subheader("Tokens Utilizados (Estimado)")
        col1, col2, col3 = st.columns(3)
        col1.metric("Tokens de Entrada (Estimado)", result["tokens"]["input"])
        col2.metric("Tokens de Salida (Estimado)", result["tokens"]["output"])
        col3.metric("Tokens de Razonamiento (Estimado)", result["tokens"]["reasoning"])
        st.metric("Total de Tokens (Estimado)", result["tokens"]["total"])

        st.subheader("Proceso de Razonamiento")
        for fase, contenido in result["intermediate_steps"].items():
            with st.expander(f"{fase}"):
                st.write(contenido)
