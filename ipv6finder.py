import re


out = open('ipv6capablesites.txt','w')
with open('nslookups.txt') as f:
	for line in f:
		match = re.search(".+has AAAA address.+",line)
		if(match):
			out.write(match.group(0).split('\t')[0] + "\n")
out.close()
