#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or None:
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    for char in roman_string:
        value = roman_dict.get(char, 0)
        total += value - 2 * total if value > total else value
    return total
