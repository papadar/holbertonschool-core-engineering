#!/usr/bin/env python3
"""import the abstractmethod"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape is an abstract class"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


def shape_info(shape):
    """Print the shape info"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


class Rectangle(Shape):
    """A Rectangle is a Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    """A Circle is a Shape"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
