with open("Ejercicios/Practica9/text/texto.txt") as f:
    palabra=f.readline().split(" ")
    
for i in palabra:
    print(i)