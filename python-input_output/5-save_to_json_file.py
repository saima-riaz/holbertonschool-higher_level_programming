#!/usr/bin/python3
"""impot Module"""
import json


def save_to_json_file(my_obj, filename):
    """write obj using Json"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
