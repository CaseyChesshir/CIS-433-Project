# ips.sh
# Casey Chesshir
# Takes in a list of websites and outputs the 
# IP addresses that the website is hosted on. 

#!/bin/bash

counter=0
while read p; do
	host $p >> top500IPs.txt	
	echo "checking website #$counter of 500: $p"
	((counter++))
done < top500sites.txt
