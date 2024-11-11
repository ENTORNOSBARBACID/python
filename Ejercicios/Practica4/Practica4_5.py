def filtrarPalabras(lista, n):
    for i in lista:
        if len(i)<n:
            lista.remove(i)
            
    return lista

lista=["wdadsdada", "sdadsadad", "sa"]
n=5

lista=filtrarPalabras(lista, n)
print(lista)