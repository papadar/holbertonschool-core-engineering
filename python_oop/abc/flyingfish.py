#!/usr/bin/env python3
"""Inherit from Multiuple parents"""


class Fish:
    """The Class is a Fish"""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """The Class is a Bird"""

    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """The FlyingFish inherits from multiple Classes"""

    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
