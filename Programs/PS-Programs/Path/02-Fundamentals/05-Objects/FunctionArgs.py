#!/usr/bin/env python3

def banner(message, border=None):
	line = border * len(message)
	print(line)
	print(message)
	print(line)