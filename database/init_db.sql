-- Eliminar tablas si ya existen
DROP TABLE IF EXISTS atencion;
DROP TABLE IF EXISTS paciente;
DROP TABLE IF EXISTS medico;

-- Tabla PACIENTE
CREATE TABLE paciente (
    id_paciente INT PRIMARY KEY,
    rut VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

-- Tabla Medico
CREATE TABLE medico (
    id_medico INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

-- Tabla Atencion
CREATE TABLE atencion (
    id_atencion INT PRIMARY KEY,
    id_paciente INT NOT NULL REFERENCES paciente(id_paciente),
    id_medico INT NOT NULL REFERENCES medico(id_medico),
    fecha_atencion DATE NOT NULL DEFAULT CURRENT_DATE,
    fecha_alta DATE NULL,
    diagnostico TEXT NOT NULL,
    costo NUMERIC(10, 2) NOT NULL
);