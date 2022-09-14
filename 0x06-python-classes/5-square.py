#!/usr/bin/python3
"Define a Square"


class Square:
    "this is a square"
    def __init__(self, size=0):
        "Instantiation of the Square"
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        "returns the current square area"
        return self.__size ** 2

    @property
    def size(self):
        "Value of Size"
        return self.__size

    @size.setter
    def size(self, value):
        "Set size value of square"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        elif isinstance(value, int):
            self.__size = value

    def my_print(self):
        "Print in stdout the square with the character #."
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
