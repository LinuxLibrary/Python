#!/usr/bin/python

# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
stot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    sppos = line.find(':')
    spam = float(line[sppos+1:].strip())
    stot = stot + spam
    count = count + 1
print "Average spam confidence:", stot/count
