"""
Algoritmo responsavel por fazer Busca Gulosa
"""
import random
import math


def busca_gulosa(node_atual, distance_matriz: list):
    result = [node_atual]

    while len(result) != len(distance_matriz):
        found = False
        for i in range(1, len(distance_matriz)):
            actual_dist = sorted(distance_matriz[node_atual])[i]

            for index, dist in enumerate(distance_matriz[node_atual]):
                if dist == actual_dist and index not in result:
                    vizinho = index
                    result.append(vizinho)
                    node_atual = vizinho
                    found = True
                    break

            if found:
                break

    return result
