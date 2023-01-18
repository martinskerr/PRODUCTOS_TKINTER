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
        fecha_ingreso_producto TEXT NOT NULL,
        cantidad_productos INTEGER NOT NULL,
        expiracion INTEGER NOT NULL,
        tipo_producto TEXT NOT NULL
    )
""")

#---------------------------------------------------TABLAS BASE DE DATOS-----------------------------------!!


#-----------------------------------creacion interfaz grafica con tkinter-----------------------------------!!
root = Tk()
root.title('BASE DE DATOS: INGRESO PRODUCTOS')

def eliminarTablaProductos():
    result = c.execute("DROP TABLE PRODUCTOS").fetchall()
    conn.commit()
    if result:
        messagebox.showinfo("Eliminar tabla", "Tabla eliminada exitosamente")
    else:
        messagebox.showerror("Error", "No se pudo eliminar la tabla")


def renderProductos():
    rows = c.execute("SELECT * FROM PRODUCTOS").fetchall()

    tree.delete(*tree.get_children())
    
    for row in rows:
        tree.insert('', END, row[0], values=(row[1], row[2], row[3], row[4], row[5]))


def insertar(productos):
    c.execute("""
    
        INSERT INTO PRODUCTOS(nombre_producto,fecha_de_ingreso, cantidad_productos, expiracion, tipo_producto ) VALUES (?,?,?,?,?)
    
    """, (productos['nombre'],productos['fecha_de_ingreso'], productos['cantidad'], productos['expiracion'], productos['tipoProducto']))
    conn.commit()
    renderProductos()


def nuevo_producto():
    def guardar():
        if not nombre.get():
            messagebox.showerror("Error", "el nombre es obligatorio")
            return

        if not fecha_de_ingreso.get():
            messagebox.showerror("Error", "la fecha de ingreso del producto es obligatorio")
            return            
            
        if not cantidad.get():
            messagebox.showerror("Error", "la cantidad de productos es obligatoria")
            return

        if not expiracion.get():
            messagebox.showerror("Error", "la fecha de expiracion del producto es obligatoria.")
            return

        if not tipoProducto.get():
            messagebox.showerror("Error", "el tipo de producto es obligatorio")
            return

        productos = {
            'nombre': nombre.get(),
            'fecha_de_ingreso': fecha_de_ingreso.get(),
            'expiracion': expiracion.get(),
            'tipoProducto': tipoProducto.get(),
            'cantidad': cantidad.get(),           
            
        }
        insertar(productos)
        top.destroy()

    top = Toplevel()
    top.title("Nuevo Producto")

    lnombre = Label(top, text='Nombre')
    nombre = Entry(top, width=40)
    lnombre.grid(row=0, column=0)
    nombre.grid(row=0, column=1)

    lfecha_de_ingreso = Label(top, text='fecha_de_ingreso')
    fecha_de_ingreso = Entry(top, width=40)
    lfecha_de_ingreso.grid(row=1, column=0)
    fecha_de_ingreso.grid(row=1, column=1)

    lexpiracion = Label(top, text='Expiracion')
    expiracion = Entry(top, width=40)
    lexpiracion.grid(row=2, column=0)
    expiracion.grid(row=2, column=1)

    ltipoProducto = Label(top, text='TipoProducto')
    tipoProducto = Entry(top, width=40)
    ltipoProducto.grid(row=3, column=0)
    tipoProducto.grid(row=3, column=1)

    lcantidad = Label(top, text='Cantidad')
    cantidad = Entry(top, width=40)
    lcantidad.grid(row=4, column=0)
    cantidad.grid(row=4, column=1)    

    guardar = Button(top, text='Guardar', command=guardar)
    guardar.grid(row=5, column=1)

    top.mainloop()

def eliminar_producto():
    
    id = tree.selection()[0]
    

    productos = c.execute("SELECT * FROM PRODUCTOS WHERE id = ?", (id, )).fetchone()
    respuesta = messagebox.askokcancel("Seguro?", "Estas seguro de querer eliminar el producto '" + productos[1] + "'?")
    
    if respuesta:

        c.execute("DELETE FROM PRODUCTOS WHERE id = ? ",[id, ])
        conn.commit()
        renderProductos()
    else:
        pass


btn = Button(root, text='Nuevo Producto', command=nuevo_producto)
btn.grid(column=0, row=0)

btn_eliminar = Button(root, text='Eliminar Producto', command=eliminar_producto)
btn_eliminar.grid(column=1, row=0)

btn_eliminar_tabla = Button(root, text='Eliminar Tabla PRODUCTOS', command=eliminarTablaProductos)
btn_eliminar_tabla.grid(column=2, row=0)

tree = ttk.Treeview(root)
tree['columns'] = ('NombreProducto','fecha_de_ingreso', 'Cantidad', 'Expiracion', 'TipoProducto')

tree.column('#0', width=0, stretch=NO)
tree.column("NombreProducto")
tree.column("fecha_de_ingreso")
tree.column("Cantidad")
tree.column("Expiracion")
tree.column("TipoProducto")

tree.heading("NombreProducto", text='Nombre Producto')
tree.heading("fecha_de_ingreso",  text='Fecha de ingreso')
tree.heading("Cantidad", text='Cantidad')
tree.heading("Expiracion", text='Expiracion')
tree.heading("TipoProducto", text='Tipo Producto')

tree.grid(column=0, row=1, columnspan=2)

renderProductos()
root.mainloop()

