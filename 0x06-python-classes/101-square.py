#!/usr/bin/python3
"Define class Square"


class Square:
    "This represent a Square"
    def __init__(self, size=0, position=(0, 0)):
        "instantiaton of the Square"
        self.__size = size
        self.__position = position
        if type(self.__position) != tuple or len(self.__position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(v) != int for v in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(v < 0 for v in self.__position):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        "Value of Size"
        return self.__position

    @position.setter
    def position(self, value):
        "to retrieve position value of a square"
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(type(v) != int for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(v < 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        "prints in stdout the square with the character #"
        if self.__size != 0:
            for k in range(self.__position[1]):
                print()

            for i in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    def __str__(self):
        "Retrieve size in square"
        s = ""
        if self.__size != 0:
            for k in range(self.__position[1]):
                s += "\n"

            for i in range(self.__size):
                for in range(self.__position[0]):
                    s += " "
                for j in range(self.__size):
                    s += "#"
                s += "\n"
        else:
            s += "\n"
        return s[:-1]
