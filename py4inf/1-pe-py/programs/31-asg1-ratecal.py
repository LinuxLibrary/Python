#!/usr/bin/python

hrs = raw_input("Enter Hours: ")
h = float(hrs)
rate = raw_input("Enter Rate: ")
r = float(rate)

if h <= 40:
    pay = h * r
else:
    pay = r * 40 + ( r * 1.5 * ( h - 40 ) )
    
print pay
