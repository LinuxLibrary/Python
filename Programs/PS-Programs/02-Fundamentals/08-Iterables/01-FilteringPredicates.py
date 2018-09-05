#!/usr/bin/env python3

'''Print prime numbers between 0 and 101'''

def is_prime(x):
	if x < 2:
		return False
	for i in range(2, int(sqrt(x)) + 1):
		if x % i == 0:
			return False
	return True
	
[x for x in range(101) if is_prime(x)]