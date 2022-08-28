#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listcopy = my_list[:]
    if idx >= 0 and idx <= len(listcopy) - 1:
        listcopy[idx] = element
    return listcopy
