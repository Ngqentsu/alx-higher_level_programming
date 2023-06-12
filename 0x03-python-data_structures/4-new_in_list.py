#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    updated_list = my_list.copy()
    updated_list[idx] = element
    return updated_list
