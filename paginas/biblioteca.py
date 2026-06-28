import streamlit as st
from modelos.normativa import obtener_normativas, eliminar_normativa
from servicios.buscador import buscar_normativas


def mostrar():

    st.header("📖 Biblioteca Normativa")

    busqueda = st.text_input("🔎 Buscar normativa")

    categoria = st.selectbox(
        "Categoría",
        [
            "Todas",
            "Seguridad",
            "Producción",
            "Perforación",
            "Laboratorio",
            "Medio Ambiente",
            "Recursos Humanos",
            "Calidad"
        ]
    )

    organismo = st.selectbox(
        "Organismo",
        ["Todos", "ISO", "API", "ASME", "IRAM", "NFPA", "Otro"]
    )

    st.markdown("---")

    normativas = obtener_normativas()

    # =========================
    # BUSCADOR INTELIGENTE
    # =========================
    normativas = buscar_normativas(
        normativas,
        busqueda,
        organismo,
        categoria
    )

    # =========================
    # RESULTADOS
    # =========================
    if normativas:

        for normativa in normativas:

            with st.expander(
                f"📄 {normativa['codigo']} - {normativa['titulo']}"
            ):

                st.write(f"**ID:** {normativa['id']}")
                st.write(f"**Organismo:** {normativa['organismo']}")
                st.write(f"**Categoría:** {normativa['categoria']}")
                st.write(f"**Objetivo:** {normativa['objetivo']}")
                st.write(f"**Alcance:** {normativa['alcance']}")
                st.write(f"**Aplicación:** {normativa['aplicacion']}")
                st.write(f"**Actualización:** {normativa['fecha_actualizacion']}")

                col1, col2 = st.columns(2)

                with col1:
                    if st.button(f"✏️ Editar {normativa['id']}", key=f"edit_{normativa['id']}"):
                        st.session_state["editar_normativa_id"] = normativa["id"]
                        st.switch_page("paginas/administracion.py")

                with col2:
                    if st.button(f"🗑️ Eliminar {normativa['id']}", key=f"del_{normativa['id']}"):
                        eliminar_normativa(normativa["id"])
                        st.success("Normativa eliminada")
                        st.rerun()

    else:
        st.warning("No se encontraron normativas.")
