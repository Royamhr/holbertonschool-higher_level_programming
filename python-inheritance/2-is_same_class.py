#!/usr/bin/python3
"""
Write a function that cheks isinstance
"""


def is_same_class(obj, a_class):
    """
    Checks, if obj isinstance a_class returns true
    """
    if (type(obj) is a_class):
        return True
    else:
        return False
