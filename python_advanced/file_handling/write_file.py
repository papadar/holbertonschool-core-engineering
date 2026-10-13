#!/usr/bin/env python3
"""simple file write func"""


def write_file(filename="", text=""):
    """the function writes text to a file"""
    with open(filename, 'w') as f:
        f.write(text)
