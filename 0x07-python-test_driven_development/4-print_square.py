#!/usr/bin/python3
"""
    Write a function that prints a square
"""


def print_square(size):
    """ print a square """
    int_error = "size must be an integer"
    neg_error = "size must be >= 0"
    if type(size) is not int:
        raise TypeError(int_error)
    if size < 0:
        raise ValueError(neg_error)
    for i in range(size):
        print("#" * size, end="")
        print()
