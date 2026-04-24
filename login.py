# login.py

usuario_real = "admin"
contrasena_real = "g4$#"

def verificar(usuario, contrasena):
    if usuario == usuario_real and contrasena == contrasena_real:
        return True
    else:
        return False
