def isNotInList(n, lista):
    for t in lista:
        if t[0]==n:
            return False
    return True
def agePerson(lista, n):
    for t in lista:
        if t[0]==n:
            if int(t[1])<20:
                return False
    return True

name=input("Name    ")

person=[]
names=[]
more20=[]
t=[]
while name!="":
    names.append(name)
    name=input("Name    ")
    
    
print(person)
for i in names:
    if isNotInList(i, person):
        print(i)
        age=input("Age  ")
        t=[i,age]
        person.append(t)
        if agePerson(person, i)==True:
            more20.append(t)
    
print("Personas")
print(f"{person}")
print("\nPersonas mayores de 20")
print(more20)