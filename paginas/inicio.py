import streamlit as st
from modelos.normativa import obtener_normativas


def mostrar():

    normativas = obtener_normativas()
    total = len(normativas)

    st.title("📚 MENFANormativas")
    st.subheader("Dashboard del Sistema Normativo")

    st.markdown("---")

    # =========================
    # KPIs
    # =========================
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📄 Normativas", total)

    with col2:
        organismos = len(set(n["organismo"] for n in normativas)) if normativas else 0
        st.metric("🏢 Organismos", organismos)

    with col3:
        categorias = len(set(n["categoria"] for n in normativas)) if normativas else 0
        st.metric("📂 Categorías", categorias)

    st.markdown("---")

    # =========================
    # RESUMEN RÁPIDO
    # =========================
    st.subheader("📊 Resumen del Sistema")

    if normativas:

        ultimas = sorted(
            normativas,
            key=lambda x: x["id"],
            reverse=True
        )[:5]

        for n in ultimas:

            st.info(
                f"📌 {n['codigo']} - {n['titulo']} | "
                f"{n['organismo']} | {n['categoria']}"
            )

    else:
        st.warning("No hay normativas cargadas aún.")

    st.markdown("---")

    # =========================
    # DISTRIBUCIÓN POR CATEGORÍA
    # =========================
    st.subheader("📊 Distribución por Categoría")

    if normativas:

        conteo = {}

        for n in normativas:
            cat = n["categoria"]
            conteo[cat] = conteo.get(cat, 0) + 1

        for cat, cantidad in conteo.items():
            st.write(f"**{cat}:** {cantidad}")

    st.markdown("---")

    # =========================
    # MENSAJE FINAL
    # =========================
    st.success(
        "MENFANormativas operativo - MVP 1.0 en desarrollo"
    )
