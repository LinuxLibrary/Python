#!/usr/bin/env python3

def sqrt(x):
	'''Compute square roots using the method of Heron of Alexandria.
	
	Args:
		x: The number for which the square root is to be computed.
		
	Returns:
		The square root of x.
		
	Raises:
		ValueError: If x is negative
	'''
	
	if x < 0:
		raise ValueError("Cannot compute square root of negative number".format(x))
		
		guess = x
	i = 0
	while guess * guess != x and i < 20:
		guess = (guess + x / guess) / 2.0
		i += 1
	return guess