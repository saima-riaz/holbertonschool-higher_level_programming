#!/usr/bin/python3
"""write a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ define class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, id, x, y)
        self.size = size

    def __str__(self):
        """ define Square """
        return f"[Square] ({self.id}), {self.x}/{self.y} - {self.width}"
