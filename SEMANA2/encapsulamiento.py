'''La encapsulación permite ocultar los detalles internos del objeto
utilizando modificadores de acceso'''

print("============")
print("ENCAPSULACION")
print("============")

#Creamos una clase
class Cliente :
    def __init__(self): # Creamos el constructor como una clase normal
        self.__codigo = 6789  #Encapsulamos una variable a la cual no podremos acceder

    def __cuenta(self):
        print('Cuenta de procesamiento')

    def getcodigo(self):  #para recuperar este valor debemos traer otro método
        return self.__codigo

persona = Cliente()
#Para poder ejecutar este valor y tenerlo como respuesta necesito
#objeto._nombreclase__nombreatributo

print(persona._Cliente__codigo)

persona._Cliente__cuenta()