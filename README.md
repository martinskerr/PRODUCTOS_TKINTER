# PRODUCTOS_TKINTER
Este código es una aplicación de escritorio desarrollada con Python y la librería gráfica Tkinter. La aplicación tiene como objetivo permitir al usuario ingresar información de productos en una base de datos y luego mostrar, eliminar y exportar esta información en una tabla.

El código utiliza la conexión a una base de datos SQLite, que se importa directamente desde un archivo "dao.py" en el directorio.

La función "main()" es la función principal que contiene todas las instrucciones para crear la interfaz gráfica de usuario y asociar las funciones a los botones y elementos de la interfaz.

El código tiene una función "renderProductos()" que se encarga de mostrar los productos en una tabla utilizando el widget TreeView de Tkinter. También tiene una función "generador_excel()" que permite exportar los productos en un archivo .csv.

La función "insertar(productos)" permite insertar un nuevo producto en la tabla de la base de datos. La función "eliminar_producto()" permite eliminar un producto seleccionado de la tabla y la función "nuevo_producto()" permite al usuario crear un nuevo producto mediante una ventana emergente.
