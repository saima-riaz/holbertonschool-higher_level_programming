#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    max_val = my_list[1]
    for x in my_list:
        if x <  max_val:
            return max_val    
