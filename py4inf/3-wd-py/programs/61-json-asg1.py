#!/usr/bin/python

import urllib, json, re

url = raw_input("Enter URL: ")
data = urllib.urlopen(url).read()

try:
	js = json.loads(str(data))
except:
	js = None

total = 0
jsdata = js["comments"]
for line in jsdata:
	count = int(line["count"])
	total = total + count
print total
