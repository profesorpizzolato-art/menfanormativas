# base_datos/conexion.py

import sqlite3


def obtener_conexion():
    conexion = sqlite3.connect(
        "base_datos/menfa_normativas.db",
        check_same_thread=False
    )

    conexion.row_factory = sqlite3.Row

    return conexion
