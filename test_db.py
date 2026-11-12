from database.conexion import obtener_conexion
from controllers.paciente_ctrl import (
    insertar_paciente,
    buscar_paciente_porID,
    actualizar_paciente,
)
from controllers.medico_ctrl import (
    insertar_medico,
    buscar_medico_porID,
    actualizar_medico,
)
from controllers.atencion_ctrl import (
    insertar_atencion,
    buscar_atencion_porID,
    actualizar_atencion,
    atenciones_vigentes,
)

def ejecutar_pruebas():
    print("--- 1. PROBANDO CONEXIÓN ---")
    conn = obtener_conexion()
    if not conn:
        print("Error: No se pudo conectar a PostgreSQL.")
        return
    print("Conexión exitosa.\n")

    print("--- 2. PROBANDO INSERCIONES (PUNTO 3) ---")
    print("Paciente:", insertar_paciente(conn, "20.123.456-7", "Juan Pérez", "911111111"))
    print("Médico:", insertar_medico(conn, "Dra. Ana Gómez", "Cardiología", "922222222"))

    # Atención cerrada (con fecha_alta -> NO debe salir en vigentes)
    print("Atención 1 (cerrada):", insertar_atencion(
        conn,
        id_paciente=1,
        id_medico=1,
        fecha_atencion="2026-11-01",
        diagnostico="Control preventivo",
        costo=35000.00,
        fecha_alta="2026-11-05"
    ))

    # Atención vigente (fecha_alta=None -> SÍ debe salir en vigentes)
    print("Atención 2 (vigente):", insertar_atencion(
        conn,
        id_paciente=1,
        id_medico=1,
        fecha_atencion="2026-11-12",
        diagnostico="Arritmia en observación",
        costo=50000.00,
        fecha_alta=None
    ))
    print()

    print("--- 3. PROBANDO CONSULTA Y MODIFICACIÓN: PACIENTE (PUNTO 4) ---")
    print("Antes:", buscar_paciente_porID(conn, 1))
    print("Update:", actualizar_paciente(conn, 1, "20.123.456-7", "Juan Pérez Soto", "999999999"))
    print("Después:", buscar_paciente_porID(conn, 1))
    print()

    print("--- 4. PROBANDO CONSULTA Y MODIFICACIÓN: MÉDICO (PUNTO 4) ---")
    print("Antes:", buscar_medico_porID(conn, 1))
    print("Update:", actualizar_medico(conn, 1, "Dra. Ana Gómez Silva", "Cardiología Infantil", "988888888"))
    print("Después:", buscar_medico_porID(conn, 1))
    print()

    print("--- 5. PROBANDO CONSULTA Y MODIFICACIÓN: ATENCIÓN (PUNTO 4) ---")
    print("Antes:", buscar_atencion_porID(conn, 2))
    # Modificamos el diagnóstico y costo manteniendo fecha_alta en None para que siga vigente
    print("Update:", actualizar_atencion(
        conn,
        id_atencion=2,
        id_paciente=1,
        id_medico=1,
        fecha_atencion="2026-11-12",
        fecha_alta=None,
        diagnostico="Arritmia severa - En monitoreo",
        costo=65000.00
    ))
    print("Después:", buscar_atencion_porID(conn, 2))
    print()

    print("--- 6. PROBANDO ATENCIONES VIGENTES (PUNTO 5) ---")
    vigentes = atenciones_vigentes(conn)
    print(f"Total vigentes encontradas: {len(vigentes)}")
    for fila in vigentes:
        print(f" -> Paciente: {fila[0]} | Médico: {fila[1]} | Especialidad: {fila[2]}")

    conn.close()
    print("\n--- TODAS LAS PRUEBAS FINALIZADAS ---")

if __name__ == "__main__":
    ejecutar_pruebas()