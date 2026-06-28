import streamlit as st

def mostrar():

    st.header("📖 Biblioteca Normativa")

    busqueda = st.text_input(
        "Buscar normativa"
    )

    categoria = st.selectbox(
        "Categoría",
        [
            "Todas",
            "Seguridad",
            "Producción",
            "Perforación",
            "Laboratorio",
            "Medio Ambiente",
            "Recursos Humanos"
        ]
    )

    st.markdown("---")

    st.write("Aquí aparecerán las normativas disponibles.")
