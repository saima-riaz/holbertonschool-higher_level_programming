#!/usr/bin/python3
""""
    prints a text with 2 new lines after each of these characters: ., ? and :
    otherrwise raise typeerror exception"""


def text_indentation(text):
    """ validation """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    """ create a list of my separators and copy text in new text """
    separators = ('.', '?', ':')
    current_line = ""

    for char in text:
        current_line += char
        if char in separators:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
