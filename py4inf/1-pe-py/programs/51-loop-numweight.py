#!/usr/bin/python

largest = None
smallest = None

while True:
        inp = raw_input("Enter a number: ")
        if inp == 'done': break
        try:
                num = int(inp)
                if num > largest or largest == None:
                        largest = num
                elif num < smallest or smallest == None:
                        smallest = num
        except:
                print "Invalid input"
                continue
print "Maximum is", largest
print "Minimum is", smallest
