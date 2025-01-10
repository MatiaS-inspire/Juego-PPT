print ("Bienvenidos al juego de piedra, papel o tijeras")

Nombre1 = input ("¿Cómo se llamará el jugador 1? ")
Nombre2 = input ("¿Cómo se llamará el jugador 2? ")

Jugador1 = input ("¡Hola " + Nombre1 + "! ¿Qué eliges? ¿piedra, papel o tijeras? ")
Jugador2 = input ("¡Ahora " + Nombre2 + "! ¿Qué eliges? ¿piedra, papel o tijeras? ")

Condicion1 = Jugador1 == "piedra" and Jugador2 == "tijeras"
Condicion2 = Jugador1 == "papel" and Jugador2 == "piedra"
Condicion3 = Jugador1 == "tijeras" and Jugador2 == "papel"

if Jugador1 == Jugador2:
        print ("¡Ha sido un empate!")
elif Condicion1 or Condicion2 or Condicion3:
        print ("¡Ha ganado!", Nombre1)
else:
        print ("¡Ha ganado!", Nombre2)
 