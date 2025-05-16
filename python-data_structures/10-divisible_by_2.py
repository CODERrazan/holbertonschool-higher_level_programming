#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Returns a list of True or False based on whether elements are divisible by 2."""
    return [
        num % 2 == 0
        for num in my_list
    ]
