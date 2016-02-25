'''
ipv6finder.py
Author: Casey Chesshir

Takes as input the output of subset.sh and outputs the list of 
websites that have IPv6 addresses into ipv6capablesites.txt. 
usage: python3 ipv6finder.py nslookups.txt ipv6capablesites.txt
'''
import sys
import re
print(sys.argv[1])
print(sys.argv[2])

out = open(sys.argv[2],'w')
with open(sys.argv[1]) as f:
	for line in f:
		match = re.search(".+has AAAA address.+",line)
		if(match):
			out.write(match.group(0).split('\t')[0] + "\n")
out.close()
