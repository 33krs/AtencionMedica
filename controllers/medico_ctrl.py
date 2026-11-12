

def insertar_medico(conexion, nombre, especialidad, telefono):
    cursor = conexion.cursor()

    insercion = "INSERT INTO medico(nombre, especialidad, telefono) VALUES (%s, %s, %s);"

    valores = (nombre, especialidad, telefono)

    try:
        cursor.execute(insercion, valores)
        conexion.commit()
        return f"Medico {nombre}, guardado exitosamente."
    
    except Exception as e:
        conexion.rollback()
        print(f"Error al insertar un medico: {e}")

    finally:
        cursor.close()



def buscar_medico_porID(conexion, id_medico):
    cursor = conexion.cursor()
    consulta = """SELECT id_medico, nombre, especialidad, telefono
        FROM medico
        WHERE id_medico = %s;
    """
    try:
        #la coma es para que sea una tupla de 1 elemento
        cursor.execute(consulta, (id_medico,))
        #fetchone() devuelve UNA tupla con los datos de la fila, o NONE
        medico = cursor.fetchone()
        return medico
    except Exception as e:
        print(f"Error al buscar medico: {e}")
        return None
    finally:
        cursor.close()


def actualizar_medico(conexion, id_medico, nombre, especialidad, telefono):
    cursor = conexion.cursor()

    consulta = """
        UPDATE medico
        SET nombre = %s, especialidad=%s, telefono = %s
        WHERE id_medico = %s;
    """
    valores = (nombre,especialidad, telefono, id_medico)
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        return True, f"Datos del medico {id_medico} actualizados correctamente" 
    except Exception as e:
        conexion.rollback()
        return False, f"Error al actualizar al medico: {e}"
    finally:
        cursor.close()