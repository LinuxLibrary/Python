#!/usr/bin/python

import re
file = raw_input("Please input a file name: ")
fh = open(file)
total = 0
data = list()
count = 0
for line in fh:
	line = line.rstrip()
	if re.search('[0-9]+',line):
		data = re.findall('[0-9]+',line)
		for num in data:
			count = count + 1
			total = total + int(num)
print "There are %s values and sum=%s" %(count, total)
