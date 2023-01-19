#!/usr/bin/python3
def add_integer(a, b=98):
    if type(a) not in (int, float) or type(b) not in (int, float):
        raise TypeError("a must be an integer or b must be an integer")
    a, b = int(a), int(b)
    return a + b
