# modelos/normativa.py

from base_datos.conexion import obtener_conexion


def obtener_normativas():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM normativas
        ORDER BY codigo
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def obtener_normativa_por_id(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT * FROM normativas
        WHERE id = ?
    """, (id,))

    dato = cursor.fetchone()

    conexion.close()

    return dato


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
        fecha_actualizacion
    ))

    conexion.commit()
    conexion.close()


def actualizar_normativa(
        id,
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
        UPDATE normativas
        SET
            codigo = ?,
            titulo = ?,
            organismo = ?,
            categoria = ?,
            objetivo = ?,
            alcance = ?,
            aplicacion = ?,
            fecha_actualizacion = ?
        WHERE id = ?
    """, (
        codigo,
        titulo,
        organismo,
        categoria,
        objetivo,
        alcance,
        aplicacion,
        fecha_actualizacion,
        id
    ))

    conexion.commit()
    conexion.close()


def eliminar_normativa(id):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM normativas
        WHERE id = ?
    """, (id,))

    conexion.commit()
    conexion.close()
