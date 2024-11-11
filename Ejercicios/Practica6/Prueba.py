from Validar.Usuario import validarUsuario
from Validar.Contraseña import validarContraseña

usuario="Peadad"
validar=validarUsuario(usuario)
print(validar)

contraseña="HOLES1TA*S"
validar=validarContraseña(contraseña)
print(validar)