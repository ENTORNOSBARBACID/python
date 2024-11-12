from Validar.Usuario import validarUsuario
from Validar.Contraseña import validarContraseña

usuario=input("Introduce el nombre de usuario, introdue '*' para terminar   ")
contraseña=input("Introduce la contraseña del usuario   ")
dicUsuarios={}
validar=True
while usuario != "*":
    validar=validarUsuario(usuario)
    print(validar)
    if validar==True:
        validar=validarContraseña(contraseña)   
        print(validar)     
        if validar==True:
            dicUsuarios[usuario]=contraseña
            print("El usuario se ha creado correctamente    ")
    validar==True
    usuario=input("Introduce el nombre de usuario, introdue '*' para terminar   ")
    contraseña=input("Introduce la contraseña del usuario   ")

print(dicUsuarios)