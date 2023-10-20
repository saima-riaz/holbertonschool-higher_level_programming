#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """write the number of text"""
    num = 0
    with open(filename, "w", encoding="utf8")as file:
        file.write(text)
        num = len(text)
        return num
