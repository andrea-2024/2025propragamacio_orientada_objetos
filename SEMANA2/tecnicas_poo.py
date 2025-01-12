''' TECNICAS DE PROGRAMACION'''

print("============")
print("TECNICAS DE POO")
print("============")

'''Creamos la clase base , con su respectivo
constructor, atributos y método'''
    
class Miembros_familia():
    def __init__(self, nombre, edad ):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad} años.")

# Luego creamos la primera clase derivada o hija

class padre (Miembros_familia):
    def __init__(self,nombre,edad,apellido):
# Llamamos al constructor de la clase base Miembros_familia
        super().__init__(nombre,edad)
        self.apellido = apellido

    def presentarse(self):
#MOdificamos la funcion para incluir el apellido
        super().presentarse() #llamamos al metodo de la clase base
        print(f"Mi apellido es  {self.apellido}.")

# Luego creamos la segunda clase derivada o hija

class madre (Miembros_familia):
    def __init__(self,nombre,edad,profesion):
# Llamamos al constructor de la clase base Miembros_familia
        super().__init__(nombre,edad)
        self.profesion = profesion

    def presentarse(self):
#MOdificamos la funcion para incluir la profesion
        super().presentarse() #llamamos al metodo de la clase base
        print(f"Mi profesion es  {self.profesion}.")

# Creamos las varibles

padre = padre("Reinaldo", 67, "Daqui")
madre = madre("Maria Jose", 57, "Comerciante")

#Llamamos al metodo de presentacion

padre.presentarse()
madre.presentarse()