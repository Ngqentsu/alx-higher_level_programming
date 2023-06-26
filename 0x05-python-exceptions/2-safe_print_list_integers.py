#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    item = 0

    try:
        for num in range(x):
            if isinstance(my_list[num], int):
                print("{:d}".format(my_list[num]), end="")
                item += 1

    except (ValueError, TypeError):
        pass
    
    print("")
    return item
