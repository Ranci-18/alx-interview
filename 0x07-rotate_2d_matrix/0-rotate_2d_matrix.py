#!/usr/bin/python3
"""Rotate 2D Matrix module"""


def rotate_2d_matrix(matrix):
    """function that rotates a matrix
    90 degrees clockwise in place"""
    # first transpose the matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # then reverse each row
    for row in matrix:
        row.reverse()
