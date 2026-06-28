import streamlit as st

def mostrar():

    st.title("📚 MENFANormativas")
    st.subheader(
        "Normativas Aplicadas a la Industria del Petróleo y Gas"
    )

    st.markdown("---")

    st.markdown("""
    ### Bienvenido

    MENFANormativas es una plataforma destinada a la consulta,
    interpretación y capacitación sobre normativas aplicables
    a la industria petrolera.

    #### Funcionalidades:

    - Biblioteca normativa.
    - Búsqueda inteligente.
    - Fichas técnicas.
    - Favoritos.
    - Capacitaciones.
    """)

    st.info(
        "Seleccione una opción desde el menú lateral."
    )
