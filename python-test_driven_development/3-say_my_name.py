#!/usr/bin/python3
""" print my_name is <first name> <last name> otherwise raise typeerror exception"""


def say_my_name(first_name, last_name=""):
    """ valid first_name"""
    if type(first_name) is not str:
            raise TypeError("first_name must be a string")
    if type(last_name)is not str:
        raise TypeError("last_name must be a string")
    print("My_name is {} {}".format(first_name, last_name))
