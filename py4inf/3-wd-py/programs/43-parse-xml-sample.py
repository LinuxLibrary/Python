#!/usr/bin/python

import urllib
import xml.etree.ElementTree as ET

total = 0
url = raw_input("Enter URL: ")
uh = urllib.urlopen(url).read()
tree = ET.fromstring(uh)
results = tree.findall('comments/comment')

for result in results:
	cval = result.find('count').text
	total = total + int(cval)

print total

# print results, len(results)
