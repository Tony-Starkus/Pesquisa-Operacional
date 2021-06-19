import random
import math
import sys


def calculate_tour_distance(tour, file_dimension, distance_matriz):
    dist = 0
    """print(distanceMatriz[0][5])"""

    for i in range(file_dimension - 1):
        dist += distance_matriz[tour[i]][tour[i + 1]]
    dist += distance_matriz[tour[file_dimension - 1]][tour[0]]
    print(f"Comprimento da rota: {dist}")
    return dist


melhor_tour = list()


def simulated_annealing(distance_matriz: list, greed_tour: list, greed_dist):
    """
    Este algoritmo procura a melhor solução usando Annealing.
    estado_inicial: 
    """
    fila = greed_tour
    temp_inicial = 100
    temp_final = 3
    temp_atual = temp_inicial
    resfriamento = 1

    melhor_distancia = greed_dist

    while temp_atual > temp_final:
        # print(melhor_distancia)
        val1, val2 = [random.randrange(len(greed_tour)) for x in range(2)]
        while val2 == val1:
            val2 = random.randrange(len(greed_tour))

        old_val1 = fila[val1]
        fila[val1] = fila[val2]
        fila[val2] = old_val1

        dist = calculate_tour_distance(fila, len(greed_tour), distance_matriz)

        if dist < greed_dist or random.uniform(0, 1) < math.exp(dist / temp_atual):
            global melhor_tour
            melhor_distancia = dist
            melhor_tour = fila

        if greed_dist < melhor_distancia:
            print("a")
            melhor_tour = greed_tour

        temp_atual -= resfriamento

        """if distance_matriz[estado_atual][vizinho] < melhor_distancia:
            melhor_distancia = distance_matriz[estado_atual][vizinho]
            solucao = vizinho
        else:
            if random.uniform(0, 1) > math.exp(-distance_matriz[estado_atual][vizinho] / temp_atual):
                melhor_distancia = distance_matriz[estado_atual][vizinho]
                solucao = vizinho
        # decrement the temperature"""

    return melhor_tour, melhor_distancia


def get_custo(state, distanceMatriz):
    """Calculates cost of the argument state for your solution."""
    raise NotImplementedError


def get_vizinhos(state, distanceMatriz):
    """Returns neighbors of the argument state for your solution."""
    raise NotImplementedError
