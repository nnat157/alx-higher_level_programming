#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

    new_matrix = []
    for element in matrix:
        new_element = list(map(lambda x: x ** 2, element))
        new_matrix.append(new_element)

    return new_matrix
