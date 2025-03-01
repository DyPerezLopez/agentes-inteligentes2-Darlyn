# importa una calse del modulo de python implementa BFS para procesar nodos en orden 
from collections import deque

# Definir el laberinto (0 = camino libre, 1 = pared, 'M' = meta)
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 'M']
]

# Tamaño del laberinto (matriz 5x5)
FILAS = 5
COLUMNAS = 5

# Posición inicial del agente
inicio = (0, 0)

# Movimientos posibles (arriba, abajo, izquierda, derecha)
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para encontrar la ruta más corta usando BFS
def encontrar_ruta(laberinto, inicio):
    fila_inicio, columna_inicio = inicio
    cola = deque()  # Cola para BFS
    cola.append((fila_inicio, columna_inicio, []))  # (fila, columna, ruta)

    visitados = set()  # Conjunto para almacenar posiciones visitadas
    visitados.add((fila_inicio, columna_inicio))

    while cola:
        fila, columna, ruta = cola.popleft()

        # Verificar si llegamos a la meta
        if laberinto[fila][columna] == 'M':
            return ruta + [(fila, columna)]  # Devolver la ruta completa

        # Explorar movimientos posibles
        for movimiento in movimientos:
            nueva_fila = fila + movimiento[0]
            nueva_columna = columna + movimiento[1]

            # Verificar si el movimiento es válido
            if 0 <= nueva_fila < FILAS and 0 <= nueva_columna < COLUMNAS:
                if (nueva_fila, nueva_columna) not in visitados and laberinto[nueva_fila][nueva_columna] != 1:
                    visitados.add((nueva_fila, nueva_columna))
                    cola.append((nueva_fila, nueva_columna, ruta + [(fila, columna)]))

    return None  # Si no se encuentra la meta

# Función para mostrar el laberinto con la ruta
def mostrar_laberinto_con_ruta(laberinto, ruta):
    for i in range(FILAS):
        for j in range(COLUMNAS):
            if (i, j) in ruta:
                print("A", end=" ")  # Mostrar el camino del agente
            else:
                print(laberinto[i][j], end=" ")
        print()

# Encontrar la ruta más corta
ruta = encontrar_ruta(laberinto, inicio)

# Mostrar resultados
if ruta:
    print("Ruta encontrada:")
    mostrar_laberinto_con_ruta(laberinto, ruta)
    print("\nCoordenadas de la ruta:")
    for paso in ruta:
        print(paso)
else:
    print("No se encontró una ruta válida.")