#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 03.05.2017
# Purpose : Using Generators in Python

def counter():
	i = 0
	while True:
		return i
a = counter()
print type(a)

print a
print a
print "There is no change. Let us try using Generators"

def counter():
	i = 0
	while True:
		yield i
a = counter()
print type(a)

print a
print a
print a

# END
