#!/usr/bin/python3
"""rotate a 2d matrix module"""
from typing import List


def rotate_2d_matrix(matrix: List[List[int]]):
    """rotate 2d matrix"""
    N = len(matrix)
    new_m = []
    for row in matrix:
        if type(row) != list:
            raise TypeError

    for i in range(N):
        row = []
        for j in range(N - 1, -1, -1):
            row.append(matrix[j][i])
        new_m.append(row)
    for i in range(N):
        for j in range(N):
            matrix[i][j] = new_m[i][j]
