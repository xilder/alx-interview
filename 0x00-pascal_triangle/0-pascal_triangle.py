#!/usr/bin/python3
"""pascal"""
def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the first n rows of Pascal's triangle.
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)

    return triangle