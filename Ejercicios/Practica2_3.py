palabra=input("Escribe una letra o numero   ")

if len(palabra)==1:
    if palabra.isnumeric():
        print("Es un número")
    elif palabra==palabra.upper():
        print("Está en mayúsculas")
    else:
        print("Está en minúsculas")
else:
    print("Solo una letra")