dicCodigo = {
'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', '1': '.----',
'2': '..---', '3': '...--', '4': '....-',
'5': '.....', '6': '-....', '7': '--...',
'8': '---..', '9': '----.', '0': '-----',
'.': '.-.-.-', ',': '--..--', ':': '---...',
';': '-.-.-.', '?': '..--..', '!': '-.-.--',
'"': '.-..-.', "'": '.----.', '+': '.-.-.',
'-': '-....-', '/': '-..-.', '=': '-...-',
'_': '..--.-', '$': '...-..-', '@': '.--.-.',
'&': '.-...', '(': '-.--.', ')': '-.--.-'
}

cadena=input("Escribe una letra, numero o simbolo y se traducira a codigo morse    ")
letra=cadena.split(" ")
letraMay=[]
for i in letra:
    letraMay.append(i.upper())

for item in dicCodigo:
    for i in letraMay:
        if str(item)==i:
            print(f"{i}: {dicCodigo[item]}")