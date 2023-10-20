i#!/usr/bin/python3
"""import module"""
import json


def load_from_json_file(filename):
    """load an object using json"""

    with open(filename, "r") as file:
        x = json.load(file)
        return x
