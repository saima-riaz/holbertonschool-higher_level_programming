#!/usr/bin/python3
"""define class"""
import json


class Base:
    """define class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert the JSON string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save a list of objects to a file in JSON format """
        filename = cls.__name__ + ".json"
        list_of_dict = []
        if list_objs is not None:
            for obj in list_objs:
                list_of_dict.append(obj.to_dictionary())
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(cls.to_json_string(list_of_dict))

    @staticmethod
    def from_json_string(json_string):
        """covert a json"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create a new instance of the class from a dictionary """
        if cls.__name__ == "Rectangle":
            obj = cls(2, 3)
        else:
            obj = cls(3)
            obj.update(**dictionary)
            return obj
