Rectangle = __import__('9-rectangle').Rectangle
"""class Square that inherits from Rectangle (9-rectangle.py)"""


class Square(Rectangle):
    """define class"""

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """define area"""
        return self.__size ** 2

    def __str__(self):
        """define str"""
        return f"[Square] {self.__size}/{self.__size}"
