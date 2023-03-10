from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
import os
from datetime import datetime
from dao import *
#---------------------------------------------------Imports-----------------------------------!!

#-----------------------------------creacion interfaz grafica con tkinter-----------------------------------!!

#las tablas SQL se importan directamente desde dao.py en el directorio 

#funcion principol que contiene las intrucciones
def main():
    root = Tk()
    root.title('BASE DE DATOS: INGRESO PRODUCTOS')
    root.geometry("1280x720+300+200")


    #tiempo actual
    def tiempo_actual():
        current_date = datetime.now().date().strftime("%d-%m-%Y")
        return current_date

    def renderProductos():
        rows = c.execute("SELECT * FROM PRODUCTOS").fetchall()

        tree.delete(*tree.get_children())
        
        for row in rows:
            tree.insert('', END, row[0], values=(row[1], row[2], row[3], row[4], row[5]))

#genera un excel con las tablas, aun no genera automaticamente lo que trae las tablas


    def generador_excel():
        # Obtener los productos de la tabla
        products = c.execute("SELECT * FROM PRODUCTOS").fetchall()

        # Crear una lista para almacenar los datos del archivo CSV
        data = [['Nombre Producto','Fecha de ingreso','Cantidad','Expiracion', 'Tipo Producto']]

        # Iterar sobre los productos y agregarlos a la lista de datos
        for product in products:
            data.append([product[1], product[2], product[3], product[4], product[5]])

        # Abre el archivo en modo escritura
        with open('data.csv', 'w', newline='') as file:
            # Crea un objeto CSV writer
            csv_writer = csv.writer(file)
            # Escribir cada fila de datos en el archivo
            for row in data:
                csv_writer.writerow(row)
                
        # Abrir el archivo generado
        os.startfile('data.csv')

    def insertar(productos):
        c.execute("""
        
            INSERT INTO PRODUCTOS(nombre_producto,fecha_de_ingreso, cantidad_productos, expiracion, tipo_producto ) VALUES (?,?,?,?,?)
        
        """, (productos['nombre'],productos['fecha_de_ingreso'], productos['cantidad'], productos['expiracion'], productos['tipoProducto']))
        conn.commit()
        renderProductos()

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


    def nuevo_producto():
        def guardar():
            if not nombre.get():
                messagebox.showerror("Error", "el nombre es obligatorio")
                return       

            if not expiracion.get():
                messagebox.showerror("Error", "la fecha de expiracion del producto es obligatoria.")
                return


            if not tipoProducto.get():
                messagebox.showerror("Error", "el tipo de producto es obligatorio")
                return

            try:
                # convertir la cadena de texto en un objeto de fecha
                expiracion_date = datetime.strptime(expiracion.get(), "%d/%m/%Y")
                fecha_expiracion = expiracion_date.date()

                productos = {
                    'nombre': nombre.get(),
                    'fecha_de_ingreso': tiempo_actual(),
                    'expiracion': expiracion_date,
                    'tipoProducto': tipoProducto.get(),
                    'cantidad': cantidad.get(),           
                }
                insertar(productos)
                top.destroy()
            except ValueError:
                # Mostrar un mensaje de error
                messagebox.showerror("Error", "El formato de fecha de expiracion es incorrecto. Debe ser dd/mm/yyyy.")


        #creacion de las tablas con funcion grid y tree de tkinter 

        top = Toplevel()
        top.title("Nuevo Producto")

        lnombre = Label(top, text='Nombre')
        nombre = Entry(top, width=40)
        lnombre.grid(row=0, column=0)
        nombre.grid(row=0, column=1)

        lfecha_de_ingreso = Label(top, text='Fecha de ingreso')
        lfecha_de_ingreso.grid(row=1, column=0)

        lexpiracion = Label(top, text='Expiracion')
        expiracion = Entry(top, width=40)
        lexpiracion.grid(row=2, column=0)
        expiracion.grid(row=2, column=1)

        ltipoProducto = Label(top, text='Tipo Producto')
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

    

    btn = Button(root, text='Nuevo Producto', command=nuevo_producto)
    btn.grid(column=0, row=0)

    btn_eliminar = Button(root, text='Eliminar Producto', command=eliminar_producto)
    btn_eliminar.grid(column=1, row=0)

    btn_generar_csv = Button(root, text='Generar archivo CSV - EXCEL', command=generador_excel)
    btn_generar_csv.grid(column=2, row=0)

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

    tree.grid(column=1, row=1, columnspan=3,sticky="nsew", padx=10, pady=10)
    root.grid_columnconfigure(0, weight=2)
    root.grid_rowconfigure(1, weight=2) 
    renderProductos()

    root.mainloop()

#inicializacion del software
main()