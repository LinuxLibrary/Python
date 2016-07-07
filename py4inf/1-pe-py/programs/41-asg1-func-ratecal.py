#!/usr/bin/python

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate: ")
r = float(rate)
    
def computepay(h,r):
    if h <= 40:
        p = h * r
        return
    else:
        p = r * 40 + ( r * 1.5 * ( h - 40 ) )
	print p
    
computepay(h,r)
