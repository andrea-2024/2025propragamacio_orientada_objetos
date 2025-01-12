# Clase para representar un producto en la tienda
class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo  # Código único del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio unitario
        self.stock = stock  # Cantidad disponible

    def reducir_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}.")
        else:
            print(f"No hay suficiente stock de {self.nombre}.")

    def aumentar_stock(self, cantidad):
        self.stock += cantidad
        print(f"Se han añadido {cantidad} unidades de {self.nombre} al inventario.")


# Clase para representar al vendedor
class Vendedor:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del vendedor
        self.ventas_totales = 0  # Total de ventas realizadas

    def realizar_venta(self, producto, cantidad):
        if cantidad <= producto.stock:
            total = cantidad * producto.precio
            producto.reducir_stock(cantidad)
            self.ventas_totales += total
            print(f"{self.nombre} ha realizado una venta por ${total:.2f}.")
        else:
            print(f"Venta fallida: no hay suficiente stock de {producto.nombre}.")

    def mostrar_ventas(self):
        print(f"Ventas totales realizadas por {self.nombre}: ${self.ventas_totales:.2f}")


# Clase para gestionar la tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la tienda
        self.productos = []  # Lista de productos disponibles

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado a la tienda.")

    def mostrar_productos(self):
        print(f"Inventario de {self.nombre}:")
        for producto in self.productos:
            print(f" - {producto.nombre}: ${producto.precio:.2f} (Stock: {producto.stock})")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    # Crear una tienda y un vendedor
    tienda = Tienda("Tienda de Electrónica")
    vendedor = Vendedor("Carlos")

    # Agregar productos a la tienda
    producto1 = Producto(101, "Auriculares", 25.50, 10)
    producto2 = Producto(102, "Mouse Inalámbrico", 15.00, 5)
    producto3 = Producto(103, "Teclado Mecánico", 45.99, 2)

    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)
    tienda.agregar_producto(producto3)

    # Mostrar productos disponibles
    tienda.mostrar_productos()

    # Realizar ventas
    vendedor.realizar_venta(producto1, 2)  # Vender 2 auriculares
    vendedor.realizar_venta(producto3, 1)  # Vender 1 teclado

    # Mostrar inventario actualizado
    tienda.mostrar_productos()

    # Mostrar ventas totales del vendedor
    vendedor.mostrar_ventas()
