from funciones.Apartados import crearDiccionario, ordenar_diccionario

nombres="Sergio,10,12,23;Alberto,50,50,60;Pinilla,3,1,0;Alberto,20,30,13;"
print(60*"-")
print("Apartado 1:")
print(nombres)
print(60*"-")
d=crearDiccionario(nombres)
print("Apartado 2:")
print(d)
print(60*"-")
o=ordenar_diccionario(d)
print("Apartado 3:")
print(o)
print(60*"-")