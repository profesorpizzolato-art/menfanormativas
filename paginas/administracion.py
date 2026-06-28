import streamlit as st
from modelos.normativa import (
    agregar_normativa,
    obtener_normativas,
    obtener_normativa_por_id,
    actualizar_normativa
)


def limpiar_edicion():
    if "editar_normativa_id" in st.session_state:
        del st.session_state["editar_normativa_id"]


def mostrar():

    st.header("⚙️ Administración de Normativas")

    editar_id = st.session_state.get("editar_normativa_id", None)

    normativa_editar = None

    if editar_id:
        normativa_editar = obtener_normativa_por_id(editar_id)
        st.info(f"Modo edición: ID {editar_id}")

    # =========================
    # FORMULARIO
    # =========================
    with st.form("formulario_normativa"):

        st.subheader(
            "Editar Normativa" if editar_id else "Nueva Normativa"
        )

        codigo = st.text_input(
            "Código",
            value=normativa_editar["codigo"] if normativa_editar else ""
        )

        titulo = st.text_input(
            "Título",
            value=normativa_editar["titulo"] if normativa_editar else ""
        )

        organismo = st.selectbox(
            "Organismo",
            ["ISO", "API", "ASME", "IRAM", "NFPA", "Otro"],
            index=0
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

        objetivo = st.text_area(
            "Objetivo",
            value=normativa_editar["objetivo"] if normativa_editar else ""
        )

        alcance = st.text_area(
            "Alcance",
            value=normativa_editar["alcance"] if normativa_editar else ""
        )

        aplicacion = st.text_area(
            "Aplicación Operativa",
            value=normativa_editar["aplicacion"] if normativa_editar else ""
        )

        fecha_actualizacion = st.date_input(
            "Fecha de Actualización"
        )

        guardar = st.form_submit_button(
            "Actualizar" if editar_id else "Guardar"
        )

        # =========================
        # GUARDAR / ACTUALIZAR
        # =========================
        if guardar:

            if editar_id:

                actualizar_normativa(
                    editar_id,
                    codigo,
                    titulo,
                    organismo,
                    categoria,
                    objetivo,
                    alcance,
                    aplicacion,
                    str(fecha_actualizacion)
                )

                st.success("Normativa actualizada correctamente.")
                limpiar_edicion()
                st.rerun()

            else:

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

                st.success("Normativa creada correctamente.")
                st.rerun()

    # =========================
    # LISTADO
    # =========================
    st.markdown("---")
    st.subheader("Normativas Registradas")

    normativas = obtener_normativas()

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
                st.write(f"**Aplicación:** {normativa['aplicacion']}")

    else:
        st.info("Todavía no existen normativas cargadas.")
