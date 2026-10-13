#!/usr/bin/env python3
"""simple file append write func"""


def append_write(filename="", text="") -> int:
    """the function appends text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
