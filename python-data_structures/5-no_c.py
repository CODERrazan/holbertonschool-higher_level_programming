#!/usr/bin/python3
def no_c(my_string):
    """loop 1 for every char then 2 to check Cc and add new"""
    new_string = ""
    for char in my_string:
        if char not in 'cC':
            new_string += char
    return new_string
