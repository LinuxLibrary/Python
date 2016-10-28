#!/usr/bin/python

import requests, json
<<<<<<< HEAD
url = 'https://spscommerce.atlassian.net/rest/api/2/search?jql=project=CHGMGMT&fields=customfield_16002&maxResults=10'
username = 'XXXXXXXXX'
password = 'xxxxxxxxx'
=======
url = 'https://spscommerce.atlassian.net/rest/api/2/search?jql=project=CHGMGMT&fields=customfield_16002&maxResults=87'
username = 'XXXXXXXX'
password = 'xxxxxxxx'
>>>>>>> c19022dbe3b901fc814b9c36d2844970366af054

data = requests.get(url, auth=(username, password)).content

envcount = dict()

jdat = json.loads(str(data))
jsdata = jdat['issues']

for line in jsdata:
	env = line['fields']["customfield_16002"]["value"]
	envcount[env] = envcount.get(env, 0) + 1

casebyenv = json.dumps(envcount)
print casebyenv
