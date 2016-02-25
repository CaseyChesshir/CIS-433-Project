import sys

'''
AS-IPmapper.py
Author: Casey Chesshir
Usage: $ python3 AS-IPmapper.py top500IPs.txt


'''

import re

#with open('AStoIP.txt') as out:
#	with open('top500IPs.txt') as f:
out = open(sys.argv[2],'w')
f = open(sys.argv[1])
seen_v4_domains = set()
seen_v6_domains = set()
for line in f:
	match = re.search(".+has address.+",line)
	if(match):
		domain = line.split(' ')[0]
		if domain not in seen_v4_domains:
			v4address = line.split(' ')[-1]
			seen_v4_domains.add(domain)
			out.write(domain + " " + v4address)
	match = re.search(".+has IPv6 address.+",line)
	if(match):
		domain = line.split(' ')[0]
		if domain not in seen_v6_domains:
			v6address = line.split(' ')[-1]
			seen_v6_domains.add(domain)
			out.write(domain + " " + v6address)
f.close()
out.close()
