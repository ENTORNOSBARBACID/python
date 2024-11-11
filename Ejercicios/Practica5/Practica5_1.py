def findName(names, n):
    for i in names:
        if(i==n):
            return True

    return False


cadena=input("Escribe una frase     ")
palabra=cadena.split(" ")
palabraClean=[]
num=[]
dic={}
for item in palabra:
    exist=findName(palabraClean, item)
    if exist==False:
        num.append(palabra.count(item))
        palabraClean.append(item)
        
for p,n in zip(palabraClean, num):
    dic[p]=n
    
print(dic)