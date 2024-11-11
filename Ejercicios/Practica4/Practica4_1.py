par=""
max=0
cont=0
number=int(input("Choose a number, if you put a negative number, the program will finish     "))
listnumbers=[]

while number>0:
    listnumbers.append(number)
    if listnumbers[cont]%2==0:
        par+=str(listnumbers[cont])+", "
    if max<listnumbers[cont]:
        max=listnumbers[cont]    
    number=int(input("Choose a number, if you put a negative number, the program will finish     "))
    cont+=1

print("Par numbers= "+par+" higher number= "+str(max))