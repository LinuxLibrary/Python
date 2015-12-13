#!/usr/bin/python
# Author:

print "----- Life Expectency v0.99-----"
name = raw_input("What is your name? ")
print name,
age = input("What is your age? ")
print name,
expect = input("To what age do you expect to live? ")

# extending life2.py to incorporate conditional testing
timeleft = expect - age

print name,
answer = input("How much time have you got left? ")

if answer != timeleft:
	print "Sorry", name, "That is an incorrect!"
else:
	print "Bingo!, you will live for", timeleft, "years"
	
print name,
print "Based on our calculation, you will live for ", expect - age, " more years"

	
print "Thank you for using Lie Expectancy v0.99"

# END
