#!/usr/bin/python3
"""
Generates Pascal's triangle up to the nth row.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.
    Args:
        n (int): The number of rows in the Pascal's triangle.
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        row = []
        coefficient = 1
        for j in range(i + 1):
            row.append(coefficient)
            coefficient = coefficient * (i - j) // (j + 1)
        triangle.append(row)

    return triangle
