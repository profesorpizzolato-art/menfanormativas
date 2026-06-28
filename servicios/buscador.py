def buscar_normativas(datos, texto, organismo, categoria):

    resultados = datos

    # =========================
    # FILTRO POR TEXTO
    # =========================
    if texto:

        texto = texto.lower()

        resultados = [
            n for n in resultados
            if texto in n["codigo"].lower()
            or texto in n["titulo"].lower()
            or texto in n["objetivo"].lower()
            or texto in n["aplicacion"].lower()
        ]

    # =========================
    # FILTRO POR ORGANISMO
    # =========================
    if organismo != "Todos":

        resultados = [
            n for n in resultados
            if n["organismo"] == organismo
        ]

    # =========================
    # FILTRO POR CATEGORÍA
    # =========================
    if categoria != "Todas":

        resultados = [
            n for n in resultados
            if n["categoria"] == categoria
        ]

    return resultados
