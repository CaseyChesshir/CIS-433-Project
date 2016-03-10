import sys
import re
import os
from collections import OrderedDict


'''
extractor.py
Author: Casey Chesshir
Usage: $ python3 extractor.py ASN
Finds all unique paths to the ASN provided by command line input.
'''

f = open("routeviews6.txt","r")
out = open("routeviews6just" + sys.argv[1] + ".txt","w")

results = set()
peers = set()
for line in f:
	tokens = line.split("|")
	peer = tokens[5]
	peers.add(peer)
	path = tokens[9]
	origin = tokens[10]
	if (origin == sys.argv[1]):
		results.add(peer + "|" + path + "|" + origin + "\n")
results = list(OrderedDict.fromkeys(results))
results = sorted(results)
peers = sorted(peers)
for item in results:
	out.write(item)

f.close()
out.close()
command = "bgpreader -d singlefile -o upd-file,v4ribtable.bz2 -w 0,1457304822"
for item in peers:
	command += " -j " + item
os.system(command + " > routeviews4.txt")

newresults = set()

peers = set()

r4 = open("routeviews4.txt","r")
for line in r4:
	tokens = line.split("|")
	peer = tokens[5]
	peers.add(peer)
	path = tokens[9]
	origin = tokens[10]
	if (origin == sys.argv[1]):
		newresults.add(peer + "|" + path + "|" + origin + "\n")

newresults = list(OrderedDict.fromkeys(newresults))
newresults = sorted(newresults)
out = open("routeviews4just" + sys.argv[1] + ".txt","w")
for item in newresults:
	out.write(item)
r4.close()
out.close()		

results = set(results)
newresults = set(newresults)
results.symmetric_difference(newresults)
