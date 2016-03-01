#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 08.02.2016
# Purpose: Illustrates Python's File I/O capabilities

han1 = open("f1","w")
han2 = open("f2","r")
blogname = "Linux-Library"
blogurl = "http://linux-library.blogspot.in"
count = 1

# % operator when applied to strings performs formatting
# %s - strings, %d - integers, %f - floats
'''
while count <= 10:
	han1.write("%d\t%s\t%s\n" % (count,blogname,blogurl))
	count += 1
'''
count = 0
while count <= 10:
	print han2.readline()
	count += 1
'''
for file_inp in han2.readline():
	print file_inp
han1.close()
#print han1()
'''
# END
