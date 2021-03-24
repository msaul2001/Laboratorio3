CREATE DATABASE laboratorio1;
Use laboratorio1;

#Creamos la Tabla Usuario
CREATE TABLE Usuarios(
idUsuario int auto_increment primary key,
username varchar(50) not null,
password varchar(50) not null,
email varchar(70) not null,
creationDate date not null
);

#Insertamos Datos en Usuarios
insert into Usuarios(username, password, email, creationDate)
    VALUES ('Pepe', md5(md5('Pepe') + md5('Contrasenia')), 'sebash@gmail.com',now());

insert into Usuarios(username, password, email, creationDate)
    VALUES ('Carlos01', md5(md5('Carlos01') + md5('Carlitos123')), 'carlth@gmail.com',now());

SELECT * FROM Usuarios;

#Creamos la Tabla Compras
CREATE TABLE Compras(
idCompra int auto_increment primary key,
totalCompra double(7,2) not null,
fechaHoraCompra DATETIME not null,
idUsuario int not null,

CONSTRAINT fk_llaveUsuarios Foreign Key(idUsuario)
    references Usuarios(idUsuario) ON delete no action
            on update cascade
);

#Insertamos Datos en compras
insert into Compras(totalCompra, fechaHoraCompra, idUsuario)
    values (450.5,now(),1);

insert into Compras(totalCompra, fechaHoraCompra, idUsuario)
    values (750.5,now(),2);

#Creamos la Tabla Productos

CREATE TABLE Productos(
idProducto int auto_increment primary key,
nombreProducto varchar(70) not null,
descripcion varchar(50) not null,
precioUnitario double(6,2) not null,
catedoria ENUM('Tecnologia','Linea Blanca','Cuidado Personal','Moda','Transporte') not null
);

#Creacion de La Tabla DetalleCompras

CREATE TABLE DetalleCompras(
    idDT int auto_increment primary key,
    cantComprada int not null,
    subTotal Double (7,2),
    idProducto int not null,
    idCompra int not null,

    CONSTRAINT fk_llaveCompra foreign key (idCompra)
        references Compras(idCompra) on delete no action
            on update cascade,
    CONSTRAINT fk_llaveProducto foreign key (idProducto)
        references Productos(idProducto) on delete  no action
            on update cascade
);

INSERT INTO DetalleCompras(cantComprada,idProducto, idCompra)

SELECT * from DetalleCompras;