#!/usr/bin/python3
"Defive the Square"


class Square:
    "This is a Square"
    def __init__(self, size=0):
        "Instantiate the Square"
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        "Get the value of current size of the square"
        return self.__size

    @size.setter
    def size(self, value):
        "set the value of the square"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(value, int):
            self.__size = value
