import login
import string
import itertools

usuario = "admin"

simbolos = "@#$_&-+()/*':;!?"
caracteres = string.ascii_lowercase + string.digits + simbolos

longitud = 3  # empieza bajo

for intento in itertools.product(caracteres, repeat=longitud):
    intento = ''.join(intento)

    print(f"Probando: {intento}")

    if login.verificar(usuario, intento):
        print("Contraseña encontrada:", intento)
        break
else:
    print("No se encontró la contraseña")
