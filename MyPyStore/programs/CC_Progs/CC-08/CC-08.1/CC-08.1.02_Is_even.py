#!/usr/bin/python

def is_even(x):
#    x = raw_input("Please input a number : ")
    if int(x) % 2 == 0:
        print "%s is an even number" %(x)
        return True
    else:
        print "%s is not an even number" %(x)
        return False
        
print is_even(5)
