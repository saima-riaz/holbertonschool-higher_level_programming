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
    
    @property
    def size(self):
        return(self.__width)

    @size.setter
    def size(self, value):
        """ size """
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ update attribut"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
