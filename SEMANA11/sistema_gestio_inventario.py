#Construccion de un programa que gestione el archivo de invenventario
# Creacion de la clase producto

import  json

class Producto:
    def __init__(self,codigo_producto, nombre,cantidad,precio):
        self.codigo_producto = codigo_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

        #Modifica la cantidad del producto
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

        # MOdifica el valor del producto
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

       #Convierte a un objeto en diccionario para guardarlo en un archivo JSON
    def to_dict(self):
        return{
        "codigo_producto":  self.codigo_producto,
        "nombre":  self.nombre,
        "cantidad":  self.cantidad,
        "precio":  self.precio

    }

    # Clase invetario
class Inventario:
    def __init__(self):
        self.productos ={}  #Diccionario donde se almacena los producto
        self.cargar_desde_archivo()  #Carga productos al inventario al iniciar

# Agrera un producto en caso de que este no exista en el invetario
    def agregar_producto(self,producto):

        if producto.codigo_producto in self.productos:
            print("El producto ya existe en el inventario")
        else:
            self.productos[producto.codigo_producto]=producto
            self.guardar_en_archivo()
            print("Producto guardado correctmente")

 #Elimina un producto del inventario por su codigo
    def eliminar_producto(self,codigo_producto):

        if codigo_producto in self.productos:
            del self.productos[codigo_producto]
            self.guardar_en_archivo()
            print("Producto eliminado")
        else:
            print("El producto no existe en el inventario")

#Permite que podamos modificar la cantidad o el precio de un producto
    def actualizar_producto(self,codigo_producto,cantidad = None, precio = None):
        if codigo_producto in self.productos:
            if cantidad is not None:
                self.productos[codigo_producto].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[codigo_producto].actualizar_precio(precio)
                self.guardar_en_archivo()
                print("producto actualizado correctamente ")
        else:
            print("El producto no existe en el invetario")

# Podemos buscar un producto por su nombre
    def buscar_producto(self,nombre):
        encontrados = [i for i in self.productos.values() if
        i.nombre.lower() == nombre.lower()]
        if encontrados:
            for i in encontrados:
                print(f"codigo: {i.codigo_producto},Nombre: {i.nombre}, cantidad:{i.cantidad}, precio: ${i.precio} ")

        else:
            print("Producto no encontrado")

#Muestra los productos disponible
    def mostrar_inventario(self):
        if self.productos:
            for i in self.productos.values():
                print(f"Codigo: {i.codigo_producto}, Nombre: {i.nombre}, Cantidad :{i.cantidad}, Precio: $ {i.precio} ")

        else:
            print("El inventario está vacio")
#Guarda en un archivo JSON
    def guardar_en_archivo(self):
        with open ( "inventario.json", "w") as archivo:
            json.dump({codigo: i.to_dict() for codigo, i in self.productos.items()},archivo)

#Cargar un archivo desde un archivo JSON
    def cargar_desde_archivo(self):
        try:
            with open("inventario.json","r") as archivo:
                datos = json.load(archivo)
                self.productos = {id: Producto(**i) for id, i in datos.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.productos = {}

    def menu(self):
        inventario = Inventario()
        while True:
            print("  ---- Gestion de inventario----")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Actualizar producto")
            print("4. Buscar producto")
            print("5. Mostrar inventario")
            print("6. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                id_producto = input("Ingrese codigo del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))
            elif opcion == "2":
                id_producto = input("Ingrese ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)
            elif opcion == "3":
                id_producto = input("Ingrese ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
                precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")
                inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None,
                                               float(precio) if precio else None)
            elif opcion == "4":
                nombre = input("Ingrese el nombre del producto a buscar: ")
                inventario.buscar_producto(nombre)
            elif opcion == "5":
                inventario.mostrar_inventario()
            elif opcion == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida, intente de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    inventario = Inventario()
    inventario.menu()



















































