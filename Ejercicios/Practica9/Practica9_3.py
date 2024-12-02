def contador(e):
    
    with open("Ejercicios/Practica9/text/Contador.txt", "r") as f:
        cont = f.read()
        
    if cont == "":
        cont = 0
    else:
        cont = int(cont)
        
    if e == "Inc":
        cont += 1
    elif e == "Dec":
        cont -= 1
        
    with open("Ejercicios/Practica9/text/Contador.txt", "w") as f:
        f.write(str(cont))

contador("d")