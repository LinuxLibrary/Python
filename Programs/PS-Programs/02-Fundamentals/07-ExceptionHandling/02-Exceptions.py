#!/usr/bin/env python3

'''A module for demonstrating exceptions.'''

import sys

def convert(s):
	'''Convert to an integer.'''
	try:
		x = int(s)
		print("Convertion succeeded! x =", x)
	except (ValueError, TypeError) as e:
		print("Conversion error: {}"\
				.format(str(e)),
				file=sys.stderr)
		raise # Re-raise exception