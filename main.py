import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#---------------------------------------------------Imports-----------------------------------!!

#---------------------------------------------------TABLAS BASE DE DATOS-----------------------------------!!

conn = sqlite3.connect('crm.db')
c = conn.cursor()
c.execute("""

    CREATE TABLE if not exists PRODUCTOS(
        id integer PRIMARY KEY AUTOINCREMENT,
        nombre_producto TEXT NOT NULL,
        cantidad_productos INTEGER NOT NULL,
        expiracion INTEGER NOT NULL,
        tipo_producto TEXT NOT NULL
    )
""")

#---------------------------------------------------TABLAS BASE DE DATOS-----------------------------------!!


#-----------------------------------creacion interfaz grafica con tkinter-----------------------------------!!
root = Tk()
root.title('BASE DE DATOS: INVENTARIO')

def nuevo_producto():
    def guardar():
        pass

    top = Toplevel()
    top.title("Nuevo Producto")

    lnombre = Label(top, text='Nombre')
    nombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    nombre.grid(row=0, column=1)

    lnombre = Label(top, text='Nombre')
    nombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    nombre.grid(row=0, column=1)

    lTipoProducto = Label(top, text='TipoProducto')
    TipoProducto = Entry(top, width=40)
    lTipoProducto.grid(row=2, column=0)
    TipoProducto.grid(row=2, column=1)

    lCantidad = Label(top, text='Cantidad')
    Cantidad = Entry(top, width=40)
    lCantidad.grid(row=3, column=0)
    Cantidad.grid(row=3, column=1)    

    guardar = Button(top, text='Guardar', command=guardar)
    guardar.grid(row=4, column=1)

    top.mainloop()

def eliminar_producto():
    pass

btn = Button(root, text='Nuevo Producto', command=nuevo_producto)
btn.grid(column=0, row=0)

btn_eliminar = Button(root, text='Eliminar Producto', command=eliminar_producto)
btn_eliminar.grid(column=1, row=0)

tree = ttk.Treeview(root)
tree['columns'] = ('NombreProducto', 'Expiracion', 'TipoProducto', 'Cantidad')

tree.column('#0', width=0, stretch=NO)
tree.column("NombreProducto")
tree.column("Expiracion")
tree.column("TipoProducto")
tree.column("Cantidad")

tree.heading("NombreProducto", text='Nombre Producto')
tree.heading("Expiracion", text='Expiracion')
tree.heading("TipoProducto", text='Tipo Producto')
tree.heading("Cantidad", text='Cantidad')

tree.grid(column=0, row=1, columnspan=2)

root.mainloop()





# numero_serie = 1123123
# expiracion = 10/12/24
# tipo_producto = "panaderia"

# root = Tk()
# root.title("TreeView")

# tree = ttk.Treeview(root)
# tree['columns'] = ('numero_serie', 'expiracion', 'tipo_producto')

# # tree.column('#0')
# tree.column('#0', width=0, stretch=NO)
# tree.column("numero_serie")
# tree.column("expiracion")
# tree.column("tipo_producto")

# # tree.heading("#0", text='id')
# tree.heading("#0")
# tree.heading("numero_serie", text='N° De Serie')
# tree.heading("expiracion", text='Fecha de vencimiento')
# tree.heading("tipo_producto", text='Tipo de Producto')

# tree.insert('', END, 'lala', values=(numero_serie,expiracion ,tipo_producto ), text='FILA1')
# tree.insert('', END, 'lele', values=('Cuatro', 'Cinco', 'Seis'), text='FILA2')
