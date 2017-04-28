#!/usr/bin/python

import urllib, json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
	address = raw_input('Please input address: ')
	
	if len(address) < 1 : break
	if address == 'done' : break
	
	url = serviceurl + urllib.urlencode({'sensor':'false', 'address':address})
	print "Retrieving", url, "...."
	
	data = urllib.urlopen(url).read()
	try:
		js = json.loads(str(data))
	except:
		js = None
	
	try:
		placeid = js['results'][0]['place_id']
		print address, ":", placeid
	except:
		print "Unable to fetch %s" %(address)
		continue
