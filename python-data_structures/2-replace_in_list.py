#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    # if stsement we do not do ant this else we assign it to position
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
