'''DISEÑA UNA SOLUCION UTILIZANDO EL PARADIGMA DEL POO
CREA UNA CLASE QUE REPRESENTE LA INFORMACION DIARIA DEL CLIMA
UTILIZA METODOS DE CLASE PARA INGRESAR DATOS Y CALCULAR EL PROMEDIO SEMANAL
APLICAR CONCEPTOS COMO ENCAPSULAMIENTO, HERENCIA O POLIMORFISMO'''

#EN PRIMERA INSTANCIA CREAMOS UNA CLASE QUE SERA LA CLASE PADRE

class Clima_ciudades:
    # DEFINIMOS EL CONTRUCTOR METODO Y ATRIBUTOS

    def __init__(self,ciudad):
        self.ciudad = ciudad  #atributo `para las ciudades
        self.temperaturas = []  #atributo para las temperaturas vacia para almacenar

 # metodo para agregar a la lista una temperatura diaria
    def ingresar_temperatura (self, temperatura):  #Se registra una temperatura por dia
        if len(self.temperaturas)<7:               #Maximo 7
            self.temperaturas.append(temperatura)
        else:
            print("se registran las temperaturas para los 7 dias")

#creamos un metodo donde calcularemos el promedio
#de la temperatura semanal
    def calcular_promedio(self):
        if len(self.temperaturas) ==0: #si no hubiera temperaturas que se registren retorna 0
            return 0                   #de esta manera evitar errores
        return sum(self.temperaturas)/len(self.temperaturas)

#mostramos la informacion del promedio semanal de la ciudad muestra informaciòn
    def mostrar_informacion(self):
        promedio = self.calcular_promedio()
        print(f"Ciudad: {self.ciudad }")
        print(f"Temperaturas registradas ´{self.temperaturas}")
        print(f"promedio semanal: {promedio:.2f}º c \n")

#creamos los objetos que vamos a utilizar

ciudades =["CIUDAD DE QUITO", "CIUDAD DE RIOBAMBA","CIUDAD DE IMBABURA","CIUDAD DE GUATAQUIL"]
objetos_clima=[]

#para cada ciudad creamos objetos de clima diario

for ciudad in ciudades:
    objeto =Clima_ciudades(ciudad)
    objetos_clima.append(objeto)

#para cada ciudad ingresamos las temperaturas diarias
#mediante la creacion de una variable que contenga estos datos

datos_temperatura=[
    [25,25,39,34,36,35,36],
    [35,36,34,34,35,38,36],
    [35,26,27,29,25,26,65],
    [26,26,38,35,36,34,36]]

#Mediante el bucle for recorremos los objetos de objetos clima y las
#temperaturas de las ciudades

for i, objeto in enumerate(objetos_clima):
    for temp in datos_temperatura[i]:
       objeto.ingresar_temperatura(temp)
#Recorremos la lista objetos_clima y llamamos al metodo mostrar informacion

for objeto in objetos_clima:
    objeto.mostrar_informacion()