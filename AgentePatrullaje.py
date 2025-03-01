#importamos la libreria random para seleccion de forma aleatoria
import random

# lista de coordenadas para el patrullaje
ruta = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (2, 2), (1, 2), (0, 2)]

# Definir la posición inicial del agente
posicion_agente = (0, 0) 

# Definir una función para detectar obstáculos
def detectar_obstaculo(posicion):
    # Simulamos la detección de obstáculos de manera aleatoria
    return random.random() < 0.2  # 20% de probabilidad de encontrar un obstáculo (esta puede cambiar)

# Definir una función para cambiar la dirección de manera aleatoria
def cambiar_direccion(posicion_actual, ruta):
    # Elegir una nueva dirección aleatoria que no sea la posición actual
    nueva_posicion = random.choice(ruta)
    while nueva_posicion == posicion_actual: #ciclo while para que se mueva a una posicion diferente en donde no encuentre obstaculo
        nueva_posicion = random.choice(ruta)
    return nueva_posicion

# Función principal para patrullar
def patrullar(ruta):
    global posicion_agente
    indice_ruta = 0

    while True:
        # Obtener la siguiente posición en la ruta
        siguiente_posicion = ruta[indice_ruta]

        # Mostrar la posición actual del agente
        print(f"Agente en posición: {posicion_agente}")

        # Detectar si hay un obstáculo en la siguiente posición
        if detectar_obstaculo(siguiente_posicion):
            print("¡Obstáculo detectado cuidado!!! Cambiando dirección...")
            posicion_agente = cambiar_direccion(posicion_agente, ruta)
            indice_ruta = ruta.index(posicion_agente)
        else:
            # Mover al agente a la siguiente posición
            posicion_agente = siguiente_posicion
            indice_ruta = (indice_ruta + 1) % len(ruta) # apunta a la siguiente posicion de la ruta

        # Simular un pequeño retraso para visualizar el movimiento
        import time
        time.sleep(1)

# Iniciar la patrulla
patrullar(ruta)