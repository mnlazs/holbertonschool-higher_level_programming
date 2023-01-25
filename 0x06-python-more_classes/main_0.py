#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
for k in sorted(my_rectangle.__dict__):
    print("{}: {}".format(k, my_rectangle.__dict__[k]))