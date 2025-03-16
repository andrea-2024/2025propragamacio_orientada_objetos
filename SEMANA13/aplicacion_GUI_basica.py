#Importación de la biblioteca tkinter para creacion de interfaces gráficas

import tkinter as tk
from itertools import product
from shutil import which
from tkinter import messagebox #Con este comando mostramos alertas y ensajes emergentes

def agregar_producto():
    producto = entrada_producto.get() # Se obtiene nombre del producto
    precio = entrada_precio.get() #Obtener precio del producto
    if producto and precio: # Verificacion de ambos parametros
        lista_productos.insert(tk.END,f"{producto}- ${precio}") # Se agrega un producto a la lista
        entrada_producto.delete(0, tk.END) #Limpieza del campo de entrada del producto
        entrada_precio.delete(0, tk.END) # Limpieza del campo de precio

   #Aviso en caso de que algun campo este vacio
    else:
        messagebox.showwarning("Advertencia","Ingrese nombre y precio del producto")

#Función de limpieza de productos

def limpiar_lista():
    lista_productos.delete(0,tk.END) # Se eliminan todos los productos de la lista

#Funcion eliminamos el producto seleccionado

def eliminar_seleccion():
    seleccion = lista_productos.curselection() #Obtencion del indice del elemento seleccionado
    if seleccion:
        lista_productos.delete(seleccion)
        guardar_productos()
    else:
        messagebox.showwarning("Advertencia", "Seleccion de un producto para eliminar") #Muestra
        #si no hay un producto

#FUNCION PARA GUARDAR PRODUCTOS
def guardar_productos():
    with open("productos.txt", "w") as file:
        for item in lista_productos.get(0,tk.END):
            file.write(item + "\n")

#FUNCION CARGAR PRODUCTO

def cargar_productos():
    try:
        with open("productos.txt", "r") as file:
            for line in file:
                lista_productos.insert(tk.END,line.strip())
    except FileNotFoundError:
        pass


def ver_productos_guardados():
    try:
        with open("productos.txt", "r") as file:
            productos = file.readlines()
            if productos:
                productos_texto = "\n".join(productos)
                messagebox.showinfo("Productos Guardados", productos_texto)
            else:
                messagebox.showinfo("Productos Guardados", "No hay productos guardados.")
    except FileNotFoundError:
        messagebox.showwarning("Error", "No se encontró el archivo de productos.")

#Creacion de una ventana principal

ventana = tk.Tk() # Ventana principal
ventana.title("Viveres Camikasi - Gestion de invetario") # Nombre del establecimiento
ventana.geometry("500x400")   #tamaño de ventana en pixeles

#Etiquetas y campos de entrada
etiqueta_producto = tk.Label(ventana, text ="Nombre del producto") # Se crear etiqueta
etiqueta_producto.pack(pady = 5) # Se agrega etiqueta con espacio de separacion
entrada_producto = tk.Entry(ventana, width = 40) #  Se crea un campo de entrada
entrada_producto.pack(pady = 5) # Agrega campo a la ventana

#Precio del producto , etiqueta y campo de entrada

etiqueta_precio = tk.Label(ventana,text = "Precio ($):") # Creacion de la etiqueta precio
etiqueta_precio.pack(pady = 5) # Se agrega etiqueta con espacio
entrada_precio = tk.Entry(ventana, width=40) # Campo de entreda para el espacio
entrada_precio.pack(pady = 5) # agrega campo de entrada a la ventana

#BOTON PARA AGREGAR UN PRODUCTO
boton_agregar = tk.Button(ventana, text = "Agregar producto",
command = agregar_producto) # Creamos el boton
boton_agregar.pack( pady = 5) # Agregamos espacio al boton

#BARRA DE DESPLAZAMIENTO DE LA LISTA DE PRODUCTOS
enmarcado_lista = tk.Frame(ventana) # CReacion del marco para la lista
enmarcado_lista.pack(pady = 5) # Agrega marco
# Creacion de la lista aqui se muestran los productos

lista_productos = tk.Listbox(enmarcado_lista, width = 60 , height=10) # en esta lista se muestran los productos

#CREAR BARRA DE DESPLAZAMIENTO
barra_desplazamiento = tk.Scrollbar(enmarcado_lista) #Creamos barra de desplazamiento
barra_desplazamiento.pack(side=tk.RIGHT, fill = tk.Y) #Barra de desplazamiento directo

lista_productos.config(yscrollcommand=barra_desplazamiento.set)
barra_desplazamiento.config(command=lista_productos.yview)

#BOTON DE LIMPIEZA Y ELIMINACION DE PRODUCTOS
boton_limpiar_lista = tk.Button(ventana, text="Lipiar lista ", command= limpiar_lista)
boton_limpiar_lista.pack(pady = 5) #agrega boton de espacio de separacion

boton_eliminar_seleccion = tk.Button(ventana, text="Eliminar Producto", command= eliminar_seleccion)#Creacion del boton
boton_eliminar_seleccion.pack(pady = 5)#Agrega al boton espacio de separacion

#Cargar productos
tk.Button(ventana, text="Ver productos guardados", command=ver_productos_guardados).pack(pady=5)
cargar_productos()

#EJECUCION DEL PROGRAMA
ventana.mainloop()  # Ceste boton permite la interaccion con el usuario













