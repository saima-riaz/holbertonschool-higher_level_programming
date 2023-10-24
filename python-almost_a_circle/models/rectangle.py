#!/usr/bin/python3
"""define class """
from models.base import Base


class Rectangle(Base):
    """ child class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class.

        Args:
        width: Width of the rectangle.
        height: Height of the rectangle.
        x: X-coordinate of the rectangle's position (default is 0).
        y: Y-coordinate of the rectangle's position (default is 0).
        id:optional identifier.If not provided,a unique id will be assigned.

        constructor of the parent cls(Base)called using super().__init__(id).
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
