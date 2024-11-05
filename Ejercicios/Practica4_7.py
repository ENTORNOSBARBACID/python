def findName(names, n):
    for i in names:
        if(i==n):
            return True

    return False


name=input("Name    ")


names=[]
namesClear=[]
while name!="":
    names.append(name)
    name=input("Name    ")

for i in names:
    exist=findName(namesClear, i)
    if exist==False:
        print(f"{i}:{names.count(i)}")
        namesClear.append(i)