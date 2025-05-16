#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'
    
    Args:
        text: The text to format (must be string)
    
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            # Skip any spaces after the delimiter
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
