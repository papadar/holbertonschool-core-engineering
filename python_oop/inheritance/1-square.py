#!/usr/bin/env python3
"""The Import documentation text"""
Rectangle = __import__('2-rectangle').Rectangle    


class Square(Rectangle):
    """The Square Class documentation text"""
    def __init__(self, size):
        """use size value for width and height"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
