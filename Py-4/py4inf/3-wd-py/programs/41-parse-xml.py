#!/usr/bin/python

import xml.etree.ElementTree as ET
data = '''
<person>
	<name>Arjun</name>
	<phone type="intl">
		+91 9885577285
	</phone>
	<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print 'Name:', tree.find('name').text
print 'Attr:', tree.find('email').get('hide')
