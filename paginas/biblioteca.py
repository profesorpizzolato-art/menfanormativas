import streamlit as st
from modelos.normativa import obtener_normativas


def mostrar():

    st.header("📖 Biblioteca Normativa")

    busqueda = st.text_input(
        "🔎 Buscar normativa"
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
            "Recursos Humanos",
            "Calidad"
        ]
    )

    st.markdown("---")

    normativas = obtener_normativas()

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

    if normativas:

        for normativa in normativas:

            with st.expander(
                f"{normativa['codigo']} - {normativa['titulo']}"
            ):

                st.write(
                    f"**Organismo:** {normativa['organismo']}"
                )

                st.write(
                    f"**Categoría:** {normativa['categoria']}"
                )

                st.write(
                    f"**Objetivo:** {normativa['objetivo']}"
                )

                st.write(
                    f"**Alcance:** {normativa['alcance']}"
                )

                st.write(
                    f"**Aplicación Operativa:** {normativa['aplicacion']}"
                )

                st.write(
                    f"**Última Actualización:** {normativa['fecha_actualizacion']}"
                )

    else:

        st.warning(
            "No se encontraron normativas."
        )
