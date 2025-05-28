#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""

class MyList(list):
    """Custom list class with additional sorting functionality."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
