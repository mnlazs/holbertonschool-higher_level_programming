#!/usr/bin/python3
def area(self):
    return self.__size ** 2

def getSize(self):
    return self.__size

def setSize(self, size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size

