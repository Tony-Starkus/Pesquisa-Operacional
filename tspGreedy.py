"""
Algoritmo responsavel por fazer Busca Gulosa
"""
import random
import math


def busca_gulosa(node_atual, distance_matriz: list):
    result = [node_atual]
    # distance_matriz_aux = distance_matriz
    while len(result) != len(distance_matriz):
        # print(sorted(distance_matriz[node_atual]))
        # exit(1)
        # verificação para não adicionar nós já visitados no result
        # print(f"node_atual: {node_atual}")
        found = False
        for i in range(1, len(distance_matriz)):
            # get dist per dist in the sorted list of distances in actual node
            # print(distance_matriz[node_atual])
            actual_dist = sorted(distance_matriz[node_atual])[i]
            # print(f"actual_dist: {actual_dist}")

            for index, dist in enumerate(distance_matriz[node_atual]):
                if dist == actual_dist and index not in result:
                    vizinho = index
                    # print(index)
                    result.append(vizinho)
                    node_atual = vizinho
                    found = True
                    break

            if found:
                break

            """if i != 0 and distance_matriz[node_atual].index(sorted(distance_matriz[node_atual])[i]) not in result:
                min_dist = sorted(distance_matriz[node_atual])[i]
                aux = sorted(distance_matriz[node_atual])
                print(aux)
                exit(1)
                vizinho = distance_matriz[node_atual].index(sorted(distance_matriz[node_atual])[i])
                break"""

        """for i in range(len(distance_matriz)):
            if i not in result:
                menor_dist = sorted(distance_matriz[node_atual])[i]
                vizinho = distance_matriz[node_atual].index(menor_dist)"""
        #print(aux)
        # print(distance_matriz[node_atual])
        # print(nodes[vizinho])
        # print(menor_dist, vizinho)
        # result.append(vizinho)
        # node_atual = vizinho
        # exit(1)
    print(len(result))
    print(f"result={result}")
    return result
