def drawRectangule(altura, anchura):
    res=""   
    for i in range(altura):
        res+="\n    *   "
        for k in range(anchura-1):
         res+="   *   "
    return res


altura=int(input("Altura:   "))
anchura=int(input("Anchura:   "))

res=drawRectangule(altura, anchura)

print(res)