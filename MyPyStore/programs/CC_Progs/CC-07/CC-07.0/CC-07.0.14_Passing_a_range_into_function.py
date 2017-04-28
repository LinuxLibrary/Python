#!/usr/bin/python

def my_function(x):
    for i in range(0,len(x)):
        x[i] = x[i] * 2
    return x
n = [0,1,2]
print my_function(n) # Add your range between the parentheses!
