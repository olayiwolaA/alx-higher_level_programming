#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ord_list = sorted(a_dictionary.keys())
    for i in ord_list:
        print("{:s}: {}".format(i, a_dictionary[i]))
