import random

cont=0
res=""
boleto=[]
cont=1
i=0
numSuyo=""
numGanador=""
while cont>50:
    boleto.append(cont)
    cont+=1

while i < 10:
    res+="\n"+str(i)+" "+str(i+10)+" "+str(i+20)+" "+str(i+30)+" "+str(i+40)
    i+=1
    
print(res)

num=input(f"Put your number {cont}     ")
numSuyo+=str(num)+" "
while cont!=6:
    cont+=1
    num=input(f"Put your number {cont}     ")
    numSuyo+=str(num)+" "

cont=0
while cont!=6:
    cont+=1
    num=random.randint(1, 50)
    numGanador+=str(num)+ " "

print(numSuyo)
print(numGanador)

listaSuyo=numSuyo.split(" ")
listaGanador=numGanador.split(" ")

cont=0

for i in listaGanador:
    for k in listaSuyo:
        if i==k:
            cont+=1

print(f"Has acertado {cont-1} veces¡¡")

