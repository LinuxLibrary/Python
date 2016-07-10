#!/usr/bin/python

import re, urllib
from BeautifulSoup import *

url = raw_input("Enter - ")
#html = urllib.urlopen(url).read()
#soup = BeautifulSoup(html)
#tags = soup('a')

#print url
for i in range(5):
	print url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	tag = tags[2]
	url = tag.get('href', None)
#	print url	
	
#print tags[2]
#for tag in tags:
#	tag = str(tag)
#	link = tag.get('href', None)
#	name = re.findall('by_(.+)\.html', link)
#	print link, name[0]
