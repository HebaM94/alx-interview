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
    pascal_tri = [[1]]
    for i in range(1, n):
        p_row = pascal_tri[i - 1]
        n_row = [1]
        for j in range(1, i):
            n_row.append(p_row[j - 1] + p_row[j])
        n_row.append(1)
        pascal_tri.append(n_row)
    return pascal_tri
