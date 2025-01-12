#Clase venta de articulos de papeleria
#CReamos una clase padre
class Articulos:
    def __init__(self,detalle,costo):
#encpsulacion de productos protegidos
        self._detalle = detalle
        self._costo = costo

    def mostrar_detalles(self):
        #Metodo para mostrar el detalle del articulo
        return f"Articulo{self._detalle}, precio ${self._costo:2f}"

    def aplicar_descuento_general(self,porcentaje):
        #Con este metodo aplicamos el descuento
        self._costo -= self._costo * (porcentaje/100)
        return f"Precio actual es {self._detalle}, ${self._costo}"

#Creamos una clase hija o clase derivada
class Cuaderno(Articulos):
    def __init__(self, detalle,costo,caracteristicas,proveedor):
        super().__init__(detalle,costo)
        self.caracteristicas = caracteristicas #Atributo especifico de la clase cuaderno
        self.proveedor = proveedor



    def mostrar_detalles(self):
        return f" Cuaderno{self._detalle},  Caracteristica{self.caracteristicas},  Proveedor{self.proveedor},valor, ${self._costo:.2f}"

#ahora crearemos otra clase derivada denominada lapices de colores

class Lapices_de_colores(Articulos):
    def __init__(self,detalle,costo,cantidad,marca):
        super().__init__(detalle,costo)
        self.cantidad = cantidad  # Atributo especifico de la clase lapices de colores
        self.marca = marca
# sobre escritura del metodo mostrar detalle
    def mostrar_detalles(self):
        return (f"Lapices de colores: {self._detalle}, Unidades : {self.cantidad}, Marca: {self.marca}, "
                f"Costo: ${self._costo:.2f}")

#CReacion de la clase tienda para gestionar los productos

class Tienda:
    def __init__(self):
        self.productos = [] #  Lista para almacenar los productos

    # Metodo para agregar productos a la tienda

    def agregar_producto(self, producto):
        """Método para agregar productos a la librería"""
        self.productos.append(producto)
        print(f"{producto._detalle} agregado al inventario.")

    # Con este metodo mostramos todos los productos del inventario
    def mostrar_inventario(self):
        print("\nInventario de la Librería:")
        for producto in self.productos:
            print(producto.mostrar_detalles())
# Con este metodo aplicamos el producto a los productos

    def aplicar_descuento_general(self, porcentaje):
        print(f"\nAplicando {porcentaje}% de descuento a todos los productos:")
        for producto in self.productos:
            print(producto.aplicar_descuento_general(porcentaje))
 #Código principal
if __name__ == "__main__":
    # Creación de objetos
    Cuaderno1 = Cuaderno("Cuaderno academico", 1.50, "Cuaderno de cuadros ", "Norma")
    Cuaderno2 = Cuaderno("Cuaderno academico", 1.50, "cuaderno de lineas ", "Norma")
    Lapices_de_colores1 = Lapices_de_colores("Caja de colores ", 1.90, "12 unidades", "norma")
    Lapices_de_colores2 = Lapices_de_colores("Caja de colores ", 1.75, "12 unidades", "Bester")

    # Creación de la librería
    mi_tienda = Tienda()

    # Agregamos los diferentes productos

    mi_tienda.agregar_producto(Cuaderno1)
    mi_tienda.agregar_producto(Cuaderno2)
    mi_tienda.agregar_producto(Lapices_de_colores1)
    mi_tienda.agregar_producto(Lapices_de_colores2)

#  Agregamos el descuento general a todos los productos

    mi_tienda.aplicar_descuento_general(20)

# Mostrar inventario actualizado
    mi_tienda.mostrar_inventario()



