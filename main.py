import functions
import vars
import random


player = functions.tablero()
player.inicializa()
computer = functions.tablero()
computer.inicializa()

print ("------ TABLERO DEL JUGADOR -------")
player.ver_juego(True)

print ("------ COMIENZA LA PARTIDA -------")
while (player.comprueba() == False and computer.comprueba() == False):
    """y = int(input("Introduce la coordenada x: "))
    x = int(input("Introduce la coordenada y: "))"""
    x = input("Introduzca la coordenada línea de su disparo")
    while int(x) > 10 or int(x) < 1:
        print('Línea incorrecta, vuelva a intentarlo')
        x = input("Introduzca la coordenada línea de su disparo")
        
    y = input("Introduzca la coordenada columna de su disparo").upper()
    while y not in "ABCDEFGHIJ":
        print('Columna incorrecta, vuelva a intentarlo')
        y = input("Introduzca la coordenada columna de su disparo").upper()
    """ global x
    global y"""
    x = int(x) - 1
    y = player.get_letters_to_numbers()[y]

    
    computer.dispara(x,y)
    """if acierto == True:
        y = int(input("Introduce la coordenada x: "))
        x = int(input("Introduce la coordenada y: "))
        computer.dispara(x,y)"""

    x = random.randint(0,9)
    y = random.randint(0,9)

    while (player.ya_disparada(x,y)):
        x = random.randint(0,9)
        y = random.randint(0,9)
    player.dispara(x,y)
    print ("------ ORDENADOR -------")
    computer.ver_juego(True)
    print ("------ JUGADOR -------")
    player.ver_juego(True)

if (player.comprueba() == True):
    print("Ha ganado la máquina!")
if (computer.comprueba() == True):
    print("Has ganado!")
    computer.ver_juego(True)


        