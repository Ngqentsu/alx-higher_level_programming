#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    pts = 0
    mass = 0

    for num in my_list:
        pts += num[0] * num[1]
        mass += num[1]

    return pts / mass
