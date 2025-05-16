#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            try:
                res = a / b
            except TypeError:
                print("wrong type")
                res = 0
            except ZeroDivisionError:
                print("division by 0")
                res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
