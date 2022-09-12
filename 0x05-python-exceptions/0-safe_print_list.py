#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    xele = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
        except Exception:
            break
        else:
            xele += 1
    print()
    return xele
