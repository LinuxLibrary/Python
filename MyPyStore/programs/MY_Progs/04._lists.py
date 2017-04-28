#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 17.06.2015
# Purpose : Illustrate lists of strings

import string

print range(10) # Returns all values excluding boundary (10)
print range(1,11) # Returns 1 - 10.

stringlist = ["LinuxCBT","Scripting","Edition"]
stringlist2 = ["Python","BASH"]
print stringlist

stringlist.reverse()
print stringlist

stringlist.append(stringlist2)
print stringlist
print stringlist[3][0]

PoppedValue = stringlist.pop()
print PoppedValue
stringlist.extend(stringlist2)
print stringlist

stringlist.insert(3,"Perl")
print stringlist

# Processing of ficticious Apache web server log file
logfile = "20150617 192.168.1.100 1100 192.168.1.104 80 404 index.php"

print logfile
print type(logfile)

# Convert logfile entry into a list from a flat string
logfile2 = string.split(logfile)
print logfile2

# Slice logfile2 to extract important fields
logfile3 = logfile2[0:5]
print logfile3

# Join logfile3 into a flat string
logfile4 = string.join(logfile3)
print logfile4
print type(logfile4)


# END
