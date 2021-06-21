""" 
    Algoritmo desenvolvido para a atividade de Pesquisa Operacional 
    no curso de Bacharelado em Sistemas de Informação
    na universidade Federal do Acre.

    Docente: Prof. Dr. Olacir Rodrigues Castro Júnior

    Autor 1: Thalisson Bandeira Araújo
    Autor 2: Evandro Cavalcante de Araújo Júnior

    Rio Branco - Acre       20/06/2021
"""
import sys
from math import sqrt
from SimulatedAnnealing import simulated_annealing
from tspGreedy import greedy_search

distanceMatriz = list()
size = -1
pos = 0
best_node = None
best_tour = []


def calculate_tour_distance(tour, file_dimension):
    """
        This function calculates the provided tour distance.
    """
    dist = 0

    for i in range(file_dimension - 1):
        dist += distanceMatriz[tour[i]][tour[i + 1]]
    dist += distanceMatriz[tour[file_dimension - 1]][tour[0]]
    
    return dist


def euc_2d(values: list):
    """
        This function calculates the distance between the nodes using euclidean distance.
    """
    for x1, y1 in values:
        row = []
        for x2, y2 in values:
            xd = x1 - x2
            yd = y1 - y2
            dist = sqrt((xd * xd) + (yd * yd))
            row.append(int(dist + 0.5))
        distanceMatriz.append(row)


def att(values: list):
    """
        This function calculates the distance between the nodes using ATT.
    """
    for x1, y1 in values:
        row = []
        for x2, y2 in values:
            xd = x1 - x2
            yd = y1 - y2
            dist = sqrt(xd*xd + yd*yd)
            row.append(int(dist + 0.000000001))
        distanceMatriz.append(row)


def ceil_2d(values: list):
    """
        This function calculates the distance between the nodes using CEIL.
    """
    for x1, y1 in values:
        row = []
        for x2, y2 in values:
            xd = x1 - x2
            yd = y1 - y2
            dist = sqrt(xd*xd + yd*yd) / 10.0
            row.append(int(dist + 0.5))
        distanceMatriz.append(row)


def main(input_file_path):
    tour = list()
    _type = list()
    s = list()

    with open(input_file_path) as input_file:
        try:
            # get lines
            lines = input_file.readlines()

            # get infos
            file_name = lines[0].split(" ")[2].strip()
            file_comment = lines[1].split(":")[1].strip()
            file_type = lines[2].split(" ")[2].strip()
            file_dimension = int(lines[3].split(" ")[2])
            file_edge_weight_type = lines[4].split(" ")[2].strip()
            print(f"Header:\n"
                  f"file name = {file_name}\n"
                  f"file comment = {file_comment}\n"
                  f"file type = {file_type}\n"
                  f"file dimension = {file_dimension}\n"
                  f"file edge weight type = {file_edge_weight_type}")

            # VALIDATIONS
            # Check if instance is valid
            if file_edge_weight_type not in ("EUC_2D", "ATT", "CEIL_2D"):
                print(
                    f"Error: Can't calculate using {file_edge_weight_type}. Use = {('EUC_2D', 'ATT', 'CEIL_2D')}")
                exit(1)

            # Check if file is type TSP
            if file_type != "TSP":
                print(f"Error: file is not of type TSP")
                exit(1)

            # END VALIDATIONS

            nodes = list()
            values = list()
            # read line per line
            for line in lines[6:]:
                # End of File
                if line.strip() == 'EOF':
                    break

                split_line = line.strip().split(" ")
                node = int(split_line[0])
                coord = tuple(
                    (float(split_line[1].strip()), float(split_line[2].strip())))
                nodes.append(node)
                values.append(coord)

            if file_edge_weight_type == "EUC_2D":
                euc_2d(values)
            elif file_edge_weight_type == "CEIL_2D":
                ceil_2d(values)
            elif file_edge_weight_type == "ATT":
                att(values)

            best_dist = sys.maxsize

            # Searching the best tour using tspGreedy
            for i in range(len(nodes)):
                #print(i)
                tour = greedy_search(i, distanceMatriz)
                dist = calculate_tour_distance(tour, file_dimension)
                if dist < best_dist:
                    best_dist = dist
                    global best_node
                    global best_tour
                    best_node = i
                    best_tour = tour

            # Printing the best distance and tour of Greedy Search algorithm
            print("\nGreedy: ")
            print(f"best greedy tour = {best_tour}")
            print(f"best greedy dist = {best_dist}")
    
            sa_best_tour, sa_best_dist = simulated_annealing(distanceMatriz, best_tour, greedy_dist=best_dist)

            # Printing the best distance and tour of Simulated Annealing algorithm
            print("\nSimmulated Annealing: ")
            print(f"best SA tour = {sa_best_tour}")
            print(f"best SA dist = {sa_best_dist}")

        except IOError:
            print(f"O arquivo {input_file_path} não existe")


file1 = "./tsp/eil51.tsp"  # EUC_2D
file2 = "./tsp/dsj1000ceil.tsp"  # CEIL_2D
file3 = "./tsp/att48.tsp"  # ATT

main(file1)
