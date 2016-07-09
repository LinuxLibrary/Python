#!/usr/lib/python

import urllib
fh = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')

for line in fh:
	print line.strip()
