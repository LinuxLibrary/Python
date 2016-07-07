#!/usr/bin/python

names = ['bash','arjun','nivas','bash','shri','arjun','nivas','bash','arjun']
counts = dict()
for name in names:
	counts[name] = counts.get(name,0) + 1
print counts
