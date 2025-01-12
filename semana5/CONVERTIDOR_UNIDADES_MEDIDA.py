class Convertidor:
    def __init__(self):
        pass # Es un constructor vacio por lo tanto no necesita inicializar ningun atributo
    # Metodo para realizar la convercion

    def convertir(self, opcion, cantidad):

        if opcion ==1:
             # Convertir metros a kilometros
             return f"{cantidad} metros son {self.metros_a_kilometros(cantidad):.2f} kilometros"
        elif opcion == 2:
        # Convertir gramos a Kilogramos
            return f"{cantidad} gramos son {self.gramos_a_kilogramos(cantidad):.2f} kilogramos"
        elif opcion == 3:
            #convertidor celcius a farenhei
            return f"{cantidad} °C son {self.celsius_a_fahrenheit(cantidad):.2f} °F"
        else:
            return "Opcion invalida"
# Convertidos de metros a kilometros

    def metros_a_kilometros(self,cantidad):
        return cantidad/1000

    #Convertidos gramos a kilogramos

    def gramos_a_kilogramos (self,cantidad):
        return cantidad/1000

    #convertidor grados celcius a farenhei

    def celcius_a_fahrenheit(self,cantidad):
        return (cantidad * 9 / 5) + 32

def main():
    # Mostrar opciones disponibles al usuario
    print("1. Longitud (metros a kilómetros)")
    print("2. Peso (gramos a kilogramos)")
    print("3. Temperatura (Celsius a Fahrenheit)")

    # Solicitar al usuario que elija una opción
    opcion = int(input("Elige una opción: "))

    # Solicitar al usuario la cantidad a convertir
    cantidad = float(input("Introduce la cantidad: "))

#ejecutar
main()