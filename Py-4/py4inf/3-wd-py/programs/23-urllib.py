#!/usr/bin/python

import urllib
#fh = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
fh = urllib.urlopen('http://www.linux-library.in')

for line in fh:
	print line.strip()
