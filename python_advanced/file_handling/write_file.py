#!/usr/bin/env python3
"""simple file write func"""


def write_file(filename="", text="") -> int:
    """the function writes text to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
