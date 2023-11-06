#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        j = 0
        for j in range(len(matrix[0])):
            print("{} ".format(matrix[i][j]), end='')
        print()
