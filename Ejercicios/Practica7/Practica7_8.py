nombres=['Sergio', 'Pinilla', 'Pedro']
saludos=['Hola', 'Hi', 'Hello']

resultado=[y.split()+ x.split() for x in nombres for y in saludos]

print(resultado)