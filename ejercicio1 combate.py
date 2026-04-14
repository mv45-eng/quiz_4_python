hp_heroe = 100
hp_enemigo = 50.

estado_inicial = hp_heroe == 100 and hp_enemigo == 50.



def calcular_dano(ataque, defensa):
  return ataque - defensa


def aplicar_dano(hp_actual, dano):
  resultado = hp_actual - dano
  if resultado > 0:
      return hp_actual - dano
  else:
      return 0


def realizar_ataque(atacante, defensor, dano):
  return(f"{atacante} ataca a {defensor} por {dano} de daño!")

print(f"----Estado Inicial----")
print(f"HP Heroe: {hp_heroe}")
print(f"HP Enemigo: {hp_enemigo}")
print("-------------------------")
print(calcular_dano(25, 10))
print(realizar_ataque("Mateo", "Slime", 15))
print(aplicar_dano(hp_enemigo, 15))
print(f"Estado del enemigo: {hp_enemigo-15}")
