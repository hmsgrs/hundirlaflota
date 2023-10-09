import numpy as np
import pandas as pd
import random
import vars


class tablero:
    

    def __init__(self):
        self.tab = np.full((10,10), "_")#esta es la matriz de juego propia
        self.dis = np.full((10,10), "_")#esta es la matriz de disparos propia

    def inicializa(self):
        #vamos a iterar por la lista de "flota"
        for i in vars.flota: 
            done = False
            while done == False:
                # Mientras no haya un nuevo tablero válido, seguimos probando
                # Creamos un tablero de trabajo para no modificar el original, porque al final del todo puede salirse del bucle 
                # en un paso intermedio
                # Si no usamos una copia, "ensuciamos" el original y al reiniciar se quedan cachos de barco por el tablero.
                working_tablero = np.copy(self.tab)    
                collide = False
                ori = random.choice(["N","S","E","O"])
                pos_x = random.randint(0,9)
                pos_y = random.randint(0,9)
                # Direcciones en las que vamos a comprobar que no haya barcos
                vectores  = [[0,-1],[0,1],[1,0],[-1,0],[0,0],[1,1],[-1,-1],[1,-1],[-1,1]]
                if ori == "N":
                    mod_x = 0
                    mod_y = -1
                    # Direcciones en las que vamos a comprobar que no haya listones cuando vayamos poniéndolos. 
                    # Es distinto por cada dirección porque iremos recorriendo el tablero y no queremos comprobar
                    # donde hemos puesto el anterior listón
                    vec = [[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
                elif ori == "S":
                    mod_x = 0
                    mod_y = 1
                    vec = [[0,1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
                elif ori == "E":
                    mod_x = 1
                    mod_y = 0
                    vec = [[0,-1],[0,1],[1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
                elif ori == "O":
                    mod_x = -1
                    mod_y = 0
                    vec = [[0,-1],[0,1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
                # Primero hacemos la comprobación de que podemos poner bien el primer listón del barco, comprobamos para todos los lados
                for vector in vectores:
                    #estamos dentro del tablero?
                    if pos_x+vector[0] > -1 and pos_x+vector[0] <= 9 and pos_y+vector[1] > -1 and pos_y+vector[1] <= 9:
                        #estamos ENCIMA de un barco?
                        if working_tablero[pos_x+vector[0],pos_y+vector[1]] != "_":
                            collide = True
                            break
                for j in range(i):
                    #estamos dentro del tablero?
                    if pos_x > -1 and pos_x <= 9 and pos_y > -1 and pos_y <= 9:
                        # estamos ENCIMA de un barco?
                        if working_tablero[pos_x,pos_y] != "_":
                            collide = True
                            break         
                        # Comprobamos que hay espacio en todos lados MENOS del que venimos, para eso tenemos el vec distinto por dirección
                        for vector in vec:
                            if pos_x+vector[0] > -1 and pos_x+vector[0] <= 9 and pos_y+vector[1] > -1 and pos_y+vector[1] <= 9:
                                if working_tablero[pos_x+vector[0],pos_y+vector[1]] != "_":
                                    collide = True              
                                    break
                        # Si no hay colisión de ningún tipo, entonces ponemos el listón del barco
                        if not collide:
                            working_tablero[pos_x,pos_y] = "B"
                            #para seguir alimentando el bucle, sumamos uno a los listones, repitiendo las comprobaciones ahora para el siguiente listón en el siguiente bucle de j.
                            pos_x += mod_x
                            pos_y += mod_y
                    else:
                        collide = True
                        break
                if collide == False:
                    # Si no ha habido colisiones, copiamos el nuevo tablero encima del viejo tablero.
                    self.tab = np.copy(working_tablero)
                    done = True               
        
         
    def dispara(self,x,y):
        if self.tab[x,y] != "_":
            self.dis[x,y] = "X"
        else:
            self.dis[x,y] = "O"
 
    def comprueba(self):
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                if self.tab[i,j] != "_":
                    if (self.dis[i,j] != "X"):
                        return False
        return True   
    def ver_juego(self, maquina = False):
        if maquina:
            print ("Tablero")
            self.print_tablero(self.tab)
        print ("Disparos")
        self.print_tablero(self.dis)
    def get_letters_to_numbers(self):
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
        return letters_to_numbers
    def print_tablero(self,t):
        tablero_p = pd.DataFrame(t, columns=vars.columnas,index=vars.filas)
        print(tablero_p)
    def ya_disparada(self,x,y):
        if self.dis[x,y] == "X" or self.dis[x,y] == "O":
            return True
        else:
            return False