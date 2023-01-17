CREATE TABLE PRODUCTOS(
    
    productos_id number(55) not null,
    tipo_producto varchar2(55) not null,
    expiracion number(55) not null,
    numero_serie number (255) not null,

    CONSTRAINT PRIMARY_KEY_PRODUCTO PRIMARY KEY productos_id

);

CREATE TABLE MERMA(

    tipo_merma varchar2(55) not null,
    expiracion_merma number(55) not null,
    tipo_producto varchar2(55) not null,

    CONSTRAINT PRIMARY_KEY_MERMA PRIMARY KEY tipo_merma,
    CONSTRAINT FK_PRODUCTOS FOREIGN KEY tipo_producto
);