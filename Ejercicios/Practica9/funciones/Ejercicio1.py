import csv
def crearDic():
    with open("python/Ejercicios/Practica9/csv/calificaciones.csv", "r",encoding='latin-1') as f:
        e=list(csv.reader(f, delimiter=";"))
        e=e[1:] 
        
        
    
    return e