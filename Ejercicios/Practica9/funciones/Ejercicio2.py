import csv

def añadirNota(e):
    
    dic={}
    cont=0
    for i in e:
        dic[f"alumno{cont}"]={
            'asistencia':i[2][0:2],
            'parcial1':i[3].replace(",", '.'),
            'parcial2':i[4].replace(",", '.'),
            'ordinario1':i[5].replace(",", '.'),
            'ordinario2':i[6].replace(",", '.'),
            'practicas':i[7].replace(",", '.'),
            'ordinarioPracticas':i[8].replace(",", '.')
            }
        final=float(dic[f"alumno{cont}"]['parcial1'])*0.3+float(dic[f"alumno{cont}"]['parcial2'])*0.3
        if dic[f"alumno{cont}"]['practicas']!='':
            final=final+float(dic[f"alumno{cont}"]['practicas'])*0.
        elif dic[f"alumno{cont}"]['ordinarioPracticas']!='':
            final=final+float(dic[f"alumno{cont}"]['ordinarioPracticas'])*0.
        dic[f"alumno{cont}"]['final']=final
        
        cont+=1
    return dic        
        