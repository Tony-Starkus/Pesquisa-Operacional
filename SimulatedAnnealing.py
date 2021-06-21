import random
import math


def calculate_tour_distance(tour, file_dimension, distance_matriz):
    dist = 0

    for i in range(file_dimension - 1):
        dist += distance_matriz[tour[i]][tour[i + 1]]
    dist += distance_matriz[tour[file_dimension - 1]][tour[0]]
    return dist


def simulated_annealing(distance_matriz: list, greedy_tour: list, greedy_dist):
    """
        This algorithm searches for the best solution using a simulated annealing.
    """
    queue = greedy_tour
    initial_temp = 100
    final_temp = 1
    current_temp = initial_temp
    cooling = 0.1

    tour_S = greedy_tour
    dist_S = greedy_dist

    best_tour = tour_S
    best_dist = greedy_dist

    tour_R = greedy_tour

    while current_temp > final_temp:
        val1, val2 = [random.randrange(len(tour_R)) for x in range(2)]
        
        while val2 == val1:
            val2 = random.randrange(len(tour_R))

        old_val1 = tour_R[val1]
        tour_R[val1] = tour_R[val2]
        tour_R[val2] = old_val1
        
        dist_R = calculate_tour_distance(tour_R, len(tour_R), distance_matriz)
        
        if dist_R < dist_S or random.uniform(0, 1) < math.exp((dist_S - dist_R)/current_temp):
            dist_S = dist_R
            tour_S =  tour_R

        if dist_S < best_dist:
            best_tour = tour_S
            best_dist = dist_S

        else:
            old_val1 = tour_R[val1]
            tour_R[val1] = tour_R[val2]
            tour_R[val2] = old_val1

        current_temp -= cooling

    return best_tour, best_dist
