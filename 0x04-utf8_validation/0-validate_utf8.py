#!/usr/bin/python3
"""utf8 validation algorithm"""


def validUTF8(data):
    """utf8 validation algorithm"""
    length = 0
    for b in data:
        b = b & 0b11111111
        if length == 0:
            if b >> 7 == 0:
                continue
            elif b >> 5 == 6:
                length = 2
            elif b >> 4 == 14:
                length = 3
            elif b >> 3 == 30:
                length = 4
        else:
            if b >> 6 != 2:
                return False
            length -= 1
    return length == 0
