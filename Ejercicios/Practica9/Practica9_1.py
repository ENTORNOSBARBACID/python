nombre=""
numero=""
cont=1
opc=int(input('1.Añadir\n2.Consultar número\n3.Eliminar\n'))
while opc<4 | opc>0:
    if opc==1:
        nombre=input("Introduce the name of the client:  ")
        numero=input("Introduce the number of  the client:  ")
        with open('Ejercicios/Practica9/text/Listin.txt', 'a') as f:
            f.writelines(nombre+", "+numero+"\n")
            print("Añadido")
        f.close()
    elif opc==2:
        nombre=input("Introduce the name of the client:  ")
        f=open("Ejercicios/Practica9/text/Listin.txt", "r")
        for linea in f:
            if nombre in linea:
                telefono=linea.strip().split(",")
                print(telefono[1])
                break
        f.close()
    elif opc==3:
        nombre=input("Introduce the name of the client:  ")
        f=open("Ejercicios/Practica9/text/Listin.txt", "r")
        lineas=f.readlines()
        with open('Ejercicios/Practica9/text/Listin.txt', 'w') as f:
            for linea in lineas:
                if nombre not in linea:
                    f.write(linea)
        
    opc=int(input('1.Añadir\n2.Consultar número\n3.Eliminar\n'))


"""Sergio, 689 98 09 98
Pinilla, 678 98 65 75
Alberto, 667 86 97 92"""