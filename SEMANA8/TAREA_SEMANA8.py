import os # IMPORTA EL MODULO E INTERACTUA CON EL SISTEMA
import subprocess  #iMPORTA EL MODULOY EJECUTA PROCESOS EXTERNOS

#funcion para listar los scrpts disponibles
def mostrar_codigo(script):
    #muestra el archivo espeificado de python
    try:
        with open(script, 'r') as archivo: # Se abre el archivo en modo lectura
            print(f"\n---Codigo de {script}---\n")
            print(archivo.read()) #Muestra el contenido del archivo
    except Exception as e: #Manejo de errores
        print(f"Error al abrir el acrchivo {e}")


def ejecutar_script(script):
    #Ejecuta el script de python especificado
    try:
        subprocess.run(['python', script], check=True)   #Ejecucion del script del nuevo proceso
    except Exception as e:    #muestra errores
        print(f"Error al ejecutar script: ´{e}")

def menu():
    #muestra los spcripts en el actual directorio de python
    scripts = [f for f in os.listdir() if f.endswith('.py')] #archivos con extension .py
    if not scripts: #cuando no hy archivos disponibles
        print("No hay scripts disponibles")
        return

    for i, script in enumerate(scripts,1):   #Scripts numerados
        print(f"{i}.{script}")
    print("0 , para salir")  #salir del programa

    #se solicita al usuario que elija una opcio(script)

    opcion = ("Seleccione una opcion(script) (0 , para salir ")
    if opcion.isdigit() and 1 <= int(opcion) <= len(scripts): #verificacioon de opcioon valida
        script = scripts[int(opcion)-1]  # Obtiene el opcion seleccion
        mostrar_codigo(script)  #Obtencion del codigo seleccioonado
        if input("¿Ejecutar?  (s/n):").lower()=='s': # Pregunta si desea ejecutar el script
            ejecutar_script(script)#Ejecutar script

if __name__ == "__main__": #Entrada del programa
    menu()  #llama a la funcion del menu

