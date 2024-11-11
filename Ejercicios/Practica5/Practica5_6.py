dicFacturas={
    '1234':123,
    '1432':1045,
    '1928':2300
}
opc=int(input("1.Añadir\n2.Pagar\n3.Salir\n"))

while(opc<3):
    if(opc==1):
        nfac=input("introduce el nuevo número de factura\n")
        coste=int(input("introduce el coste\n"))
        dicFacturas[nfac]=coste
        print(dicFacturas)
    elif(opc==2):
        nfac=input("introduce el número de factura\n")
        del(dicFacturas[nfac])
        print(dicFacturas)
        
    opc=int(input("1.Añadir\n2.Pagar\n3.Salir\n"))