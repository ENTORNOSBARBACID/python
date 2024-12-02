import csv

with open("Ejercicios/Practica9/csv/AlumnosFP.csv", "r", encoding='latin-1') as f:
    nombres=list(csv.reader(f, delimiter=";"))
    nombres=nombres[1:]
    

correos=[]
    
for i in nombres:
   correos.append(i[1])
   
with open("Ejercicios/Practica9/csv/ListadoAlumnosFP.csv", "r", encoding='latin-1') as f:
    nombre=list(csv.reader(f, delimiter=";"))
    
    nombre=nombre[1:]
    
    print(nombre)
    
correoAlumno=[]

for i in nombre:
    correo=i[0].lower()+"."+i[1].lower()+"@plazacastilla.salesianas.org"
    if correo in correos:
        correo=i[0].lower()+"."+i[1].lower()+"."+i[2].lower()+"@plazacastilla.salesianas.org"
        correoAlumno.append(correo)
    else:
        correoAlumno.append(correo)
        
print(correoAlumno)

fichero=open("Ejercicios/Practica9/csv/AlumnosFP.csv", "a")
contenido=csv.writer(fichero, delimiter=";")

nombreJunto=[]

for i in nombre:
    nombreJunto.append(" ".join(i))
    
for i in range(0, len(nombre)):
    contenido.writerow([nombreJunto[i], correoAlumno[i], 'Ventajas de uso de Microsoft 365 A3 para estudiantes'])
