import os
import time
from repositorio import *

archivo_usuarios = 'usuarios.txt'
archivo_libros = 'libros.txt'
session = 0

try:
    usuario_guardado, contraseña_guardada = verificar_session('usuario.txt')
    if usuario_guardado is not None and contraseña_guardada is not None:
        print("¡Bienvenido de nuevo!", usuario_guardado)
        session = 1
except FileNotFoundError:
    pass
except TypeError:
    pass

if session == 0: 
    estado = iniciar_sesion(archivo_usuarios)
    if not estado:
        exit()

time.sleep(2)

while True:
    time.sleep(1)
    os.system('clear')
    print("\n1. Mostrar un libro por ISBN")
    print("2. Mostrar todos los libros")
    print("3. Agregar un libro")
    print("4. Eliminar un libro")
    print("5. Editar un libro")
    print("6. Salir")
    print("7. Salir y cerrar sesion")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == '1':
            isbn_a_buscar = input("Ingrese el ISBN del libro: ")
            libro_encontrado = mostrar_libro(isbn_a_buscar, archivo_libros)
            if libro_encontrado:
                print("Información del libro:")
                print("ISBN:", libro_encontrado[0])
                print("Título:", libro_encontrado[1])
                print("Autor:", libro_encontrado[2])
            else:
                print("Libro no encontrado.")
        elif opcion == '2':
            print("Todos los libros:")
            libros = mostrar_todos_libros(archivo_libros)
            for libro in libros:
                print("ISBN:", libro[0])
                print("Título:", libro[1])
                print("Autor:", libro[2])
                print()
        elif opcion == '3':
            agregar_libro(archivo_libros)
        elif opcion == '4':
            eliminar_libro(archivo_libros)
        elif opcion == '5':
            editar_libro(archivo_libros)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        elif opcion == '7':
            print("Saliendo del programa...")
            cerrar_sesion()

        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
    except Exception as e:
        print("Se produjo un error:", e)
