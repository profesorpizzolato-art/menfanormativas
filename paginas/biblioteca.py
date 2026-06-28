with st.expander(
    f"📄 {normativa['codigo']} - {normativa['titulo']}"
):

    # =========================
    # FICHA TÉCNICA
    # =========================
    st.markdown("### 📊 Ficha Técnica")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
        **🏢 Organismo:** {normativa['organismo']}  
        **📂 Categoría:** {normativa['categoria']}  
        **📅 Actualización:** {normativa['fecha_actualizacion']}  
        """)

    with col2:
        st.markdown(f"""
        **🆔 ID:** {normativa['id']}  
        **📌 Código:** {normativa['codigo']}  
        """)

    st.markdown("---")

    # =========================
    # CONTENIDO TÉCNICO
    # =========================
    st.markdown("### 📘 Contenido Técnico")

    st.markdown(f"""
    **🎯 Objetivo:**  
    {normativa['objetivo']}

    **📌 Alcance:**  
    {normativa['alcance']}

    **⚙️ Aplicación Operativa:**  
    {normativa['aplicacion']}
    """)

    st.markdown("---")

    # =========================
    # NIVEL DE IMPORTANCIA (SIMULADO)
    # =========================
    st.markdown("### ⚠️ Nivel de Importancia")

    categoria = normativa["categoria"]

    if categoria in ["Seguridad", "Medio Ambiente"]:
        st.error("🔴 CRÍTICO - Alta prioridad operativa")
    elif categoria in ["Producción", "Perforación"]:
        st.warning("🟠 MEDIO - Impacto operativo relevante")
    else:
        st.success("🟢 BAJO - Documentación de soporte")

    st.markdown("---")

    # =========================
    # ACCIONES
    # =========================
    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            f"✏️ Editar {normativa['id']}",
            key=f"edit_{normativa['id']}"
        ):
            st.session_state["editar_normativa_id"] = normativa["id"]
            st.switch_page("paginas/administracion.py")

    with col2:
        if st.button(
            f"🗑️ Eliminar {normativa['id']}",
            key=f"del_{normativa['id']}"
        ):
            eliminar_normativa(normativa["id"])
            st.success("Normativa eliminada")
            st.rerun()
