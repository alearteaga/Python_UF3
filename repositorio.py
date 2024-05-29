import hashlib
import os
def obtener_hash_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()

def iniciar_sesion(archivo_usuarios):
    try:
        intentos = 3
        while intentos != 0:
            usuario = input("Usuario: ")
            contraseña = input("Contraseña: ")

            with open(archivo_usuarios, 'r') as f:
                for line in f:
                    usuario_guardado, contraseña_guardada = line.strip().split('|')
                    if usuario == usuario_guardado and obtener_hash_md5(contraseña) == contraseña_guardada:
                        print("Inicio de sesión exitoso.")
                        with open('usuario.txt', 'a') as f:
                            f.write(f"{usuario}|{obtener_hash_md5(contraseña)}\n")
                        return True
                print("Usuario o contraseña incorrectos. Inténtelo de nuevo. Te quedan:", intentos - 1, "intentos")
                intentos -= 1

        print("Ha superado el número máximo de intentos. Saliendo del programa.")
        return False
    except IOError:
        print("Error al leer el archivo de usuarios.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    

def mostrar_libro(isbn, archivo):
    try: 
        with open(archivo, 'r') as f:
            for line in f:
                libro_info = line.strip().split('|')
                if libro_info[0] == isbn:
                    return libro_info
            print("El libro con el ISBN", isbn, "no se encontró.")
            return None
    except IOError:
        print("Error al abrir el archivo:")
    except Exception as e:
        print("Se produjo un error inesperado:", e)

def mostrar_todos_libros(archivo):
    try:
        with open(archivo, 'r') as f:
            for line in f:
                yield line.strip().split('|')
    except IOError :
        print(f"Error al abrir el archivo")
        return None
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        return None

def agregar_libro(archivo):
    try:
        isbn = input("Ingrese el ISBN del libro: ")
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el nombre del autor del libro: ")
        
        # Validar el ISBN antes de agregar el libro
        if not isbn or not titulo or not autor:
            print("Por favor, complete todos los campos.")
            return
        
        with open(archivo, 'a') as f:
            f.write(f"{isbn}|{titulo}|{autor}\n")
        print("Libro agregado correctamente.")
    except IOError:
        print("Error al escribir en el archivo.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
    
def eliminar_libro(archivo):
    try:
        isbn = input("Ingrese el ISBN del libro que desea eliminar: ")
        with open(archivo, 'r') as f:
            lines = f.readlines()
        
        with open(archivo, 'w') as f:
            eliminado = False
            for line in lines:
                libro_info = line.strip().split('|')
                if libro_info[0] != isbn:
                    f.write(line)
                else:
                    eliminado = True
            if eliminado:
                print("Libro eliminado correctamente.")
            else:
                print("No se encontró ningún libro con el ISBN", isbn)
    except (FileNotFoundError, IOError):
        print("Error al abrir o manipular el archivo:")
    except PermissionError:
        print("Permiso denegado para manipular el archivo.")
    except Exception as e:
        print("Se produjo un error inesperado:", e)
        
def editar_libro(archivo):
    try:
        isbn = input("Ingrese el ISBN del libro que desea editar: ")
        nueva_isbn = input("Ingrese el nuevo ISBN del libro: ")
        nuevo_titulo = input("Ingrese el nuevo título del libro: ")
        nuevo_autor = input("Ingrese el nuevo autor del libro: ")

        # Validación de datos de entrada
        if not nueva_isbn or not nuevo_titulo or not nuevo_autor:
            print("Por favor, complete todos los campos.")
            return

        # Edición del libro directamente en el archivo
        with open(archivo, 'r+') as f:
            lines = f.readlines()
            f.seek(0)
            for line in lines:
                libro_info = line.strip().split('|')
                if libro_info[0] == isbn:
                    f.write(f"{nueva_isbn}|{nuevo_titulo}|{nuevo_autor}\n")
                else:
                    f.write(line)
            f.truncate()
        
        print("Libro editado correctamente.")
    except (FileNotFoundError, IOError) :
        print("Error al abrir o manipular el archivo:")
    except PermissionError:
        print("Permiso denegado para manipular el archivo.")
    except Exception as e:
        print("Se produjo un error inesperado:", e)
        
        

def verificar_session(archivo_usuarios):
    try:
        with open(archivo_usuarios, 'r') as f:
            for line in f:
                usuario_guardado, contraseña_guardada = line.strip().split('|')
                return usuario_guardado, contraseña_guardada
    except FileNotFoundError:  
        pass
        
def cerrar_sesion():
    print("Cerrando sesión...")
    try:
        os.remove('usuario.txt')
    except FileNotFoundError:
        pass 
    exit()


    