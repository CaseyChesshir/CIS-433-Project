#!/bin/bash

counter=0
while read p; do
	nslookup -query=AAAA  $p >> nslookups.txt

	echo " $counter "
	((counter++))
done < output.txt
