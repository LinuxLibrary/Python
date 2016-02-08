#!/usr/bin/python
# Author : Arjun Shrinivas
# Date : 08.02.2016
# Purpose: Illustrates Python's File I/O capabilities

han1 = open(f1,"w")
blogname = "Linux-Library"
blogurl = "http://linux-library.blogspot.in"
count = 1
han1.write(blogname,blogurl)
han1.close()

# END
