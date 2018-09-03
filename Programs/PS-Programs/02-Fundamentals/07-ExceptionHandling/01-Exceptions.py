#!/usr/bin/env python3

'''A module for demonstrating exceptions.'''

def convert(s):
	'''Convert to an integer.'''
	try:
		x = int(s)
		print("Convertion succeeded! x =", x)
	except ValueError:
		print("Conversion failed!")
		x = -1
	except TypeError:
		print("Conversion failed!")
		x = -1
	return x