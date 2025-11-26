#!/usr/bin/python3
"""
create empty class
"""


class BaseGeometry:
    """
    empty class
    """

    def area(self):
        """
        if area is not defined, raise exception
        """
        raise Exception("area() is not implemented")
