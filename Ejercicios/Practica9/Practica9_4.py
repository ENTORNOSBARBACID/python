with open("Ejercicios/Practica9/text/texto.txt") as f:
    palabra=f.readline().split(" ")
    
cleanPalabra=[]

for i in palabra:
    if i not in cleanPalabra:
        cleanPalabra.append(i)

mas=""

for i in cleanPalabra:
    if palabra.count(i)>palabra.count(mas):
        mas=i
    
print("La palabra que mas sale es "+mas+", apareciendo un total de "+str(palabra.count(mas))+" veces")