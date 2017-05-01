#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 01.05.2017

import subprocess

usage_threshold = 5
df_cmd = subprocess.check_output(['df','-k'])
lines = df_cmd.splitlines()

for line in lines[1:]:
	columns = line.split()
	occupied = columns[4].rstrip('%')
#	print "Disk %s occupied %s" % (columns[0], occupied)
	if int(occupied) >= usage_threshold:
		print "\n", '+' * 40
		print "Disk %s usage is beyond threshold at %s" % (columns[0], columns[4])
		print '+' * 40
print
