
#importamos libreria random 
import random

# Definir el tamaño de la cuadrícula (debido que son 5x5 puede cambiar si quisieramos)
FILAS = 5
COLUMNAS = 5

# Crear una matriz para representar el programa
entorno = [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)] #crea unaa lista de filas y columnas

# Posición inicial del agente iniciando 0, 0
posicion_agente = (0, 0)

# almacena las posiciones visitadas para que ya no las pase
visitadas = set()

# Función para mover al agente
def mover_agente(posicion_actual, entorno, visitadas):
    fila, columna = posicion_actual
    movimientos_posibles = []

    # Definir movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

    for movimiento in movimientos:
        nueva_fila = fila + movimiento[0]
        nueva_columna = columna + movimiento[1]

        # Verificar si el movimiento es válido y no ha sido visitado
        if 0 <= nueva_fila < FILAS and 0 <= nueva_columna < COLUMNAS:
            if (nueva_fila, nueva_columna) not in visitadas:
                movimientos_posibles.append((nueva_fila, nueva_columna))

    # Elegir un movimiento aleatorio entre los posibles
    if movimientos_posibles:
        nueva_posicion = random.choice(movimientos_posibles)
        return nueva_posicion
    else:
        return None  # No hay movimientos posibles

# Función principal para explorar el entorno
def explorar_entorno(entorno, posicion_inicial):
    posicion_agente = posicion_inicial
    visitadas.add(posicion_agente)

    while True:
        # Marcar la posición actual como visitada
        fila, columna = posicion_agente
        entorno[fila][columna] = 1

        # Mostrar el entorno
        for fila in entorno:
            print(fila)
        print()

        # Mover al agente
        nueva_posicion = mover_agente(posicion_agente, entorno, visitadas)

        if nueva_posicion:
            posicion_agente = nueva_posicion
            visitadas.add(posicion_agente)
        else:
            print("No hay más áreas nuevas para explorar.")
            break

        # Simular un pequeño retraso para visualizar el movimiento
        import time
        time.sleep(1)

# Iniciar la exploración
explorar_entorno(entorno, posicion_agente)