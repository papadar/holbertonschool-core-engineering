#!/usr/bin/env python3
"""simple file read line by line"""


def read_file(filename=""):
    with open(filename) as f:
        for line in f:
            print(line, end='')
    f.close()
