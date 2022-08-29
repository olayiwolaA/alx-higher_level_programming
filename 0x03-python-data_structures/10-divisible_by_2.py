#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    find_div = []
    for i in my_list:
        if i % 2 == 0:
            find_div.append(True)
        else:
            find_div.append(False)
    return find_div
