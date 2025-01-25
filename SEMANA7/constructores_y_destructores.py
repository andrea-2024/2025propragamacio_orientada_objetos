# Esta vez trabajaremos en un codigo que simula el inventario de una tienda
# Crearemos la clase llamada producto

class Articulo:
    def __init__(self,codigo,nombre,precio,unidades): # constructor que inicializa el producto con sus atributos
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.unidades = unidades
        print(f"Articulo creado:{self.nombre}, (Codigo{self.codigo})")
# Destructor que se invoca cuando se elimina un producto

    def __del__(self):
        print(f"Eliminando articulo:{self.nombre},Codigo:{self.codigo}")

#Creamos la clase mi tienda

class Tienda:

    def __init__(self,nombre_tienda):  #constructor que inicializa tinda
       self.nombre_tienda = nombre_tienda
       self.inventario = {} # Diccionario, almacena productos por su codigo
       print(f"Tienda:{self.nombre_tienda}' Creada.")

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario de la tienda.
        """
        if producto.codigo in self.inventario:
            self.inventario[producto.codigo].unidades += producto.unidades
            print(
                f"Producto existente actualizado: {producto.nombre}, nueva cantidad: {self.inventario[producto.codigo].unidades}")
        else:
            self.inventario[producto.codigo] = producto
            print(f"Producto agregado al inventario: {producto.nombre}")

#Elimina por su codigo un producto del inventario
    def eliminar_producto (self,codigo):
        if codigo in self.inventario:
            producto = self.inventario.pop(codigo)
            print(f"Producto eliminado del inventario: {producto.nombre}")

        else:
            print(f"Error producto con codigo{codigo}, no encontrado")
#Mostrar los productos del inventario

    def mostrar_inventario(self):
        print("Inventario del local")
        if self.inventario:
            for producto in self.inventario.values():
                print(f"Código: {producto.codigo}, Nombre: {producto.nombre}, Precio: ${producto.precio}, Cantidad: {producto.unidades}")

            else:
                print("El inventario se encuentra vacio")

# este destructor invoca a cerrar la tienda

    def __del__(self):
        print(f"Cerrar tienda: {self.nombre_tienda}'.....")

# Programa principal
if __name__  == "__main__":
    print("Crear tienda")
    tienda = Tienda("Viveres Camikasi")

    print(tienda.agregar_producto)
    articulo1 = Articulo(222, "@ Arroba arroz  ", 13.25, 3 )
    articulo2 = Articulo(122,"Caja aceite", 10.75, 5 )
    articulo3 = Articulo(777, "Detergente", 1.25, 10)

    tienda.agregar_producto(articulo1)
    tienda.agregar_producto(articulo2)
    tienda.agregar_producto(articulo3)

    print("Mostrando inventario")
    tienda.mostrar_inventario()

    print("Eliminando producto")
    tienda.eliminar_producto(777)

    print("INVENTARIO ACTUALIZADO")
    tienda.mostrar_inventario()

    print("Finalizar programa") #Los destructores se invocan de manera automatica eb cuanto
                                #cerramos el programa













