# Establecer la conexión a PostgreSQL mediante python-dotenv
import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

# Carga automáticamente las variables definidas en el archivo .env de la raíz
load_dotenv()

def obtener_conexion():
    try:
        conexion = psycopg2.connect(
            # Formato : os.getenv("nombre exacto que se buscara en el .env", "valor por defecto(si no se encuentra en el .env)" )
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432"),
            database=os.getenv("DB_NAME", "clinica_db"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASS")
        )
        return conexion
        
    except Error as e:
        print(f"[ERROR] No se pudo conectar a PostgreSQL: {e}")
        return None

# Bloque para validacion
if __name__ == "__main__":
    conn = obtener_conexion()
    if conn:
        print("¡Conexión exitosa a PostgreSQL!")
        conn.close()