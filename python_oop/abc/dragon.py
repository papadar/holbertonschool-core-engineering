#!/usr/bin/env python3
"""The mixins project"""


class SwimMixin:
    """The Swim Mix"""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """The Fly Mix"""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """The Dragon Class"""

    def roar(self):
        print("The dragon roars!")
