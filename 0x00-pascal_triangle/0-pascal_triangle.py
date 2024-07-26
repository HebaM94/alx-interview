#!/usr/bin/python3
"""
Pascal's triangle module
"""


def pascal_triangle(n):
    """ Pascal's triangle generator using addition
        Args:
           n (int): levels of pascal triangle
        Return:
            Integer list of list representing pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[i - 1]
        new = [1]
        for j in range(1, i):
            new.append(prev[j - 1] + prev[j])
        new.append(1)
        triangle.append(new)
    return triangle
