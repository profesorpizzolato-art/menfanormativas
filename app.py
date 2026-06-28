import streamlit as st

from paginas import inicio
from paginas import biblioteca
from paginas import favoritos
from paginas import perfil

st.set_page_config(
    page_title="MENFANormativas",
    page_icon="📚",
    layout="wide"
)

st.sidebar.title("MENFANormativas")

opcion = st.sidebar.radio(
    "Menú",
    [
        "Inicio",
        "Biblioteca",
        "Favoritos",
        "Perfil"
    ]
)

if opcion == "Inicio":
    inicio.mostrar()

elif opcion == "Biblioteca":
    biblioteca.mostrar()

elif opcion == "Favoritos":
    favoritos.mostrar()

elif opcion == "Perfil":
    perfil.mostrar()

st.sidebar.markdown("---")
st.sidebar.caption("Versión MVP 1.0")
