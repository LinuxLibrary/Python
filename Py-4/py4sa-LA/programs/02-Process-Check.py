#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 02.05.2017
# Purpose : Check the number of processes running by a user in Linux Machine

import subprocess
lookup_user = 'root'
pCount = 0
for line in subprocess.check_output("ps -ef", shell=True).splitlines()[1:]:
	user = line.split()[0]
	if lookup_user == user:
		pCount+=1
print "User %s has %s processes running" % (lookup_user, pCount)

# END
