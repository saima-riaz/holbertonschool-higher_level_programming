#!/usr/bin/python3
"""function that returns the JSON representation of an object"""


import json


def from_json_string(my_str):
    """json obj"""
    return json.loads(my_str)
