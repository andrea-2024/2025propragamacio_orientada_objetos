''' HERENCIA , es una caracteristica importanteconsiste en la posibilidad de crear
una nueva clase a partir de esta, o de las ya existentes
'''

print("============")
print("TECNICAS DE PROGRAMACION")
print("============")
class Calculadora:
    def __init__(self,numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingresardato(self):
        self.datos = [int(input("ingrese datos:" + str(i +1)+'=')) for i in range(self.n)]

class operaciones_basicas(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,2)

    def suma(self):
         a,b, = self.datos
         sum = a + b
         print('el resultado es:', sum)

    def restar(self):
         a,b, = self.datos
         rest = a - b
         print('el resultado es:', rest)

    def multiplicacion(self):
        a,b, = self.datos
        mul = a * b
        print('el resultado es:', mul)

    def division(self):
        a,b, = self.datos
        div = a / b
        print('el resultado es:', div)

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self,1)
    def cuadrada(self):
        import math
        a,= self.datos
        print('el resultado es :', math.sqrt(a))

resultado= operaciones_basicas()
print(resultado.ingresardato())
print(resultado.multiplicacion())


resultado = raiz()
print(resultado.ingresardato())
print(resultado.cuadrada())