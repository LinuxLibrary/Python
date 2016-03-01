#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 08.02.2016
# Purpose: Illustrates Python's File I/O capabilities

han1 = open("f1.txt","w")
blogname = "Linux-Library"
blogurl = "http://linux-library.blogspot.in"
count = 1

# % operator when applied to strings performs formatting
# %s - strings, %d - integers, %f - floats
while count <= 10:
	han1.write("%d\t%s\t%s\n" % (count,blogname,blogurl))
	count += 1
han1.close()
# END
