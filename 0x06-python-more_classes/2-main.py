#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
my_rectangle_rep = repr(my_rectangle)

new_rectangle = eval(my_rectangle_rep)
print(new_rectangle)