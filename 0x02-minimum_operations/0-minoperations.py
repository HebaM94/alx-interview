#!/usr/bin/python3
""" Minimum operations"""


def minOperations(n: int) -> int:
    """ Finds the minimum operations needed
        to result in exactly nH characters in
        a file
        Args:
            n (int): The number of H characters
        Returns:
            Number of minimum operations needed or
            0 if impossible
    """
    char = 1
    needed_chars = n - 1
    copied_chars = 0
    ops = 0

    while (needed_chars > 0):
        if copied_chars and needed_chars % char:
            ops += 1
        else:
            copied_chars = char
            ops += 2
        char += copied_chars
        needed_chars -= copied_chars
    return ops
