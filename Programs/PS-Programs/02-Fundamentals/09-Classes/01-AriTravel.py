#!/usr/bin/env python3

"""Model for aircraft flights"""

class Flight:

	def __init__(self, number):
		if not number[:2].isalpha():
			raise ValueError("No airline code in '{}'".format(number))
		
		if not number[:2].isupper():
			raise ValueError("Invalid airline code '{}'".format(number))
			
		if not (number[2:].isdigit() and int(number[2:]) <= 9999):
			raise ValueError("Invalid route number '{}'".format(number))
			
		self._number = number
		
	def number(self):
		return self._number