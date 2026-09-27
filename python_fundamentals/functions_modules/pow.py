#!/usr/bin/env python3
def pow(a, b):
    result = 1
    absb = abs(b)
    for i in range(absb):
        result *= a
    if b < 0:
        return 1 / result
    return result
