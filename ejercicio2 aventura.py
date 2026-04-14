pip install random
pip install datetime\

import random
from datetime import datetime

def generar_nombre():
  nombres_heroes = ["Link", "Zelda", "Mario", "Gru", "Luigi", "Sonic"]
  return random.choice(nombres_heroes)

def generar_clase():
  clases_heroes = ["Guerrero", "Mago", "Arquero", "Sanador", "Tanque", "Asesino"]
  return random.choice(clases_heroes)

def generar_hp():
  return random.randint(80, 120)

def mostrar_fecha():
  fecha_actual = datetime.now()
  print(f"Fecha: {fecha_actual.day}/{fecha_actual.month}/{fecha_actual.year}")

print("=== GENERADOR DE AVENTURAS ===")
mostrar_fecha()
print("------------------------------")
print("=== Heroes Generados ===")

for i in range(1, 4):
  nombre = generar_nombre()
  clase = generar_clase()
  hp = generar_hp()
  print(f"Heroe {i}: {nombre} | Clase: {clase} | HP: {hp}")
