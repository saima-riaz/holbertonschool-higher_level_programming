#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)"""


def append_write(filename="", text=""):
    """write the number of text"""
    num = 0
    with open(filename, "a", encoding="utf8")as file:
        file.write(text)
        num = len(text)
        return num
