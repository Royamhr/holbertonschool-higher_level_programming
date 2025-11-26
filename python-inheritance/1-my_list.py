#!/usr/bin/python3
"""Module that defines MyList class, inheriting from list."""

class MyList(list):
    """MyList class that inherits from list and adds print_sorted method."""

    def print_sorted(self):
        """Print the list in ascending order without modifying the original list."""
        print(sorted(self))
