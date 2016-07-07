#!/usr/bin/python

file = raw_input("Enter file name: ")
fh = open(file)
lst = list()
for line in fh:
	line = line.rstrip()
	line = line.split()
	for word in line:
		if word in lst: continue
		lst.append(word)
lst.sort()
print lst
