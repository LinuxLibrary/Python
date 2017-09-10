#!/usr/bin/python

for i in range(2):
    choice = raw_input("Please input your name : ")
    if choice != "Arjun":
        print "Entry restricted!"
        break
else:
    print "Welcome Geek!"
