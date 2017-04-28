#!/usr/bin/python

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)

hcount = dict()
for line in fh:
	words = line.strip()
	if not words.startswith("From "): continue
	lst = words.split()
	pos = lst[5].index(':')
	hour = lst[5][0:pos]
	hcount[hour] = hcount.get(hour, 0) + 1

#print hcount
hlst = list()
for k, v in hcount.items():
	hlst.append( (k, v) )
hlst.sort()
#print hlst
for k, v in hlst:
	print k, v
