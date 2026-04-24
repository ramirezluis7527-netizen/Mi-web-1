import os

x = 2
y = 2

mapa = [
    ["⬜","⬜","⬜","⬜","⬜"],
    ["⬜","⬜","⬜","⬜","⬜"],
    ["⬜","⬜","🟦","⬜","⬜"],
    ["⬜","⬜","⬜","⬜","⬜"],
    ["⬜","⬜","⬜","⬜","⬜"]
]

while True:
    os.system("clear")
    
    for fila in mapa:
        print(" ".join(fila))
    
    movimiento = input("W/A/S/D: ").lower()
    
    mapa[y][x] = "⬜"
    
    if movimiento == "w" and y > 0:
        y -= 1
    elif movimiento == "s" and y < 4:
        y += 1
    elif movimiento == "a" and x > 0:
        x -= 1
    elif movimiento == "d" and x < 4:
        x += 1
    
    mapa[y][x] = "🟦"
