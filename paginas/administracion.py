# paginas/administracion.py

import streamlit as st
from modelos.normativa import (
    agregar_normativa,
    obtener_normativas
)

def mostrar():

    st.header("⚙️
