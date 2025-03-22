#Importamos

import tkinter as tk

from tkinter import messagebox, Entry, Listbox


#Funcion de la aplicacion
def add_task(): #obtener texto y eliminar espacios en blanco
    task = entry.get().strip() #Verifica si el campo no està vacio
    if task:
        listbox.insert(tk.END,task) #Inserta tarea a la lista al final
        entry.delete(0,tk.END)#Limpia el texto despues de agregar la tarea
    else:
        messagebox.showwarning("Cacilla vacia", "Porfavor ingrese su tarea")#Si el campo esta vacio muestra adventencia

def marcar_completada():
    try:
        seleccione_index = listbox.curselection()[0] #Obtiene el indice  de la tarea seleccionada
        task = listbox.get(seleccione_index) #obtiene el texto de la tarea seleccionada
        listbox.delete(seleccione_index) #Elimina la tarea seleccionada
        listbox.insert(seleccione_index, f"{task}")
    except IndexError: #Insertar la tarea nuevamente
        #Muestra advertencia si no hay tarea seleccionada
        messagebox.showwarning("Seleccion no valida", "Marque la tarea como completada")


def borrar_tarea():
    try:
    #Se obtiene el indice de la tarea que se selecciona
        seleccione_index = listbox.curselection()[0]
    #Elimina la tarea sellecionada
        listbox.delete(seleccione_index)
    except IndexError:
    #Si no hay tarea muestra mensaje de advertencia
        messagebox.showwarning("Seleccion no vàlida", "Seleccione tarea")


def ingresar(evento):
    add_task()

#Creacion de la intefaz grafica
#Ventana principal
root = tk.Tk()  #Esta ventana es la base donde se agregan los elemento
root.title (" MI LISTA DE TAREAS")
#Campo de entrada
entry = tk.Entry(root,width=35) #Crea campo donde el usuario ingresa tareas con un ancho de 35 caracteres
entry.pack(pady = 10)#Empaqueta el campo con espacio de 10 pixeles por encima y por debajo
entry.bind("<Return>", ingresar) #Asocia la tecla ingresar on la funcion

#Añadir botones
#Crea el boton con el texto agregar tarea
agregar_boton = tk.Button(root, text="Añadir tarea", command=add_task)
agregar_boton.pack()

#Crea el boton con el texto marcar tarea completada
marcar_boton = tk.Button(root, text="Marcar tarea como completada", command=marcar_completada)
marcar_boton.pack()

#Crea el boton con el texto eliminar tarea
borrar_boton = tk.Button(root, text="Eliminar tarea", command=borrar_tarea)
borrar_boton.pack()

#Lista de tareas
listbox=tk.Listbox(root, width=50 , height=10) #Crea un widge de lista muestra tareas
listbox.pack(pady=10)#Empaqueta la lista en la ventana

#Ejecucion del programa
root.mainloop() #Inicia el bucle , mantiene la vemtana abierta y espera que el usuario interactue






