import numpy as np

#definimos las constantes
FILAS = 10
COLUMNAS = 10
MAR = " "
n_submarinos = 4  # Ocupa una celda hay 4
n_barcos = 3  # Ocupa dos celdas hay 3
n_navios = 2  # Ocupa tres celdas hay 2
n_portaviones = 1  # Ocupa 4 celdas hay 1

######################################################
## Código para imprimir la matriz de manera vistosa ##
######################################################

# defino una serie de funciones que utilizaré para la estética del output de la matriz

# función que me imprime los separadores entre filas
def imprimir_separador_horizontal():
    # Imprimir un renglón dependiendo de las columnas
    for _ in range(COLUMNAS+1):
        print("+---", end="")
    print("+")


# función que me imprime la fila de números del tablero (nums del 1 al 10)
def imprimir_fila_de_numeros():
    print("|   ", end="")
    for x in range(COLUMNAS):
        print(f"| {x+1} ", end="")
    print("|")

# funcion que me imprime la columna de números del tablero
def incrementar_letra(letra):
    return chr(ord(letra)+1)

# funcion que imprime la matriz

def imprimir_matriz(matriz, muestra_barcos, tipo = "mar"):
    """"
    Esta funcion pide como argumentos de entrada la matriz a printear
    y muestra_barcos un booleano que si es True nos muestra los valores (hay que perfeccionar para que sólo no nos muestre los barcos)
    y si es False lo pasa a vacío
    """
    print("Este es el", tipo, "del jugador: ")
    letra = "A"
    for y in range(FILAS):
        imprimir_separador_horizontal()
        print(f"| {letra} ", end="")
        for x in range(COLUMNAS):
            celda = matriz[y][x]
            valor_real = celda
            if (muestra_barcos == False):
                valor_real = " "
            print(f"| {valor_real} ", end="")
        letra = incrementar_letra(letra)
        print("|",)  # Salto de línea
    imprimir_separador_horizontal()
    imprimir_fila_de_numeros()
    imprimir_separador_horizontal()

##############################################
#########   Colocar barcos DONE    ########### 
##############################################
import random

# da aleatoriamente una coordenada columna
def x_aleatoria():
    return random.randint(0, COLUMNAS-1)

# da aleatoriamente una coordenada fila
def y_aleatoria():
    return random.randint(0, FILAS-1)

#da aleatoriamente la colocación 0 = horizontal / 1 = vertical
def z_aleatoria():
    return(random.randint(0,1))

#función que devuelve un booleano indicando si la coordenada está en rango
def coordenada_en_rango(y, x):
    return x >= 0 and x <= COLUMNAS-1 and y >= 0 and y <= FILAS-1

# FUNCIÓN QUE IDENTIFICA SI HAY MAR EN SU POSICIÓN Y ALREDEDOR #
def hay_mar_cerca(fila, columna, matriz):
    for incremento_columna in range(-1,2):
        for incremento_fila in range(-1,2):
            Pos1 = fila + incremento_fila
            Pos2 = columna + incremento_columna
            if (coordenada_en_rango(Pos1,Pos2) == True):
                if (matriz[Pos1,Pos2] == MAR):
                    continue
                else:
                    return False
            else:
                continue
    return True  


# lista que incluye las coordenadas de cada barco en otra sublista, las coordenadas son tuplas
lista_barcos = []

# Funcion que coloca los submarinos si hay mar cerca
def colocar_submarinos(n_submarinos,tablero):
    colocados = 0
    while colocados < n_submarinos:
        y = y_aleatoria()
        x = x_aleatoria()
        if (hay_mar_cerca(y,x,tablero) == True):
            tablero[y,x] = "S"
            lista_barcos.append(([(y,x)]))
            colocados += 1


# Funcion que coloca los barcos si hay mar cerca y no se sale del rango
def colocar_barcos(n_barcos,tablero):
    colocados = 0
    while colocados < n_barcos:
        y = y_aleatoria()
        x = x_aleatoria()
        z = z_aleatoria()
        if (hay_mar_cerca(y,x,tablero) == True):
            
            if (z == 0):
                if (hay_mar_cerca(y+1,x,tablero) == True):
                    if (coordenada_en_rango(y+1,x)):

                        tablero[y,x] = "B"
                        tablero[y+1,x] = "B"
                        lista_barcos.append([(y,x),(y+1,x)])
                    else:
                        continue
                else:
                    continue
            else:
                if (hay_mar_cerca(y,x+1,tablero) == True):
                    if (coordenada_en_rango(y,x+1)):

                        tablero[y,x] = "B"
                        tablero[y,x+1] = "B"
                        lista_barcos.append([(y,x),(y,x+1)])
                    else:
                        continue
                else:
                    continue                

            colocados += 1

# Funcion que coloca los navíos si hay mar cerca y no se sale del rango
def colocar_navios(n_navios,tablero):
    colocados = 0
    while colocados < n_navios:
        y = y_aleatoria()
        x = x_aleatoria()
        z = z_aleatoria()
        if (hay_mar_cerca(y,x,tablero) == True):
            
            if (z == 0):
                if (hay_mar_cerca(y+1,x,tablero) & hay_mar_cerca(y+2,x,tablero) == True):
                    if (coordenada_en_rango(y+1,x) & coordenada_en_rango(y+2,x)):

                        tablero[y,x] = "N"
                        tablero[y+1,x] = "N"
                        tablero[y+2,x] = "N"
                        lista_barcos.append([(y,x),(y+1,x),(y+2,x)])
                    else:
                        continue
                else:
                    continue
            else:
                if (hay_mar_cerca(y,x+1,tablero) & hay_mar_cerca(y,x+2,tablero) == True):
                    if (coordenada_en_rango(y,x+1) & coordenada_en_rango(y,x+2)):

                        tablero[y,x] = "N"
                        tablero[y,x+1] = "N"
                        tablero[y,x+2] = "N"
                        lista_barcos.append([(y,x),(y,x+1),(y,x+2)])
                    else:
                        continue
                else:
                    continue                

            colocados += 1

# Funcion que coloca el portaviones si hay mar cerca y no se sale del rango
def colocar_portaviones(n_portaviones,tablero):
    colocados = 0
    while colocados < n_portaviones:
        y = y_aleatoria()
        x = x_aleatoria()
        z = z_aleatoria()
        if (hay_mar_cerca(y,x,tablero) == True):
            
            if (z == 0):
                if (hay_mar_cerca(y+1,x,tablero) & hay_mar_cerca(y+2,x,tablero) & hay_mar_cerca(y+3,x,tablero) == True):
                    if (coordenada_en_rango(y+1,x) & coordenada_en_rango(y+2,x) & coordenada_en_rango(y+3,x)):

                        tablero[y,x] = "P"
                        tablero[y+1,x] = "P"
                        tablero[y+2,x] = "P"
                        tablero[y+3,x] = "P"
                        lista_barcos.append([(y,x),(y+1,x),(y+2,x),(y+3,x)])
                    else:
                        continue
                else:
                    continue
            else:
                if (hay_mar_cerca(y,x+1,tablero) & hay_mar_cerca(y,x+2,tablero) & hay_mar_cerca(y,x+3,tablero) == True):
                    if (coordenada_en_rango(y,x+1) & coordenada_en_rango(y,x+2) & coordenada_en_rango(y,x+3)):

                        tablero[y,x] = "P"
                        tablero[y,x+1] = "P"
                        tablero[y,x+2] = "P"
                        tablero[y,x+3] = "P"
                        lista_barcos.append([(y,x),(y,x+1),(y,x+2),(y,x+3)])

                    else:
                        continue
                else:
                    continue                

            colocados += 1


##############################################################################
#### FUNCIÓN QUE COMPRUEBA SI TODOS LOS ELEMENTOS DE UA LISTA SON IGUALES ####
##############################################################################

def chkList(lst): 
    if len(lst) < 0 : 
        res = True
    res = all(ele == lst[0] for ele in lst) 
      
    if(res): 
        return True 
    else: 
        return False


##########################################################
###### FUNCIÓN QUE IDENTIFICA LOS BARCOS HUNDIDOS ########
##########################################################

lista_barcos2 = lista_barcos

def barco_hundido(y,x):
    comp = (y,x)
    for i in range(len(lista_barcos)):
        for j in range(len(lista_barcos[i])):
            if(comp == lista_barcos[i][j]):
                lista_barcos2[i][j] = 'X'
                if(chkList(lista_barcos2[i])):
                    return print("HUNDIDO")
                else:
                    continue

#####################################################
# CODIGO QUE IDENTIFICA SI LA PARTIDA SE HA ACABADO #
#####################################################

########## FUNCIÓN hay_barcos() ###########   ¿¿¿¿¿¿la meto en la clase Tablero????
'''Esta función me devolverá True o False en función de si quedan o no barcos.
    Cuando estén todos los barcos hundidos la función será False y, por tanto, se romperá el bucle while que mantiene el juego activo'''
def hay_barcos(tablero):
    hundidos = np.array(tablero == "X")
    if tablero[hundidos].size == 20: # En el momento en que en el tablero de mira haya 20 tiros acertados, todos los barcos estarán hundidos
        return False
    return True
    ''' Los 20 aciertos vienen de:
                    - 4 submarinos
                    - 3 buques * 2 de eslora = 6
                    - 2 navíos * 3 de eslora = 6
                    - 1 portaviones * 4 de eslora = 4 '''

######################################################
############ NORMALIZACIÓN COORDENADAS ###############
######################################################

def coord_fila(fila):
    fila = fila.upper()
    letras_filas = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    if (fila in letras_filas):
        y = letras_filas.index(fila.upper())
        return y
    else:
        return "" 

def coord_columna(columna):
    if columna in range(1,COLUMNAS+1):
        x = columna - 1
        return x
    else:
        return ""

##################################################################################
### FUNCION QUE PIDE O PROPORCIONA LAS COORDENADAS EN FUNCIÓN DE QUIEN DISPARE ###
##################################################################################

def coordenadas_disparo(pto_mira,maquina):

    if maquina == True:
        y = y_aleatoria()
        x = x_aleatoria()
        while pto_mira[y,x] != MAR:
            y = y_aleatoria()
            x = y_aleatoria()
        return y,x
    else:
        fila = input("Introduce la posición de fila: ")
        columna = int(input("Introduce la posición de columna: "))
        y = coord_fila(fila)
        x = coord_columna(columna)
        return y,x


#######################################
########## FUNCIÓN DISPARO ############
#######################################


def disparo(tablero_disparado, pto_mira, punto_mira_jugador, tablero_del_jugador, maquina = False):

    y,x = coordenadas_disparo(pto_mira,maquina)

    if(y == "" or x==""):
        print("coordenadas invalidas")
        return disparo(tablero_disparado,pto_mira,punto_mira_jugador,tablero_del_jugador,maquina)

    elif pto_mira[y,x]=="X" or pto_mira[y,x]=="-":
        print("Tiro repetido. Pierde su turno")

    elif tablero_disparado[y,x]=="S":
        pto_mira[y,x] = "X"
        tablero_disparado[y,x]="X"
        print("TOCADO")
        imprimir_matriz(punto_mira_jugador, True, "pto mira")
        imprimir_matriz(tablero_del_jugador, True)
        barco_hundido(y,x)
        if hay_barcos(pto_mira):
            print("Por favor, dispare de nuevo")
            return disparo(tablero_disparado,pto_mira,punto_mira_jugador,tablero_del_jugador,maquina)
        else:
            print("Todos los barcos hundidos\n ¡¡¡FELICIDADES!!!\nHa ganado el juego")
    
    elif tablero_disparado[y,x]=="B":
        pto_mira[y,x] = "X"
        tablero_disparado[y,x]="X"
        print("TOCADO")
        imprimir_matriz(punto_mira_jugador, True, "pto mira")
        imprimir_matriz(tablero_del_jugador, True)
        barco_hundido(y,x)
        if hay_barcos(pto_mira):
            print("Por favor, dispare de nuevo")
            return disparo(tablero_disparado,pto_mira,punto_mira_jugador,tablero_del_jugador,maquina)
        else:
            print("Todos los barcos hundidos\n ¡¡¡FELICIDADES!!!\nHa ganado el juego")

        
    elif tablero_disparado[y,x]=="N":
        pto_mira[y,x] = "X"
        tablero_disparado[y,x]="X"
        print("TOCADO")
        imprimir_matriz(punto_mira_jugador, True, "pto mira")
        imprimir_matriz(tablero_del_jugador, True)        
        barco_hundido(y,x)
        if hay_barcos(pto_mira):
            print("Por favor, dispare de nuevo")
            return disparo(tablero_disparado,pto_mira,punto_mira_jugador,tablero_del_jugador,maquina)
        else:
            print("Todos los barcos hundidos\n ¡¡¡FELICIDADES!!!\nHa ganado el juego")

    
    elif tablero_disparado[y,x]=="P":
        pto_mira[y,x] = "X"
        tablero_disparado[y,x]="X"
        print("TOCADO")
        imprimir_matriz(punto_mira_jugador, True, "pto mira")
        imprimir_matriz(tablero_del_jugador, True)        
        barco_hundido(y,x)
        if hay_barcos(pto_mira):
            print("Por favor, dispare de nuevo")
            return disparo(tablero_disparado,pto_mira,punto_mira_jugador,tablero_del_jugador,maquina)
        else:
            print("Todos los barcos hundidos\n ¡¡¡FELICIDADES!!!\nHa ganado el juego")
        
    elif tablero_disparado[y,x]==" ":
        pto_mira[y,x] = "-"
        tablero_disparado[y,x]="-"
        print("¡AGUA!. Pierde su turno")
        imprimir_matriz(punto_mira_jugador, True, "pto mira")
        imprimir_matriz(tablero_del_jugador, True)        

####################################
### FUNCIÓN CREADORA DE TABLEROS ###
####################################

def crear_tab():
    tablero = np.full((FILAS,COLUMNAS), MAR)
    return(tablero)


####################################################
########### CODIGO PARA JUGAR PARTIDA ##############
####################################################

def Jugar_Partida():
    
    #Defino los tableros
    tablero_jugador = crear_tab()
    tablero_maquina = crear_tab()
    punto_mira_jugador = crear_tab()
    punto_mira_maquina = crear_tab()

    #Coloco los barcos del jugador
    colocar_submarinos(n_submarinos,tablero_jugador)
    colocar_barcos(n_barcos,tablero_jugador)
    colocar_navios(n_navios,tablero_jugador)
    colocar_portaviones(n_portaviones,tablero_jugador)

    #Coloco los barcos de la maquina
    colocar_submarinos(n_submarinos,tablero_maquina)
    colocar_barcos(n_barcos,tablero_maquina)
    colocar_navios(n_navios,tablero_maquina)
    colocar_portaviones(n_portaviones,tablero_maquina)

    #imprimo el tablero y el punto de mira del jugador
    imprimir_matriz(punto_mira_jugador, True, "pto mira")
    imprimir_matriz(tablero_jugador, True)

    #Sorteo quien realiza el primer disparo
    aleat = z_aleatoria()

    #Defino las condiciones de para del bucle
    quedan_barcos_pto_maquina = hay_barcos(punto_mira_maquina)

    quedan_barcos_pto_jugador = hay_barcos(punto_mira_jugador)

    #comienza el bucle
    while (quedan_barcos_pto_maquina  == True & quedan_barcos_pto_jugador == True):

        #caso en el que sorteo es 0 (comenzará disparando el jugador)
        if(aleat == 0):
            disparo(tablero_maquina, punto_mira_jugador, punto_mira_jugador, tablero_jugador) # jugador
            quedan_barcos_pto_jugador = hay_barcos(punto_mira_jugador)
            if(quedan_barcos_pto_jugador == False):
                break
            disparo(tablero_jugador, punto_mira_maquina, punto_mira_jugador, tablero_jugador, True) # maquina
            quedan_barcos_pto_maquina = hay_barcos(punto_mira_maquina)
            if(quedan_barcos_pto_maquina == False):
                break
        #caso en el que sorteo es 1 (comenzará disparando la máquina)
        else:
            disparo(tablero_jugador, punto_mira_maquina, punto_mira_jugador, tablero_jugador, True) # maquina
            quedan_barcos_pto_maquina = hay_barcos(punto_mira_maquina)
            if(quedan_barcos_pto_maquina == False):
                break
            disparo(tablero_maquina, punto_mira_jugador, punto_mira_jugador, tablero_jugador) # jugador
            quedan_barcos_pto_jugador = hay_barcos(punto_mira_jugador)
            if(quedan_barcos_pto_maquina == False):
                break            

    #Condición para indicar el ganador de la partida
    if (quedan_barcos_pto_maquina  == False):
        ganador = "maquina"
    else:
        ganador = "jugador"
        

    print ("Fin de la partida, Ha ganado", ganador) 

#####################
# COMIENZA EL JUEGO #
#####################

Jugar_Partida()        