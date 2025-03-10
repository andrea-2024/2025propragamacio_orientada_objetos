
#Creacion de la clase libro

class Libro:
    #Creamos el constructor de la clase que inicializara el libro
    def __init__(self, titulo,autor,categoria, codigo):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.codigo = codigo
#Creacion del metodo que nos devuelve una cadena de texto
    def __str__(self):
        return f"\"{self.titulo}\" de {self.autor} (Categoria: {self.categoria}, codigo:{self.codigo})"

#Creacion de la clase usuario

class Usuario:
    def __init__(self,nombre_usuario, codigo_usuario):
        self.nombre_usuario = nombre_usuario
        self.codigo_usuario = codigo_usuario
        self.libros_prestados = []  # Lista de libros prestados al usuario

    def __str__(self):   # Muestra los libros que el usuario tiene prestado
        libros  = ','.join([libro.titulo for  libro in self.libros_prestados]) or "Sin libros prestados"
        return f"{self.nombre_usuario} (Codigo: {self.codigo_usuario})-Libros prestados {libros}"

# Creacion de la clase biblioteca

class Biblioteca:
    def __init__(self):
        self.catalogo = { } #ALmacena los libros disponibles decauerdo al codigo del usuario
        self.usuarios = { } #Almacena a los usuarios registrados por su codigo

    #Metodos de la biblioteca si el libro no está en el catalogo se agrega
    #Caso contrario muestra un mensaje de advertencia

    def agregar_libro(self,libro):
        if libro.codigo not in self.catalogo:
            self.catalogo[libro.codigo] = libro
            print(f"Se agregó el libro {libro}")

        else:
            print("Este libro ya está en la biblioteca")

    #Metodo de la biblioteca para eliminar un libro

    def eliminar_libro(self,codigo):
        if codigo in self.catalogo:
            libro = self.catalogo.pop(codigo)
            print(f"Se eliminó el libro {libro}")
        else:
            print( "EL libro no se encuentra en la biblioteca")

# Metodo registrar usuario, agrega un usario si el codigo no existe

    def registrar_usuario(self, usuario):
        if usuario.codigo_usuario not in self.usuarios:
            self.usuarios[ usuario.codigo_usuario] = usuario
            print( f"Se registó usuario : {usuario.nombre_usuario}")

        else:
            print("El usuario se encuentra registrado")

    # Elimina usuario si su codigo no se encuentra registrado

    def eliminar_usuario (self, codigo_usuario):
        if codigo_usuario in self.usuarios:
            usuario = self.usuarios.pop(codigo_usuario)
            print(f"Usuario eliminado: {usuario.nombre_usuario}")
        else:
            print(" Usuario no se encuentra")


    def prestar_libro(self,codigo_usuario,codigo):
        if codigo_usuario not in self.usuarios:
            print("El usuario no esta registrado.")
            return
        if codigo not in self.catalogo:
            print("El libro no está disponible")
# Si el usuario o el libro no existen muestra error si todo esta normal
#Se elimina del catalogo y se asigna al usuario
        usuario = self.usuarios[codigo_usuario]
        libro = self.catalogo.pop(codigo)  # Se quita del catálogo
        usuario.libros_prestados.append(libro)  # Se agrega a la lista del usuario
        print(f" {usuario.nombre_usuario} ha tomado prestado: {libro}")

    def devolver_libro(self, codigo_usuario, codigo):
        if codigo_usuario not in self.usuarios:
            print("El usuario no se encuentra registrado")
            return

        # Busca si el usuario tiene un libro prestado
        usuario = self.usuarios[codigo_usuario]
        for libro in usuario.libros_prestados:
            if libro.codigo == codigo:
                usuario.libros_prestados.remove(libro)
                self.catalogo[libro.codigo] = libro  # Usar el objeto libro directamente
                print(f"{usuario.nombre_usuario}: ha devuelto el libro {libro}")
                return

        print("Este libro no estaba prestado a ningún usuario")

    def buscar_libros(self, **filtros):
        resultados = [
            libro for libro in self.catalogo.values()
            if all(getattr(libro, k, '').lower() == v.lower() for k, v in filtros.items())
        ]
        return resultados or ["No se encontraron libros."]

    def mostrar_prestamos(self, codigo_usuario):
        if codigo_usuario in self.usuarios:
            usuario = self.usuarios[codigo_usuario]
            return usuario.libros_prestados or ["No tiene libros prestados."]
        return ["Usuario no encontrado."]

libro1 = Libro("Un grito desesperado en la obscuridad", "Carlos Cuautemoc Sanches", "Novela", "L001")
libro2 = Libro("Los juegos del hambre ", "Suzzan Collins", "Ciencia Ficcion", "L002")
libro3 = Libro("De animales a diose", "Yuval Noha Arari","Ficcion","L003" )
libro4 = Libro("La sombra del viento", "Carlos Luis Zafòn ", "Ficcion", "L004")
libro5 = Libro ("Los ojos del perro Siberiano", "Antonio Santa Ana", "Narrativa Juveni", "L005")

# Creacion de biblioteca
biblioteca = Biblioteca()

#Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.agregar_libro(libro4)
biblioteca.agregar_libro(libro5)

#Crear usuarios
usuario1 = Usuario("Andrea Daqui","Us001")
usuario2 = Usuario("Camila Daqui" , "Us002")
usuario3 = Usuario("Kasandra Suarez", "Us003")
usuario4 = Usuario("Sarahi Suarez", "Us004")

#Registrar usuario
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)
biblioteca.registrar_usuario(usuario3)
biblioteca.registrar_usuario(usuario4)


#Prestar libro
biblioteca.prestar_libro("Us003", "L005")
biblioteca.prestar_libro("Us001", "L002")
biblioteca.prestar_libro("Us004", "L003")
biblioteca.prestar_libro("Us002", "L004")

# Devolver un libro
biblioteca.devolver_libro("Us001", "L002")  # Andrea devuelve "Cien años de soledad"

# Mostrar libros disponibles en la biblioteca después del préstamo
print("\nLibros disponibles en la biblioteca:")
for libro in biblioteca.catalogo.values():
    print(libro)

# Mostrar estado de los usuarios
print("\nEstado de los usuarios:")
print(usuario1)  # Andrea no debería tener libros

