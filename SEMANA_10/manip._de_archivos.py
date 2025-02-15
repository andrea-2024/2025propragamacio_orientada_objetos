import json
import os

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """Inicializa la clase y carga el inventario desde un archivo."""
        self.archivo = archivo
        self.productos = self.cargar()

    def cargar(self):
        """Carga el inventario desde un archivo JSON si existe."""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        return {}

    def guardar(self):
        """Guarda el inventario en un archivo JSON."""
        with open(self.archivo, "w") as f:
            json.dump(self.productos, f, indent=4)

    def agregar(self, nombre, cantidad, precio):
        """Agrega un nuevo producto al inventario."""
        self.productos[nombre] = {"cantidad": cantidad, "precio": precio}
        self.guardar()

    def actualizar(self, nombre, cantidad=None, precio=None):
        """Actualiza la cantidad o el precio de un producto existente."""
        if nombre in self.productos:
            if cantidad is not None:
                self.productos[nombre]["cantidad"] = cantidad
            if precio is not None:
                self.productos[nombre]["precio"] = precio
            self.guardar()

    def eliminar(self, nombre):
        """Elimina un producto del inventario."""
        if nombre in self.productos:
            del self.productos[nombre]
            self.guardar()

    def mostrar(self):
        """Muestra el inventario en formato JSON legible."""
        print(json.dumps(self.productos, indent=4))

def ejecutar_opcion(opcion, tienda):
    """Ejecuta la opción seleccionada por el usuario."""
    if opcion == "1":
        nombre = input("Nombre: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        tienda.agregar(nombre, cantidad, precio)
    elif opcion == "2":
        nombre = input("Nombre: ")
        cantidad = input("Cantidad (dejar en blanco si no cambia): ") or None
        precio = input("Precio (dejar en blanco si no cambia): ") or None
        tienda.actualizar(nombre, int(cantidad) if cantidad else None, float(precio) if precio else None)
    elif opcion == "3":
        nombre = input("Nombre: ")
        tienda.eliminar(nombre)
    elif opcion == "4":
        tienda.mostrar()
    else:
        print("Opción no válida")

if __name__ == "__main__":
    tienda = Inventario()
    while (op := input("1. Agregar 2. Actualizar 3. Eliminar 4. Mostrar 5. Salir: ")) != "5":
        ejecutar_opcion(op, tienda)
