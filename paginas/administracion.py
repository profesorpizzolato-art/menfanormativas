import streamlit as st
from modelos.normativa import (
    agregar_normativa,
    obtener_normativas
)

def mostrar():

    st.header("⚙️ Administración de Normativas")

    with st.form("formulario_normativa"):

        st.subheader("Nueva Normativa")

        codigo = st.text_input("Código")

        titulo = st.text_input("Título")

        organismo = st.selectbox(
            "Organismo",
            ["ISO", "API", "ASME", "IRAM", "NFPA", "Otro"]
        )

        categoria = st.selectbox(
            "Categoría",
            [
                "Seguridad",
                "Producción",
                "Perforación",
                "Laboratorio",
                "Medio Ambiente",
                "Recursos Humanos",
                "Calidad"
            ]
        )

        objetivo = st.text_area("Objetivo")

        alcance = st.text_area("Alcance")

        aplicacion = st.text_area(
            "Aplicación Operativa"
        )

        fecha_actualizacion = st.date_input(
            "Fecha de Actualización"
        )

        guardar = st.form_submit_button("Guardar Normativa")

        if guardar:

            agregar_normativa(
                codigo,
                titulo,
                organismo,
                categoria,
                objetivo,
                alcance,
                aplicacion,
                str(fecha_actualizacion)
            )

            st.success("Normativa guardada correctamente.")

    st.markdown("---")

    st.subheader("Normativas Registradas")

    normativas = obtener_normativas()

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
                    f"**Aplicación:** {normativa['aplicacion']}"
                )

    else:

        st.info(
            "Todavía no existen normativas cargadas."
        )
