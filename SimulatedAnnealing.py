import random
import math
import sys


def simulated_annealing(estado_inicial: int, distanceMatriz: list):
    """
    Este algoritmo procura a melhor solução usando Annealing.
    estado_inicial: 
    """
    temp_inicial = 100
    temp_final = 1
    temp_atual = temp_inicial
    resfriamento = 0.1

    estado_atual = estado_inicial  # 0
    solucao = estado_atual
    melhor_distancia = sys.maxsize

    while temp_atual > temp_final:
        # print(melhor_distancia)
        vizinho = random.randrange(len(distanceMatriz))
        # print(vizinho)

        if distanceMatriz[estado_atual][vizinho] < melhor_distancia:
            melhor_distancia = distanceMatriz[estado_atual][vizinho]
            solucao = vizinho
        else:
            if random.uniform(0, 1) > math.exp(-distanceMatriz[estado_atual][vizinho] / temp_atual):
                melhor_distancia = distanceMatriz[estado_atual][vizinho]
                solucao = vizinho
        # decrement the temperature
        temp_atual -= resfriamento

    return solucao

def get_custo(state, distanceMatriz):
    """Calculates cost of the argument state for your solution."""
    raise NotImplementedError
    
def get_vizinhos(state, distanceMatriz):
    """Returns neighbors of the argument state for your solution."""
    raise NotImplementedError