import random

adivinar=int(random.randint(1,100))
numero=0

while numero!=adivinar:
    numero=int(input("Adivina el número     "))
    if numero<adivinar:
        print("El número es mayor")
    else:
        print("El número es menor")
        
print("Ganasteeee!!!!!")