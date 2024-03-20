
import random

partida = 1

usuario = 0
pc = 0
user_1 = ('piedra','papel','tijera')
while True:

  if usuario < 2 or pc < 2:
    
    print('*' * 10)
    print(f"Partida {partida}")
    print('*' * 10)
    
    print(f"usuario {usuario}")
    print(f"pc {pc}")
  
    user_1 = input("Escoge => piedra, papel o tijera =>")
    user_1 = user_1.lower()
    user_pc = random.choice(["piedra", "papel", "tijera"])
    user_pc = user_pc.lower()
  
    if not user_1 in ("piedra", "papel", "tijera"):
      print("No es una opcion valida")
  
    if (user_1 == user_pc):
      print("Empate")
    elif (user_1 == "piedra"):
      if (user_pc == "tijera"):
        print("tu ganaste, piedra gana a tijera")
        usuario += 1
      else:
        print("tu perdiste papel gana a piedra")
        pc += 1
  
    elif (user_1 == "papel"):
      if (user_pc == "tijera"):
        print("tu perdiste, tijera gana a papel")
        pc += 1
      else:
        print("tu ganaste, papel gana a piedra")
        usuario += 1
        
    elif (user_1 == "tijera"):
      if (user_pc == "papel"):
        print("tu ganaste, tijera gana a papel")
        usuario += 1
      else:
        print("tu perdiste piedra gana a tijera")
        pc += 1

  if usuario == 2:
    print(f"usuario ganó")
    break

  if pc == 2:
    print(f"pc ganó")
    break
  
  partida += 1
  