#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text: Input text to format (must be string)

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="\n\n")
            # Skip spaces after delimiter
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        else:
            print(text[i], end="")
        i += 1
