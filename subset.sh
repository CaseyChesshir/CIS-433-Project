# subset.sh
# Author: Casey Chesshir
# Takes in a list of websites and outputs 
# the IPv6 address if it exists. 
#!/bin/bash

counter=0
while read p; do
	nslookup -query=AAAA  $p >> nslookups.txt

	echo " $counter "
	((counter++))
done < top500sites.txt
