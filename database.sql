CREATE DATABASE testusuariosapi;
CREATE TABLE "usuarios_api_usuario" (
    "id" serial NOT NULL PRIMARY KEY,
    "nombre" varchar(120) NOT NULL,
    "apellido" varchar(120) NOT NULL,
    "direccion" varchar(180) NOT NULL,
    "ciudad" varchar(120) NOT NULL,
    "longitud" double precision NULL,
    "latitud" double precision NULL,
    "estadogeo" boolean NOT NULL);
COMMIT;
