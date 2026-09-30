#!/usr/bin/env python3
def safe_print_division(a, b):
    result = 0
    try:
        result = float(a) / float(b)
    except (TypeError, ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
