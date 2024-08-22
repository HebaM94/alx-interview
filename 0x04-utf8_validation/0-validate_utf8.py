#!/usr/bin/python3
"""
UTF8 validation module
"""

def validUTF8(data):
    """
    Validates if data consists of
    valid utf-8 encoded characters
    """
    num_bytes = 0
    for byte in data:
        byte = byte & 0xFF
        if num_bytes:
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1
            continue
        while (1 << abs(7 - num_bytes)) & byte:
            num_bytes += 1
        if num_bytes == 1 or num_bytes > 4:
            return False
        num_bytes = max(num_bytes - 1, 0)
    return num_bytes == 0

