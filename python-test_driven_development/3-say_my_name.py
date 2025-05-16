#!/usr/bin/python3
"""Prints a formatted name string"""


def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'
    
    Args:
        first_name: First name string (required)
        last_name: Last name string (optional, defaults to empty string)
    
    Raises:
        TypeError: If either name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
