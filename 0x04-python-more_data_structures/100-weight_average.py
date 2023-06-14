#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    score = 0
    weight = 0

    for num in my_list:
        score += num[0] * num[1]
        weight += num[1]

    return score / weight
