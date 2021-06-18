"""
Algoritmo responsavel por fazer Busca Gulosa
"""
import random
import math


def busca_gulosa(node_atual, distance_matriz: list, nodes):
    result = [node_atual]
    # distance_matriz_aux = distance_matriz
    while len(result) != len(distance_matriz):
        print(sorted(distance_matriz[node_atual]))
        exit(1)
        for i in range(1, len(distance_matriz)):
            if i != 0 and distance_matriz[node_atual].index(sorted(distance_matriz[node_atual])[i]) not in result:
                aux = sorted(distance_matriz[node_atual])[i]

        for i in range(len(distance_matriz)):
            if i not in result:
                menor_dist = sorted(distance_matriz[node_atual])[i]
                vizinho = distance_matriz[node_atual].index(menor_dist)

        # print(distance_matriz[node_atual])
        # print(nodes[vizinho])
        # print(menor_dist, vizinho)
        result.append(vizinho)
        node_atual = vizinho
        # exit(1)
    
    print(result)
