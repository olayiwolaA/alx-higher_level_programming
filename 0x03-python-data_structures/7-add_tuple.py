#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        addtup1 = tuple_a[:2]
    else:
        if len(tuple_a) == 1:
            addtup1 = tuple_a[0], 0
        else:
            addtup1 = 0, 0
    if len(tuple_b) >= 2:
        addtup2 = tuple_b[:2]
    else:
        if len(tuple_b) == 1:
            addtup2 = tuple_b[0], 0
        else:
            addtup2 = 0, 0
    return (addtup1[0] + addtup2[0], addtup1[1] + addtup2[1])
