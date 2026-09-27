#!/usr/bin/env python3
string = ""
for i in range(97, 123):
    if i != 101 and i != 113:
        string += chr(i)
print(f"{string}")
