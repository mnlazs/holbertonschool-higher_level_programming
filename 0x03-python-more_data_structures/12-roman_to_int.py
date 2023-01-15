#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    result = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i+2] in roman:
            result += roman[roman_string[i:i+2]]
            i += 2
        else:
            result += roman[roman_string[i]]
            i += 1
    return result

