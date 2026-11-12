# Funciones de los pacientes

def insertar_paciente (conexion, rut, nombre, telefono):
    cursor = conexion.cursor()

    insercion = "INSERT INTO paciente (rut, nombre, telefono) VALUES (%s, %s, %s);"

    valores = (rut, nombre, telefono)

    try:
        #Se pasan la consulta y tupla de valores por separado
        cursor.execute(insercion, valores)
        #.commit() obligatorio en psycopg2 para guardar la transaccion
        conexion.commit()
        return f"Paciente {nombre} guardado exitosamente."
    except Exception as e:
        #Si hubiese algun error, se hace rollback
        conexion.rollback()
        print(f"Error al insertar un paciente: {e}")

    finally: 
        cursor.close()


def buscar_paciente_porID(conexion, id_paciente):
    cursor = conexion.cursor()
    consulta = """SELECT id_paciente, rut, nombre, telefono
        FROM paciente
        WHERE id_paciente = %s;
    """
    try:
        #la coma es para que sea una tupla de 1 elemento
        cursor.execute(consulta, (id_paciente,))
        #fetchone() devuelve UNA tupla con los datos de la fila, o NONE
        paciente = cursor.fetchone()
        return paciente
    except Exception as e:
        print(f"Error al buscar paciente: {e}")
        return None
    finally:
        cursor.close()


def actualizar_paciente(conexion, id_paciente, rut, nombre, telefono):
    cursor = conexion.cursor()

    consulta = """
        UPDATE paciente
        SET rut = %s, nombre = %s, telefono = %s
        WHERE id_paciente = %s;
    """
    valores = (rut, nombre, telefono, id_paciente)
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        return True, f"Datos del paciente {id_paciente} actualizados correctamente" 
    except Exception as e:
        conexion.rollback()
        return False, f"Error al actualizar paciente: {e}"
    finally:
        cursor.close()
