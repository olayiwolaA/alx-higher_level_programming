#!/usr/bin/python3
"Define The Square"


class Square:
    "This is a Square"
    def __init__(self, size=0):
        self.__size = size
        "Instamtiate the Square"
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        "method:returns the current square area"
        return self.__size ** 2
