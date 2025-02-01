import os   # Importamos la librería para manejar archivos y directorios

# Función para mostrar el código de un archivo Python
def mostrar_codigo(ruta_script):
    """Lee y muestra el contenido de un archivo Python."""
    try:
        with open(ruta_script, 'r') as archivo:
            print(archivo.read())  # Muestra el contenido del archivo
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")  # Muestra otros errores posibles

# Función para mostrar las carpetas disponibles
def mostrar_menu():
    """Muestra el menú principal con las carpetas disponibles."""
    ruta_base = os.path.dirname(os.path.dirname(__file__))   # Obtiene la ruta del proyecto

    # Paso 1: Listar carpetas UNIDAD1 a UNIDAD8 dentro del proyecto
    carpetas_disponibles = []
    for numero in range(1, 9):  # Del 1 al 8
        carpeta = f"Unidad{numero}"  # Construimos el nombre de la carpeta (Unidad1, Unidad2, etc.)
        ruta_carpeta = os.path.join(ruta_base, carpeta)  # Creamos la ruta completa
        if os.path.isdir(ruta_carpeta):  # Verificamos si la carpeta existe
            carpetas_disponibles.append(ruta_carpeta)  # Agregamos a la lista

    if not carpetas_disponibles:  # Si no hay carpetas encontradas, mostramos un mensaje
        print("No se encontraron carpetas de unidades.")
        return

    while True:
        # Mostramos el menú de carpetas
        print("\n******** Menú Principal - Selecciona una Unidad *************")
        for i, carpeta in enumerate(carpetas_disponibles, start=1):  # Enumeramos las carpetas
            print(f"{i} - {os.path.basename(carpeta)}")  # Mostramos solo el nombre de la carpeta
        print("0 - Salir")  # Opción para salir

        seleccion_carpeta = input("Elige una unidad para ver los archivos o '0' para salir: ")

        if seleccion_carpeta == '0':  # Si elige 0, salimos del programa
            break
        elif seleccion_carpeta.isdigit() and 1 <= int(seleccion_carpeta) <= len(carpetas_disponibles):
            ruta_elegida = carpetas_disponibles[int(seleccion_carpeta) - 1]  # Obtiene la ruta de la carpeta seleccionada
            mostrar_archivos(ruta_elegida)  # Llama a la función para mostrar los archivos de esa unidad
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")  # Mensaje de error si la opción no es válida

# Función para mostrar los archivos dentro de la carpeta seleccionada
def mostrar_archivos(ruta_carpeta):
    """Muestra los archivos Python dentro de la carpeta seleccionada."""
    archivos_py = [f for f in os.listdir(ruta_carpeta) if f.endswith(".py")]  # Filtra solo archivos .py

    if not archivos_py:  # Si no hay archivos Python, muestra un mensaje
        print("No hay archivos Python en esta unidad.")
        return

    while True:
        # Mostramos los archivos disponibles
        print("\n******** Archivos Python *************")
        for i, archivo in enumerate(archivos_py, start=1):  # Enumeramos los archivos
            print(f"{i} - {archivo}")  # Mostramos solo el nombre del archivo
        print("0 - Regresar")  # Opción para regresar

        seleccion_archivo = input("Elige un archivo para ver su código o '0' para regresar: ")

        if seleccion_archivo == '0':  # Si elige 0, volvemos al menú de unidades
            break
        elif seleccion_archivo.isdigit() and 1 <= int(seleccion_archivo) <= len(archivos_py):
            ruta_script = os.path.join(ruta_carpeta, archivos_py[int(seleccion_archivo) - 1])  # Obtiene la ruta del archivo seleccionado
            mostrar_codigo(ruta_script)  # Llama a la función para mostrar el código del archivo
        else:
            print("Opción no válida. Intento de nuevo.")  # Mensaje de error si la opción no es válida

# Ejecutar el programa
if __name__ == "__main__":
    mostrar_menu()  # Llama a la función principal cuando se ejecuta el script