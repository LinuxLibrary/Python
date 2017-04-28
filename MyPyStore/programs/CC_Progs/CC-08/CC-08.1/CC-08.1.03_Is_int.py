#!/usr/bin/python

def is_int(x):
    #if x % 1 == 0:
    if x == int(x):
        return True
    else :
        return False
print is_int(5.7)
