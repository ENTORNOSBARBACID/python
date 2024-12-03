def informacion(e):
    cont=0
    dicS={}
    dicA={}
    for i in e:
        final=e[f'alumno{cont}']['final']
        if final<5:
            dicS[f'alumno{cont}']={
                'nota':e[f'alumno{cont}']['final']
            }
        else:
            dicA[f'alumno{cont}']={
                'nota':e[f'alumno{cont}']['final']
            }
        cont+=1
    return dicA, dicS