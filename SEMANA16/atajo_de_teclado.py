#IMPORTAR BIBLIOTECA TKINTER

import tkinter as tk
from tkinter import messagebox, Listbox


#CREACION DE VENTANA PRINCIPAL
root = tk.Tk() #Creacion de ventana principal
root.title("Lista de tareas") #Titulo de la ventana
root.geometry("380x380") #Tamaño de la ventana

def add_tarea(event=None):
    tarea = entry_tarea.get().strip()
    if tarea:
        listbox_tareas.insert(tk.END, tarea) #Agrega la tarea a la lista
        entry_tarea.delete(0,tk.END) #Limpia el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacia")

#Marcar una tarea completa
def mark_completed():
    try:
        selected_index = listbox_tareas.curselection()[0]
        tarea = listbox_tareas.get(selected_index)
        if not tarea.startswith("*"):
            listbox_tareas.delete(selected_index)
            listbox_tareas.insert(selected_index,f"{tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciones una tarea y marquela")


#Eliminar una tarea de la lista
def deleted_task():
    try:
        selected_index = listbox_tareas.curselection()[0]
        listbox_tareas.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia","Seleccione una tarea para eliminar")

#CREACION DE CAMPOS DE ENTRADA
entry_tarea = tk.Entry(root, width=40) # En este campo de etrada el usuario puede escribir
entry_tarea.pack(pady=10)  # Existen 10 pixeles por ecima y debajo de la ventana
entry_tarea.bind("<Return>", add_tarea) #El ususario con esta tecla puede agragar una tarea

#LISTAS DE TAREAS

listbox_tareas  = tk.Listbox(root,width=50,height=15)
listbox_tareas.pack(pady=10)

#BOTONES PARA MANEJAR TAREAS
frame_buttons = tk.Frame(root)
frame_buttons.pack()

#   BOTON PARA AÑADIR TAREA
btn_add = tk.Button(frame_buttons, text = "Añadir tarea",command = add_tarea)
btn_add.pack(side=tk.LEFT, pady=5)


#COMPLETAR TAREA
btn_complete = tk.Button(frame_buttons, text="Marcar tarea como completada", command=mark_completed)
btn_complete.pack(side=tk.LEFT,pady=5)

#ELIMINAR TAREA
btn_delete = tk.Button(frame_buttons, text="Eliminar", command=deleted_task)
btn_delete.pack(side=tk.LEFT, padx=5)


root.mainloop()
