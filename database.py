# database.py
import sqlite3

# Función para conectar a la base de datos
def get_db():
    conn = sqlite3.connect("usuarios.db")
    conn.row_factory = sqlite3.Row
    return conn

# Crear tabla si no existe
def crear_tabla():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            rol TEXT
        )
    """)

    conn.commit()
    conn.close()

# Llamamos a la función para crear la tabla
crear_tabla()
