
import math


numero=input("Pon los minutos  ")
horas=math.trunc(int(numero)/60)
minutos=int(numero)%60

print(f"Son {horas} horas y {minutos} minutos")