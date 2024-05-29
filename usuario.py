import hashlib
def obtener_hash_md5(texto):
    return hashlib.md5(texto.encode()).hexdigest()
def añadir_usuario(archivo_usuarios):
    usuario = input("Nuevo usuario: ")
    contraseña = input("Contraseña: ")
    with open(archivo_usuarios, 'a') as f:
        f.write(f"{usuario}|{obtener_hash_md5(contraseña)}\n")
    print("Usuario añadido correctamente.")

archivo_usuarios = './usuarios.txt'
añadir_usuario(archivo_usuarios)
