#!/usr/bin/python

def factorial(x):
    if x == 0 or x == 1 :
        return 1
    else:
        x = factorial(x-1) * x
    return x
print factorial(1)
