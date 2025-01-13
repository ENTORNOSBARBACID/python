def crearDiccionario(nombres):
    dic={}
    contenido=nombres.split(";")
    contenido=contenido[0:-1]
    
    for i in contenido:
        fila=i.split(",")
        clave=fila[0]
        total=int(fila[1])+int(fila[2])+int(fila[3])
        if clave in dic:
            dic[clave].append(total)
        else:
            dic[clave]=[total]
    
    return dic
        
def ordenar_diccionario(dic):
    dic=dict(sorted(dic.items()))
    return dic