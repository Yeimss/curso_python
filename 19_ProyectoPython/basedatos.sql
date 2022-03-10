CREATE DATABASE IF NOT EXISTS master_py;
use master_py;

CREATE TABLE usuarios(
id          int(25) auto_increment,
nombre      varchar(100),
apellidos   varchar(100),
email       varchar(125) not null unique,
contraseña  varchar(255) not null,
fecha       date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id)
)ENGINE=InnoDb;

CREATE TABLE notas(
id int(25) auto_increment,
usuario_id int(25) not null,
titulo varchar(255) not null,
descripcion MEDIUMTEXT,
fecha date not null,
CONSTRAINT pk_nota PRIMARY KEY(id),
CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;
