# subset.sh
# Author: Casey Chesshir
# Takes in a list of websites and outputs 
# the IPv6 address if it exists. 
#!/bin/bash
args=("$@")
echo ${args[0]}
echo ${args[1]}
counter=0
while read p; do
	nslookup -query=AAAA  $p >> ${args[1]}

	echo "getting nslookup info for site #$counter out of 500: $p"
	((counter++))

done < ${args[0]}
