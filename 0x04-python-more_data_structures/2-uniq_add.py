#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_integers = set(my_list)
    sum_total = 0

    for i in unique_integers:
        sum_total += i

    return(sum_total)
