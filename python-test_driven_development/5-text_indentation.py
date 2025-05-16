#!/usr/bin/python3
"""Module for text indentation."""

def text_indentation(text):
    """Prints text with new lines after '.', '?', and ':'.
    
    Args:
        text: Input text to format
        
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    if not text.strip():
        return
    
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end="")
        i += 1
