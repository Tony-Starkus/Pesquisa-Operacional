import sys
from math import sqrt


def calculate_tour_distance(tour):
    pass


def euc_2d(values: list):
    """for i in range(len(values)):
        for j in range(len(values)):
            xd = values[i][0] - values[j][0]
            xd = values[i][1] - values[j][1]
            dist = sqrt(xd * xd + yd * yd)
            dis
            print(values[i][0])
            print(values[j][1])"""
    for x1, y1 in values:
        row = []
        for x2, y2 in values:
            xd = x1 - x2
            yd = y1 - y2
            dist = sqrt(xd*xd + yd*yd)
            row.append(dist + 0.5)
        distanceMatriz.append(row)
    print(len(distanceMatriz))


def att(values: list):
    for x1, y1 in values:
        row = []
        for x2, y2 in values:
            xd = x1 - x2
            yd = y1 - y2
            dist = sqrt(xd*xd + yd*yd)
            row.append(dist + 0.000000001)
        distanceMatriz.append(row)
    print(len(distanceMatriz))


def ceil_2d(values: list):
    for x1, y1 in values:
        row = []
        for x2, y2 in values:
            xd = x1 - x2
            yd = y1 - y2
            dist = sqrt(xd*xd + yd*yd) / 10.0
            row.append(dist + 0.5)
        distanceMatriz.append(row)
    print(len(distanceMatriz))


distanceMatriz = list()
size = -1
pos = 0


def main(input_file_path):
    tour = list()
    _type = list()
    #if arg < 2:
     #   print(f"asddwdw")
      #  exit(1)
    s = list()

    print("asadwdw")
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
            print(f"file_name={file_name}\n"
                  f"file_comment={file_comment}\n"
                  f"file_type={file_type}\n"
                  f"file_dimension={file_dimension}\n"
                  f"file_edge_weight_type={file_edge_weight_type}")

            # VALIDATIONS
            # Check if instance is valid
            if file_edge_weight_type not in ("EUC_2D", "ATT", "CEIL_2D"):
                print(f"Error: Can't calculate using {file_edge_weight_type}. Use = {('EUC_2D', 'ATT', 'CEIL_2D')}")
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
                coord = tuple((float(split_line[1].strip()), float(split_line[2].strip())))
                nodes.append(node)
                values.append(coord)
                # print(f"node={node} coord={coord}")

            if file_edge_weight_type == "EUC_2D":
                print("a")
                euc_2d(values)
            elif file_edge_weight_type == "CEIL_2D":
                print("b")
                ceil_2d(values)
            elif file_edge_weight_type == "ATT":
                print("c")
                att(values)

            tour = [i for i in range(len(values))]
            print(len(tour))

        except IOError:
            print(f"O arquivo {input_file_path} não existe")


file1 = "./tsp/tsp225.tsp"  # EUC_2D
file2 = "./tsp/dsj1000ceil.tsp"  # CEIL_2D
file3 = "./tsp/att48.tsp"  # ATT

main(file2)
