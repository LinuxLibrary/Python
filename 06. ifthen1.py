#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 06.07.2015
# Purpose : Expound on conditional branching

import sys
# print sys.argv
# print len(sys.argv)

THRESHOLD = 5
ARGLEN = len(sys.argv)
if ARGLEN < THRESHOLD:
	print "Script requires at least", THRESHOLD - 1, "arguments"
	print "You've entered ", ARGLEN - 1, "arguments"
elif ARGLEN >= 5 and ARGLEN <= 8:
	print "You've entered ", ARGLEN - 1, "arguments"
	print "You are in branch 2"
elif ARGLEN >= 8 and ARGLEN <= 10:
	print "You've entered ", ARGLEN - 1, "arguments"
	print "You are in branch 3"
	for i in sys.srgv:
		print i
else:
	print sys.argv[0], "Accepts only 9 arguments"


# END
