#!/usr/bin/python
# Author: Arjun Shrinivas
# Purpose : Illustrate while loops

import sys

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

count = 0
while answer != timeleft:
	print "Sorry", name, "That is an incorrect!"
	answer = input("How much time have you got left? ")
	if count ==2:
		print "Would you like to exit the program? "
		exitprog = raw_input()
		if exitprog == "yes":
			sys.exit()
		else:
			count = 0
	count = count + 1

print "Bingo!, you will live for", timeleft, "years"	
print "Thank you for using Lie Expectancy v0.99"

# END
