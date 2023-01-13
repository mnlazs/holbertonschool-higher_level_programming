#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b()):
first_a = tuple_a[0] if len(tuple_a) > 0 else 0
    first_b = tuple_b[0] if len(tuple_b) > 0 else 0
    second_a = tuple_a[1] if len(tuple_a) > 1 else 0
    second_b = tuple_b[1] if len(tuple_b) > 1 else 0
    return (first_a + first_b, second_a + second_b)
