# modelos/normativa.py

from base_datos.conexion import obtener_conexion


def obtener_normativas():

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM normativas
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def agregar_normativa(
        codigo,
        titulo,
        organismo,
        categoria,
        objetivo,
        alcance,
        aplicacion,
        fecha_actualizacion):

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO normativas(
            codigo,
            titulo,
            organismo,
            categoria,
            objetivo,
            alcance,
            aplicacion,
            fecha_actualizacion
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        codigo,
        titulo,
        organismo,
        categoria,
        objetivo,
        alcance,
        aplicacion,
