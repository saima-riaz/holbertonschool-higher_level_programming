#!/usr/bin/python3
"""Divide all elements of a matrix by a given divisor
    matrix (list of lists): The matrix to be divided
    div (int or float): The divisor for the division
    Return new matrix or raise Exception"""


def matrix_divided(matrix, div):
    """ validation div """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    """ validation matrix """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")
    lenrow = len(matrix[0])
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")
        if len(row) != lenrow:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    """ create new matrix """
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
