#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for comp in my_list:
        if comp == search:
            new_list.append(replace)
        else:
            new_list.append(comp)

    return new_list
