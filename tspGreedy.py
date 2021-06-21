

def greedy_search(current_node, distance_matriz: list):
    """
        This algorithm searches for the best solution using Greedy Search
    """
    result = [current_node]

    while len(result) != len(distance_matriz):
        neighbour_found = False
        for i in range(1, len(distance_matriz)):
            current_dist = sorted(distance_matriz[current_node])[i]

            for index, dist in enumerate(distance_matriz[current_node]):
                if dist == current_dist and index not in result:
                    neighbour = index
                    result.append(neighbour)
                    current_node = neighbour
                    neighbour_found = True
                    break

            if neighbour_found:
                break

    return result
