import streamlit as st
from modelos.normativa import obtener_normativas, eliminar_normativa


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

    st.markdown("---")

    normativas = obtener_normativas()

    # =========================
    # FILTROS
    # =========================
    if busqueda:
        normativas = [
            n for n in normativas
            if busqueda.lower() in n["codigo"].lower()
            or busqueda.lower() in n["titulo"].lower()
        ]

    if categoria != "Todas":
        normativas = [
            n for n in normativas
            if n["categoria"] == categoria
        ]

    # =========================
    # MOSTRAR RESULTADOS
    # =========================
    if normativas:

        for normativa in normativas:

            with st.expander(
                f"{normativa['codigo']} - {normativa['titulo']}"
            ):

                st.write(f"**ID:** {normativa['id']}")
                st.write(f"**Organismo:** {normativa['organismo']}")
                st.write(f"**Categoría:** {normativa['categoria']}")
                st.write(f"**Objetivo:** {normativa['objetivo']}")
                st.write(f"**Alcance:** {normativa['alcance']}")
                st.write(f"**Aplicación Operativa:** {normativa['aplicacion']}")
                st.write(f"**Última Actualización:** {normativa['fecha_actualizacion']}")

                # =========================
                # ACCIONES
                # =========================
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
