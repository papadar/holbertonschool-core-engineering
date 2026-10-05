#!/usr/bin/env python3
"""extend the list functions"""


class VerboseList(list):
    """the overwritten methods"""

    def append(self, value):
        super().append(value)
        print("Added [{}] to the list.".format(value))

    def extend(self, args):
        items = list(args)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, index):
        if index in self:
            super().remove(index)
            print("Removed [{}] from the list.".format(index))

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(self[index]))
        return super().pop(index)
