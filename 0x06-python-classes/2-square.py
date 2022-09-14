#!/usr/bin/python3
"""Define a Square by size"""


class Square:
    """This ia a Square"""
    def __init__(self, size=0):
        """Instantaite the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
