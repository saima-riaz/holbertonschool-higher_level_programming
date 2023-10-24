#!/usr/bin/python3
""" define class """


class Base:
    """ define class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ define class constructor """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """ define class childi Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):

        """ Class constructor """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        """ called super class """
        super().__init__(id)
