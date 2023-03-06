CREATE TABLE clinica(
    codigo integer,
    nombre VARCHAR(20),
    direccion VARCHAR(50),
    CONSTRAINT pk_clinica PRIMARY KEY (codigo),
    CONSTRAINT not_nom CHECK(nombre is NOT NULL)
);

CREATE TABLE propietarios(
    DNI VARCHAR(9),
    nombre VARCHAR(20),
    telefono VARCHAR(9),
    CONSTRAINT pk_prop PRIMARY KEY (DNI),
    CONSTRAINT dni_prop CHECK (DNI like '[0-9]{8}[A-Z]{1}'),
    constraint nom_prop CHECK (nombre like '^[A-Z]'),
    constraint telf_prop CHECK (telefono like'6([0-9]){8}')
);

CREATE TABLE animales(
    codigo integer,
    nombre VARCHAR(20),
    especie VARCHAR(20),
    raza VARCHAR(15),
    color_pelo VARCHAR(10),
    fecha_nacimiento DATE,
    DNI_propietario VARCHAR(9),
    CONSTRAINT pk_animales PRIMARY KEY (codigo),
    CONSTRAINT nm_noma CHECK(nombre is NOT NULL),
    CONSTRAINT fk_prop FOREIGN KEY (DNI_propietario) REFERENCES propietarios(DNI),
    CONSTRAINT esp_ani CHECK(especie IN('perro', 'gato', 'conejo', 'pajaro', 'rana'))
);

INSERT INTO clinica (codigo, nombre, direccion) VALUES(6876321, 'San Idelfonso', 'Avenida Andalucia');
INSERT INTO clinica (codigo, nombre, direccion) VALUES(6821231, 'San Agustin', 'Calle Clavel');
INSERT INTO clinica (codigo, nombre, direccion) VALUES(6815375, 'Hospital de Valme', 'Avenida Sevilla');
                                                       
INSERT INTO propietarios (DNI, nombre, telefono) VALUES('49056787Q', 'Juan', 635341422);
INSERT INTO propietarios (DNI, nombre, telefono) VALUES('57568933J', 'Pepe', 665162138);
INSERT INTO propietarios (DNI, nombre, telefono) VALUES('89127544P', 'Andres', 661874630);
                                                       
INSERT INTO animales (codigo, nombre, especie, raza, color_pelo, fecha_nacimiento, DNI_propietario) VALUES( 6666666, 'sira', 'gato', 'persa', 'gris', '2002/01/01', '49056787Q');
INSERT INTO animales (codigo, nombre, especie, raza, color_pelo, fecha_nacimiento, DNI_propietario) VALUES( 6666669, 'coco', 'perro', 'pastor aleman', 'negro', '2002/01/01', '57568933j');    
INSERT INTO animales (codigo, nombre, especie, raza, color_pelo, fecha_nacimiento, DNI_propietario) VALUES( 6666661, 'toby', 'perro', 'yorsair', 'marron, '2002/01/01', '89127544P');                                                       
