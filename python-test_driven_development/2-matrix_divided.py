#!/usr/bin/python3
"""Divide all elements of a matrix by a given divisor
    matrix (list of lists): The matrix to be divided
    div (int or float): The divisor for the division
    Return new matrix or raise Exception"""


def matrix_divided(matrix, div):
    if not all(
            isinstance(row, list) and all(
                isinstance(num, (int, float)) for num in row
                ) for row in matrix
            ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(num / div, 2) for num in row] for row in matrix]

    return result
