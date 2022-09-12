#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    result = 0
    safe = 0
    try:
        result = fct(*args)
        safe = 1
    except Exception as func:
        print("Exception: {}".format(func), file=sys.stderr)
    if safe == 1:
        return (result)
    else:
        result = None
