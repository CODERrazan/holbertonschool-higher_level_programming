#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element in a list with a new element."""
    return [replace if num == search else num for num in my_list]
