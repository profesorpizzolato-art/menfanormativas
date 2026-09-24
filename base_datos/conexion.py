```python
import sqlite3
from pathlib import Path


# ============================================================
# UBICACIÓN DE LA BASE DE DATOS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "menfa_normativas.db"


# ============================================================
# CONEXIÓN
# ============================================================

def obtener_conexion():

    conexion = sqlite3.connect(
        DB_PATH,
        check_same_thread=False
    )

    conexion.row_factory = sqlite3.Row

    return conexion


# ============================================================
# INICIALIZACIÓN DE LA BASE
# ============================================================

def inicializar_base_datos():

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS normativas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT NOT NULL,
            titulo TEXT NOT NULL,
            organismo TEXT,
            categoria TEXT,
            objetivo TEXT,
            alcance TEXT,
            aplicacion TEXT,
            fecha_actualizacion TEXT
        )
    """)

    conexion.commit()
    conexion.close()
```
