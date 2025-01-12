#DEMOSTRAR Y APLICAR LA COMPRENSION ORIENTADA A OBJETOS
#Ejemplos mundo real
'''Para la realizacion del presente codigo tomaremos como referencia
el negocio al cual me dedico que es la venta de articulos de primera
necesidad en una tienda'''

#Clase representar un producto de la tienda
class Producto:
    def __init__(self, codigo,nombre,precio,inventario):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.inventario = inventario

    def reducir_inventario(self,cantidad):
        if cantidad <=self.inventario:
            self.inventario -= cantidad
            print(f"Se ha vendido ¨{cantidad} unidades de ¨{self.nombre}")

        else:
            print(f"No hay stock suficiente en {self.nombre}")

    def incrementar_inventario(self,cantidad):
        self.inventario += cantidad
        print(f"Se ha aumentado {cantidad}, unidades de {self.nombre}, al inventario")
# Creamos la clase vendedor
class Vendedor:
    def __init__(self, nombre):
        self.nombre = nombre  #Nombre del vendedor
        self.ventas_totales = 0  #Total de ventas

    def realizar_venta(self,producto,cantidad):
        if cantidad <= producto.inventario:
            total = cantidad * producto.precio
            producto.reducir_inventario(cantidad)
            self.ventas_totales +=total
            print(f"´{self.nombre} ha realizado una venta por {total:.2f}.")

#Clase gestion de la tienda

class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la tienda o local
        self.productos = []   #lista de productos disponibles

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda.")

    def mostrar_producto (self):
        print(f"Inventario de {self.nombre}")
        for producto in self.productos:
            print(f" - {producto.nombre}: ${producto.precio:.2f} (Stock: {producto.inventario})")

# Uso del sistema

if __name__ == "__main__":

#Creaciòn de tienda y vendedor
    tienda = Tienda("Tienda de Viveres")
    vendedor = Vendedor("Andrea Daqui")

#Agregar producto a la tienda

    producto1 = Producto(125,"qq arroz", 48.50 , 3)
    producto2 = Producto(105, "aceite", 2.05, 15)
    producto3 = Producto(109, "Cola", 3.5 , 25)
    producto4 = Producto(222, "atun", 1.5 , 30)
    producto5 = Producto(206, "cubeta de huevos ", 3.75, 10)

    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)
    tienda.agregar_producto(producto3)
    tienda.agregar_producto(producto4)
    tienda.agregar_producto(producto5)

#Mostrar productos disponibles
    tienda.mostrar_producto()

# Realizar venta
    vendedor.realizar_venta( producto4,3)
    vendedor.realizar_venta( producto5,3)
    vendedor.realizar_venta( producto3,6)
    vendedor.realizar_venta( producto2,2)

# Mostrar inventario actual

    tienda.mostrar_producto()














