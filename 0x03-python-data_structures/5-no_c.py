#!/usr/bin/python3
def no_c(my_string):
    chgstr = ''
    for i in my_string:
        if i != 'c' and i != 'C':
            chgstr += i
    return chgstr
