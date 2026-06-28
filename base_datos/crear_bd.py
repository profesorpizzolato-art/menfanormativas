# base_datos/crear_bd.py

from base_datos.conexion import obtener_conexion


def crear_tablas():

    conexion = obtener_conexion()

    cursor = conexion.cursor()

    # Tabla usuarios
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            contraseña TEXT NOT NULL,
            rol TEXT DEFAULT 'usuario'
        )
    """)

    # Tabla normativas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS normativas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            titulo TEXT NOT NULL,
            organismo TEXT NOT NULL,
            categoria TEXT NOT NULL,
            objetivo TEXT,
            alcance TEXT,
            aplicacion TEXT,
            fecha_actualizacion TEXT
        )
    """)

    # Tabla favoritos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS favoritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER,
            normativa_id INTEGER,

            FOREIGN KEY(usuario_id)
                REFERENCES usuarios(id),

            FOREIGN KEY(normativa_id)
                REFERENCES normativas(id)
        )
    """)

    conexion.commit()
    conexion.close()


if __name__ == "__main__":
    crear_tablas()
    print("Base de datos creada correctamente.")
