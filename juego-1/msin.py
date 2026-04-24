import random

numero_secreto = random.randint(1, 10)
intentos = 3

print("🎮 Adivina el número (1 al 10)")
print("Tienes 3 intentos")

while intentos > 0:
    intento = int(input("Tu número: "))
    
    if intento == numero_secreto:
        print("🔥 ¡Ganaste!")
        break
    else:
        intentos -= 1
        print("❌ Incorrecto. Intentos restantes:", intentos)

if intentos == 0:
    print("💀 Perdiste, el número era:", numero_secreto)
