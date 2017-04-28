#!/usr/bin/python

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith('From: '): continue
    line = line.strip()
    line = line.split()
    print line[1]
    count = count + 1

print "There were", count, "lines in the file with From as the first word"
