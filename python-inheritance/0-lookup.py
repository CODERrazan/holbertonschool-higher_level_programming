#!/usr/bin/python3
"""Module for listing object attributes and methods."""

def lookup(obj):
    """Return a list of available attributes and methods of an object.
    
    Args:
        obj: Any Python object to inspect
        
    Returns:
        list: Alphabetized list of attributes/methods
    """
    return dir(obj)
