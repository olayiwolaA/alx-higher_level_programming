#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = 0
    uni = set(my_list)
    for i in uni:
        num += i
    return num
