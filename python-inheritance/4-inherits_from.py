#!/usr/bin/python3
"""
Write a function that cheks isinstance
"""


def inherits_from(obj, a_class):
    """
    Checks, if obj isinstance a_class returns true
    """
    if ((type(obj) is not a_class) and isinstance(obj, a_class)):
        return True
    else:
        return False
