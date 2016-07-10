#!/usr/bin/python

import re, urllib
from BeautifulSoup import *

url = raw_input("Enter - ")

for i in range(8):
	print url
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup('a')
	tag = tags[17]
	url = tag.get('href', None)
