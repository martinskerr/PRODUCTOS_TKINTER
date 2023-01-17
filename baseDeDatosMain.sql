CREATE TABLE PRODUCTOS(
    
    tipo_producto varchar2(55) not null,
    expiracion number(10) not null,
    numero_serie number (10) not null,

    CONSTRAINT PRIMARY_KEY_PRODUCTO PRIMARY KEY (numero_serie)

);

CREATE TABLE MERMA(
    
    nombre_Producto varchar(55) not null,
    tipo_merma varchar2(55) null,
    expiracion_merma number(10) not null,
    numero_serie number(10) not null,

    CONSTRAINT PRIMARY_KEY_MERMA PRIMARY KEY(nombre_Producto),
    CONSTRAINT FK_PRODUCTOS FOREIGN KEY (numero_serie) REFERENCES PRODUCTOS(numero_serie)
);