print ("Bienvenido al juego de piedra, papel o tijeras")


Nombre1 = input ("¿Cómo se llama el jugador 1? ")
Nombre2 = input ("¿Cómo se llama el jugador 2? ")


print ("Comenzemos, ¡el mejor de 3 gana!")


Condición1 = jugador1 == "piedra" and jugador2 == "tijeras"
Condición2 = jugador1 == "papel" and jugador2 == "piedra"
Condición3 = jugador1 == "tijeras" and jugador2 == "papel"


puntos1 = 0
puntos2 = 0
puntos_maximos = 2


while not puntos1 >= puntos_maximos and not puntos2 >= puntos_maximos:
 jugador1 = input (Nombre1 + " ¿Qué elijes, piedra, papel o tijeras? ")
 jugador2 = input ("Ahora " + Nombre2 + " ¿Qué elijes, piedra, papel o tijeras? ")


 if jugador1 == jugador2:
  print("¡Ha sido un empate")
 elif Condición1 or Condición2 or Condición3:
  print("¡Ha ganado " + Nombre1 + "!")
  puntos1 += 1
 else:
  print("¡Ha ganado " + Nombre2 + "!")
  puntos2 += 1


print("Score: " + Nombre1 + " tiene " + (str(puntos1)) + " puntos y " + Nombre2 + " tiene " + (str(puntos2)))


if puntos1 == puntos_maximos:
  print("¡Felicidades " + Nombre1 + " eres el ganador!")
elif puntos2 == puntos_maximos:
  print("¡Felicidades " + Nombre2 + " eres el ganador!")
