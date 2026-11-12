


def insertar_atencion(conexion, id_paciente, id_medico, fecha_atencion, fecha_alta, diagnostico, costo):
    cursor = conexion.cursor()
    
    # Si llega None, vacío ("") o solo espacios ("   ") desde Tkinter, lo pasamos a None
    if not fecha_alta or str(fecha_alta).strip() == "":
        fecha_alta = None
    
    insercion = """
    INSERT INTO atencion (id_paciente, id_medico, fecha_atencion, fecha_alta, diagnostico, costo) VALUES
        (%s, %s, %s, %s, %s, %s);
    """
    valores = (id_paciente, id_medico, fecha_atencion, fecha_alta, diagnostico, costo)

    try:
        cursor.execute(insercion, valores)
        conexion.commit()
        return "Atencion agendada con exito."
    except Exception as e:
        conexion.rollback()
        print(f"Error al insertar una atencion: {e}")
    finally:
        cursor.close()



def buscar_atencion_porID(conexion, id_atencion):
    cursor = conexion.cursor()
    consulta = """SELECT id_atencion, id_paciente, id_medico, fecha_atencion, fecha_alta, diagnostico, costo
        FROM atencion
        WHERE id_atencion = %s;
    """
    try:
        #la coma es para que sea una tupla de 1 elemento
        cursor.execute(consulta, (id_atencion,))
        #fetchone() devuelve UNA tupla con los datos de la fila, o NONE
        atencion = cursor.fetchone()
        return atencion
    except Exception as e:
        print(f"Error al buscar la atencion: {e}")
        return None
    finally:
        cursor.close()


def actualizar_atencion(conexion, id_atencion, id_paciente, id_medico, fecha_atencion, fecha_alta, diagnostico, costo):
    cursor = conexion.cursor()
    
    # Si en el formulario de Tkinter dejan la fecha_alta vacía (""), 
    # la convertimos a None para que PostgreSQL la guarde como NULL (atención vigente)
    if fecha_alta == "" or fecha_alta is None:
        fecha_alta = None

    consulta = """
        UPDATE ATENCION 
        SET id_paciente = %s, 
            id_medico = %s, 
            fecha_atencion = %s, 
            fecha_alta = %s, 
            diagnostico = %s, 
            costo = %s
        WHERE id_atencion = %s;
    """
    
    valores = (id_paciente, id_medico, fecha_atencion, fecha_alta, diagnostico, costo, id_atencion)
    
    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        return True, "Atención médica actualizada correctamente."
    except Exception as e:
        conexion.rollback()
        return False, f"Error al actualizar atención: {e}"
    finally:
        cursor.close()

def atenciones_vigentes(conexion):
    cursor = conexion.cursor()

    consulta = """
        SELECT p.nombre, m.nombre, m.especialidad
        FROM paciente p
        JOIN atencion a ON p.id_paciente = a.id_paciente
        JOIN medico m ON m.id_medico = a.id_medico
        WHERE a.fecha_alta IS NULL;
    """

    try:
        cursor.execute(consulta)
        resultados = cursor.fetchall()
        return resultados
    except Exception as e:
        print(f"Error al consultar atenciones vigentes: {e}")
        return []
    finally:
        cursor.close()