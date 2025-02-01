#Creamos la clase que representa un producto en la tienda Camikasi

class Producto:
    def __init__(self, codigo, nombre, cantidad,costo):
        self.codigo = codigo   #identificador del producto
        self.nombre = nombre   #nombre del producto
        self.cantidad = cantidad  #unidades
        self.costo = costo

    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_costo(self):
        return self.costo

    # Modifica la cantidad del producto
    def set_cantidad(self,cantidad):
        self.cantidad = cantidad

    #Modifica el valor del producto
    def set_costo(self,costo):
        self.costo = costo

#Creamos la clase que gestiona el inventario de la tienda camikasi

class InventarioCamikasi():
    def __init__(self):
        self.productos = []  #Lista donde se almacenan los productos

    def añadir_producto(self, producto):

        # Verifica si el ID del producto ya existe en el inventario
        if any(p.get_codigo() == producto.get_codigo() for p in self.productos):
            print("Error: El codigo del producto ya existe.")

        else:
             self.productos.append(producto)
             print(f"Producto {producto.get_nombre()} añadido a Camikasi.")

    def buscar_producto_por_codigo(self, codigo):
        """Busca un producto en el inventario por su código y lo devuelve si existe."""
        for producto in self.productos:
            if producto.get_codigo() == codigo:
                return producto
        return None


    def eliminar_producto(self,codigo):
        #buscar un producto y eliminar el codigo
        producto = self.buscar_producto_por_codigo(codigo)

        if producto:
            self.productos.remove(producto)
            print(f"Producto {producto.get_nombre()} Eliminado de inventario Camikasi.")

        else:
            print("Producto no encontrado")

# Actualizar los productos existentes
    def actualizar_productos(self, codigo, cantidad = None, costo = None):
        producto = self.buscar_producto_por_codigo(codigo)
        if  producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if costo is not None:
                producto.set_costo(costo)
            print(f"Producto {producto.get_nombre()} Actualizar inventario de Camikasi")

        else:
            print("Producto no encontrado")


#Muestra los productos del inventario

    def mostrar_inventario(self):
        # Muestra todos los productos en el inventario
        if not self.productos:
            print("El inventario de Camikasi está vacío.")
        else:
            for producto in self.productos:
                print(
                    f"ID: {producto.get_codigo()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Precio: {producto.get_costo()}")

# Mostrar menù para gestionar el inventario

    def buscar_producto_por_nombre(self,nombre):
        return[p for p in self.productos if p.get_nombre(). lower() == nombre.lower()]


def mostrar_menu():
    print("\n--- Menú de Inventario de Camikasi ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")
    return input("Seleccione una opción: ")

#Funcion que ejecuta el programa
def ejecutar_programa():
    inventario = InventarioCamikasi()

    while True:
        opcion = mostrar_menu()


#añadir producto
        if opcion == '1':
            #añadir un producto
            codigo = int(input(" Ingrese el còdigo del producto"))
            nombre = input("Ingrese el nombre del producto")
            cantidad = int(input("Ingrese la cantidad"))
            costo = int(input("Ingrese el valor "))
            producto = Producto(codigo,nombre,cantidad,costo)
            inventario.añadir_producto(producto)
#eliminar producto

        elif opcion == '2':
            codigo = int(input("Ingrese Codigo del producto a eliminar: "))
            inventario.eliminar_producto(codigo)

        elif opcion == '3':
            # Actualizar producto
            codigo = int(input("Ingrese el codigo del producto a actualizar: "))
            cantidad = input("Ingrese nueva cantidad (deje en blanco si no desea cambiar): ")
            costo= input("Ingrese nuevo precio (deje en blanco si no desea cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            costo = float(costo) if costo else None

            inventario.actualizar_productos(codigo, cantidad, costo)

        elif opcion == '4':
            # Buscar producto por nombre
            def buscar_producto_por_nombre(self, nombre):
                return [p for p in self.productos if p.get_nombre().lower() == nombre.lower()]

            productos_encontrados = buscar_producto_por_nombre(nombre)
            if productos_encontrados:

                for producto in productos_encontrados:
                    print(
                        f"Codigo: {producto.get_codigo()}, Nombre: {producto.get_nombre()}, Cantidad: {producto.get_cantidad()}, Costo: {producto.get_costo()}")
            else:
                print("No se encontraron productos en Camikasi.")

        elif opcion == '5':
            # Mostrar todos los productos
            inventario.mostrar_inventario()

        elif opcion == '6':
            # Salir del programa
            print("Saliendo del sistema de inventario de Camikasi...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_programa()

