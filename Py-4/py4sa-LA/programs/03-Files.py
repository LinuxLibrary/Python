#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 03.05.2017
# Purpose : File processing and exception handling

try:
	file = '/var/log/dummy'
	for line in open(file):
		print line
except IOError:
	print "File does not exist"
except:
	print "Can't open file"
else:
	print "Done processing file"

# END
