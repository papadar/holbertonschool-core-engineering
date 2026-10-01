#!/usr/bin/env python3
def raise_exception_msg(message=""):
    try:
        print(my_variable)
    except NameError as e:
        e.args = (f"{e.args[0]} {message}",)
        raise
