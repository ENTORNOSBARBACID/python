import random

nombre1=input("Indica el nombre del jugador 1     ")
nombre2=input("Indica el nombre del jugador 2     ")

a1=random.randint(1, 10)
a2=random.randint(1,10)

d1=random.randint(1, 15)
d2=random.randint(1, 15)

jugador1=[nombre1, a1, d1]
jugador2=[nombre2, a2, d2]

print(jugador1, jugador2)

while jugador1[2]>0 and jugador2[2]>0:
    print(f"Turno de {nombre1}")
    jugador2[2]=jugador2[2]-jugador1[1]
    if jugador2[2]<0:
        print(f"El jugador {nombre2} ha muerto, {nombre1} ha ganado")
        break
    else:       
        print(f"Turno de {nombre2}")
        jugador1[2]=jugador1[2]-jugador2[1]
        if jugador1[2]<0:
            print(f"El jugador {nombre2} ha muerto, {nombre1} ha ganado")
            break
print(jugador1, jugador2)