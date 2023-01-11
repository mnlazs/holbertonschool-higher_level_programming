#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
        result = None
    finally:
        print("Inside Result: {}".format(result))
    return result

