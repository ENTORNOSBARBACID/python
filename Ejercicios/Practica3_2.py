def calculateTriangle1(width, sign):
    res=""
    for i in range(width):
        res+=str(sign*i+"\n")
    return res

def calculateTriangle2(width, sign):
    res=""
    while width>0:
        res+=str(sign*width+"\n")
        width-=1
    return res

width=int(input("Choose width   "))
sign=input("Choose sign    ")

res=calculateTriangle1(width, sign)
res+=calculateTriangle2(width, sign)

print(res)