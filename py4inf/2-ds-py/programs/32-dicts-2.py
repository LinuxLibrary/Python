#!/usr/bin/python

counts = {'arjun': 3, 'nivas': 2, 'mallik': 1, 'shri': 1, 'omkar': 2}
for name in counts:
	if name in counts:
		print name, counts[name]
	else:
		print 0
