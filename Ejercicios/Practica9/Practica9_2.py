dicDatos={}
with open("Ejercicios/Practica9/text/Nombres.txt", "r") as f:
    for linea in f:
        datos=linea.split(";")
        dicDatos[datos[0]]={
            "Nombre":datos[1],
            "Apellido":datos[2],
            "Fecha":datos[3],
        }

print(dicDatos)