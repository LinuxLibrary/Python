#!/usr/bin/python

fh = open("mbox-short.txt", "r")

count = 0
for line in fh:
    print line.strip()
    count = count + 1
        
print count, "MBOX-Short Lines: "
