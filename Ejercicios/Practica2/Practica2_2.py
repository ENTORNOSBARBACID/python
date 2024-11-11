mes=int(input("Elige un número del 1 al 12  "))
while mes<1 | mes>12:
    mes=int(input("Elige un número del 1 al 12  "))

fecha30=(4, 6, 9, 11)
fecha31=(1, 3, 5, 7, 8, 10, 12)
febrero=2

if mes in fecha30:
    dias=30
elif mes in fecha31:
    dias=31
else:
    dias=28
    
print(f"El número de días del mes nº{mes} es {dias}")