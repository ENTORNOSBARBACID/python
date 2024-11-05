dicNombres={
    'Persona1':{
        'Nombre':'Sergio',
        'Gustos': 'Comer penes'
            }, 
    'Persona2':{
        'Nombre':'Pinilla',
        'Gustos': 'Bailar drill', 
                },
    'Persona3':{
        'Nombre':'Enzo',
        'Gustos': 'Ver Hentai', 
    },
    'Persona4':{
        'Nombre':'Alex',
        'Gustos': 'Fumar y gastar dinero en la ruleta', 
    }
    }
count=5
exist=True
nombre=input("Introuce el nombre    ")

while nombre!="END":
    gustos=input("Introduce los gustos que quiere añadir    ")
    for p in dicNombres:
        if dicNombres[p]['Nombre']==nombre:
            dicNombres[p]['Gustos']+=", "+gustos
            exist=True
            break
        else:
            exist=False

    if exist==False:
        dicNombres[f'Persona{count}']={
                                    'Nombre':nombre,
                                    'Gustos':gustos,
                                        }
        count+=1
        exist=True
        
    print(dicNombres)
    nombre=input("Introuce el nombre    ")

