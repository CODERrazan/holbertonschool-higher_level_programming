#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """we created a copy then we cheked  if so return copy if not we change"""
    Thecpoy = my_list.copy()
    if idx < 0 or idx >= len(Thecopy):
        return new_list
    Thecopy[idx] = element
    return Thecopy
