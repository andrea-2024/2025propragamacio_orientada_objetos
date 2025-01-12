'''Programación Tradicional:
-Implementa una solución utilizando estructuras de funciones.
-Define funciones para la entrada de datos diarios (temperaturas)
 y el cálculo del promedio semanal.
-Organiza el código de manera lógica y funcional utilizando la programación tradiciona'''

# Definimos los datos mediante la creacion de una
#variable

ciudades  = [ "QUITO", "RIOBAMBA","GUAYAQUIL","IMBABURA"]
# Creamos otra variable donde almacenaremos las temperaturas
temp_ciudades = [[25,30,40,38,25,39,28], #QUITO
                 [25,26,28,29,35,25,23], #RIOBAMBA
                 [36,36,38,39,38,40,42], #GUAYAQUIL
                 [28,25,29,29,28,28,30]] #IMBABURA

#CREAMOS UNA VARIABLE DONDE SE ALMACENE EL PROMEDIO  POR SEMANA Y SE DIVIDA PARA 7
#POR CADA SEMANA

promedios = {
    ciudad: sum(temp_ciudades[i][:7])/7 for i, ciudad in enumerate(ciudades ) }

#IMPRIMIMOS EL RESULTADO EN PANTALLA

print(promedios)