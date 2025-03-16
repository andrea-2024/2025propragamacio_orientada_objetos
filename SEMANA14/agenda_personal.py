#Importamos desde la biblioteca tkinter
import  tkinter as tk
from tkinter import ttk, Frame

#DEFINIMOS LA FUNCION
def agregar_evento():
    fecha = entry_fecha.get() #Obtiene el campo de fecha ingresado
    descripcion = entry_descripcion.get() #Se obtiene el texto de descripcion

    if fecha and descripcion:
        tree.insert("","end", values = (fecha , descripcion)) #Agrega datos a la tabla
        entry_fecha.delete(0, tk.END) #Borra la fecha despues de agregar
        entry_descripcion.delete(0, tk.END) #Borra la descripcion despues de agregar

#Ventana principal
root = tk.Tk()  #Creacion de la ventana principal
root.title("Agenda personal") #Titulo de la ventana
root.geometry("500x400")

#Creacion y configuracion de tabla de eventos(TreeView)
columns = ("Fecha", "Descripcion") #Define las columnas de las tablas
tree = ttk.Treeview(root, columns = columns, show="headings") #Tabla sin columnas de indices
for col in columns:
    tree.heading(col, text=col) #Nombre de la columna
    tree.column(col, width=150)#Ancho de columna
tree.pack(pady=10) #Ubicamos la tabla en la ventana espacio de 10pixeles abajo y arriba

#Creacion de campos de entrada
frame_entrada = tk.Frame(root) #Marco frame para orgaizar los campos
frame_entrada.pack(pady=10) #Marco en la ventana

tk.Label(frame_entrada, text="Fecha:").grid(row=0,column=0) #Etiqueta de fecha
entry_fecha = tk.Entry(frame_entrada) #Campo entrada de fecha
entry_fecha.grid(row=0, column=1)

tk.Label(frame_entrada, text="Descripcion:").grid(row=1, column=0) #Etiqueta de descripcion
entry_descripcion = tk.Entry(frame_entrada) #Entrada de descripcion
entry_descripcion.grid(row=1, column=1)

#BOTON DE AGREGAR EVENTOS
btn_agregar = tk.Button(root, text="Agregar evento",command=agregar_evento)
btn_agregar.pack(pady=10)

root.mainloop()



