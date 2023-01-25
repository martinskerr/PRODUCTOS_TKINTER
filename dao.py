import sqlite3

#---------------------------------------------------TABLAS BASE DE DATOS-----------------------------------!!

conn = sqlite3.connect('crm.db')
c = conn.cursor()
c.execute("""

    CREATE TABLE if not exists PRODUCTOS(
        id integer PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL,
        fecha_de_ingreso DATE NOT NULL,
        cantidad_productos INTEGER NOT NULL,
        expiracion DATE NOT NULL,
        tipo_producto TEXT NOT NULL
    )
""")

#---------------------------------------------------TABLAS BASE DE DATOS-----------------------------------!!
