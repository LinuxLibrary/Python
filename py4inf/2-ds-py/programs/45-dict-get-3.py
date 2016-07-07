#!/usr/bin/python

# This program is used to ask for a paragraph or sentance from the user 
# and get the number of occurances of the word in the scentance.

counts = dict()
print 'Enter a line / paragraph of text'
line = raw_input('')

words = line.split()

print 'Counting words...'
for word in words:
	counts[word] = counts.get(word,0) + 1
print counts
