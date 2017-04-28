#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 08.02.2016
# Purpose: Illustrates Python's File I/O capabilities

# Open accepts 2 arguments: Filename, Mode
# Modes include: r, rb, w, wb, a, r+
# 2 file handles - han1=read han2=write
han1 = open("file1","r")
han2 = open("file2","a")

# readline reads into a string the first line upto \n
# read - reads entire file into a string, unless num of chars specified
# readlines - will read one line per list element
print han1.readline()
tempread1 = han1.readlines()
print tempread1
for i in tempread1:
	han2.write(i)
	
han1.close()
han2.close()

# END
