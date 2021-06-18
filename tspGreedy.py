"""
Algoritmo responsavel por fazer Busca Gulosa
"""
import random
import math

def busca_gulosa(node_atual, distance_matriz, nodes):
    result = [node_atual]
   # distance_matriz_aux = distance_matriz
    while len(result) != len(distance_matriz):
       # distance_matriz[node_atual].pop(node_atual)
        menor_dist = sorted(distance_matriz[node_atual])[1]
        vizinho = distance_matriz[node_atual].index(menor_dist)

        print(nodes[vizinho])
        print(menor_dist, vizinho)
        exit(1)

        if vizinho in result:
            continue
        else:
            result.append(vizinho)            
    
    print(result)
