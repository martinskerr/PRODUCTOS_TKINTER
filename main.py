import conexion
import requests
import cx_Oracle
from tkinter import *
from tkinter import ttk
#---------------------------------------------------Imports-----------------------------------!!
#creacion interfaz grafica con tkinter

numero_serie = 1123123
expiracion = 10/12/24
tipo_producto = "panaderia"

root = Tk()
root.title("TreeView")

tree = ttk.Treeview(root)
tree['columns'] = ('numero_serie', 'expiracion', 'tipo_producto')

# tree.column('#0')
tree.column('#0', width=0, stretch=NO)
tree.column("numero_serie")
tree.column("expiracion")
tree.column("tipo_producto")

# tree.heading("#0", text='id')
tree.heading("#0")
tree.heading("numero_serie", text='N° De Serie')
tree.heading("expiracion", text='Fecha de vencimiento')
tree.heading("tipo_producto", text='Tipo de Producto')

tree.insert('', END, 'lala', values=(numero_serie,expiracion ,tipo_producto ), text='FILA1')
tree.insert('', END, 'lele', values=('Cuatro', 'Cinco', 'Seis'), text='FILA2')


tree.grid(column=0, row=0)

root.mainloop()





