#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dict = a_dictionary.copy()
    for i, num in mul_dict.items():
        mul_dict[i] = num * 2
    return mul_dict
