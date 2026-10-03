#!/usr/bin/env python3
'''The documentation text'''


class Square:
    '''The class documentation text'''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        if (self.size == 0):
            print()
            return
        for j in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        if (self.size == 0):
            return ""
        lines = [""] * self.position[1]
        lines += [" " * self.position[0] + "#" * self.size] * self.size
        return "\n".join(lines)
