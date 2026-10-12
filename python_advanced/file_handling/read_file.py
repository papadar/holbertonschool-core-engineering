#!/usr/bin/env python3
"""simple file read line by line"""


def read_file(filename=""):
    """the function reads a file, and prints it line by line"""
    with open(filename) as f:
        for line in f:
            print(line, end='')
    f.close()
