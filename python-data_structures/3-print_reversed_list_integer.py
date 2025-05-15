#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """we use slicing to revers"""
    for num in my_list[::-1]:
        print("{:d}".format(num))
