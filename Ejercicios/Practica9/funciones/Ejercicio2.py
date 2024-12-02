import csv

def añadirNota(e):
    archivo=("python/Ejercicios/Practica9/csv/calificaciones.csv","a")
    contenido=csv.writer(archivo, delimiter=";")
    
    numero=[]
    for i in e:
        numero.append([i[3], i[4]])