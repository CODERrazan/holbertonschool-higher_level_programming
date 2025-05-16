#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints result with debug info"""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))
        return result
