import heapq

def encontrar_mejor_ruta(recompensas, inicio, objetivo):
    filas, columnas = len(recompensas), len(recompensas[0])
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Arriba, Abajo, Izquierda, Derecha
    
    prioridad = [(-recompensas[inicio[0]][inicio[1]], inicio, [inicio])]
    visitados = set()
    
    while prioridad:
        utilidad, (x, y), camino = heapq.heappop(prioridad)
        utilidad = -utilidad  # Convertimos a positivo
        
        if (x, y) in visitados:
            continue
        visitados.add((x, y))
        
        if (x, y) == objetivo:
            return camino, utilidad
        
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and (nx, ny) not in visitados:
                nueva_utilidad = utilidad + recompensas[nx][ny]
                heapq.heappush(prioridad, (-nueva_utilidad, (nx, ny), camino + [(nx, ny)]))
    
    return None, 0  # Si no se encuentra camino

# Ejemplo de entorno con recompensas
tabla_recompensas = [
    [0,  1,  4,  2],
    [3, -1,  2,  1],
    [4,  2,  1,  3],
    [2,  3,  5,  9]
]

inicio = (0, 0)
objetivo = (3, 3)

mejor_ruta, utilidad_maxima = encontrar_mejor_ruta(tabla_recompensas, inicio, objetivo)

print("Mejor ruta encontrada:", mejor_ruta)
print("Utilidad máxima:", utilidad_maxima)