#!/usr/bin/env python3
'''The documentation text'''


class Square:
    '''The class documentation text'''
    def __init__(self, size: int):
        self.size = size
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
