#!/usr/bin/env python3
"""import the abstractmethod"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal is an abstract class"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog is an Animal"""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat is also an Animal"""

    def sound(self):
        return "Meow"