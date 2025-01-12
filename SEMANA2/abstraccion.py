'''una clase abstracta evita que un usario
cree una clase abstracta'''
#Este ejemplo muestra un sistema que controlará electrodomésticos

#Definimos una clase abstracta

from abc import  ABC,abstractmethod
# Creamos la clase base
class Electrodomestico(ABC):
    def enceder(self):      # Definimos el metodo bastracto 1
        pass

    def apagar (self):      #Definimos el metodo abstracto 2
        pass

#Creacion de clases concretas

class lavadora(Electrodomestico):
    def enceder(self):
        print('La lavadora está encendida')


class Horno (Electrodomestico):
    def apagar(self):
        print("El Horno està apagado")
#cada una de estas clases define especificamente un comportamiento

#USOS DE LAS CLASES
def controlar_electrodomestico(electrodomestico,accion):
    if accion == "encender":
        electrodomestico.enceder()

    elif accion == "apagar":
        electrodomestico.apagar()



#Creamos los objetos electrodomesticos

lavadora = lavadora()
Horno = Horno()

controlar_electrodomestico(Horno,"apagar")
controlar_electrodomestico(lavadora,"encende")