#!/usr/bin/python3
"""Module: MyList class"""

class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
