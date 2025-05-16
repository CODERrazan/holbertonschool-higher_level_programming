#!/usr/bin/python3
"""Module for text indentation."""


def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text: Input text to format (must be string).

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()  # Ensure no leading/trailing spaces
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:": 
            print("\n")  # Only one newline after punctuation
            print()      # Second newline
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1  # Skip spaces after punctuation
            continue
        i += 1
