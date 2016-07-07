#!/usr/bin/python

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word, 0 ) + 1

lst = list()
for k, v in counts.items():
	lst.append( (v, k) )

lst.sort(reverse=True)
for v, k in lst[:10] :
	print k, v
