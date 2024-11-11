import random

adivinar=int(random.randint(1,100))
numero=0
contador=0

while numero!=adivinar:
    numero=int(input("Adivina el número     "))
    if numero<adivinar:
        print("El número es mayor")
        contador+=1
    elif numero>adivinar:
        print("El número es menor")
        contador+=1
    if contador>6:
        break


if int(contador)<6:
    print("Ganasteeee!!!!!")
else:
    print(f"Has perdido panoli, el número era {adivinar}")