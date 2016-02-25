# ips.sh
# Casey Chesshir
# Takes in a list of websites and outputs the 
# IP addresses that the website is hosted on. 
# usage: ./ips.sh top500sites.txt top500IPs.txt
#!/bin/bash
args=("$@")
counter=0
while read p; do
	host $p >> ${args[1]}
	echo "getting host info for site #$counter of 500: $p"
	((counter++))
done < ${args[0]}
