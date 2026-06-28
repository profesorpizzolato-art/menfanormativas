import streamlit as st

# Configuración general de la página
st.set_page_config(
    page_title="MENFANormativas",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Encabezado principal
# ==========================

st.title("📚 MENFANormativas")
st.subheader("Normativas Aplicadas a la Industria del Petróleo y Gas")

st.markdown("---")

# ==========================
# Descripción de la aplicación
# ==========================

st.markdown("""
### Bienvenido a MENFANormativas

MENFANormativas es una plataforma destinada a la consulta,
interpretación y capacitación sobre las normativas aplicables
a la industria del petróleo y gas.

#### Funcionalidades disponibles:

✅ Biblioteca normativa.

✅ Búsqueda de normativas.

✅ Fichas técnicas.

✅ Material de estudio.

✅ Evaluaciones y capacitaciones.

""")

# ==========================
# Barra lateral
# ==========================

st.sidebar.title("MENFANormativas")

opcion = st.sidebar.radio(
    "Seleccione una opción:",
    [
        "Inicio",
        "Biblioteca Normativa",
        "Favoritos",
        "Perfil"
    ]
)

# ==========================
# Navegación básica
# ==========================

if opcion == "Inicio":
    st.header("🏠 Inicio")

    st.info(
        "Seleccione una opción en el menú lateral para comenzar."
    )

elif opcion == "Biblioteca Normativa":
    st.header("📖 Biblioteca Normativa")

    st.write(
        "Aquí se visualizarán las normativas disponibles."
    )

elif opcion == "Favoritos":
    st.header("⭐ Favoritos")

    st.write(
        "Aquí se mostrarán las normativas guardadas por el usuario."
    )

elif opcion == "Perfil":
    st.header("👤 Perfil")

    st.write(
        "Información del usuario."
    )

# ==========================
# Pie de página
# ==========================

st.markdown("---")

st.caption(
    "© 2026 MENFANormativas | Todos los derechos reservados"
)
