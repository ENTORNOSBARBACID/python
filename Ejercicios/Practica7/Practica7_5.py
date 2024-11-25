dicAlumnos={
    'Alumno':{
            'Nombre':'Jared',
            'Nota':9
        },
    'Alumno2':{
            'Nombre':'Pinilla',
            'Nota':1
        },
    'Alumno3':{
            'Nombre':'Sergio',
            'Nota':4
        },
    'Alumno1':{
            'Nombre':'Alberto',
            'Nota':13
        }
}
dicAprobados=list(filter(lambda i: i["Nota"]>=5, dicAlumnos.values()))
dicSuspensos=list(filter(lambda i: i["Nota"]<5, dicAlumnos.values()))

print(dicAprobados)
print("-----------------------")
print(dicSuspensos)