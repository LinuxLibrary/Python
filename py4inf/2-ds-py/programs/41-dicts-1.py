#!/usr/bin/python

counts = dict()
names = ['arjun','nivas','omkar','arjun','shri','omkar','arjun','mallik','nivas']
for name in names:
	if name not in counts:
		counts[name] = 1
	else:
		counts[name] = counts[name] + 1
print counts
