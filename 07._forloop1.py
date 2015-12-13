#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 07.07.2015
# Purpose : Illustrate For Loop usage

import string

# Define and loop through a string
string1 = "LinuxCBT"
for i in string1:
	print i

# Define and loop through list	
list1 = ["LinuxCBT", 395, "Open Source", "Kernel", "Debian", "Scripting"]
 for i in list:
 	print i	
	
logfile = ["20150707 192.168.1.2 3950", "20150707 192.168.1.100 42500"]	
logfile2 = []
for i in logfile:
	logfile2.extend(string.split(i))
	print logfile2
	
# END
