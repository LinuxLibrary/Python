#!/usr/bin/python

counts = {'arjun': 3, 'nivas': 2, 'mallik': 1, 'shri': 1, 'omkar': 2}
for name in counts:
	print name, counts.get(name,0)
