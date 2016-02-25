'''
----------------------------------------------
topsitescraper.py
Author: Casey Chesshir

Gathers data from alexa.com's website. Finds 
the top 500 ranked websites and outputs into 
a file called top500sites.txt. 
----------------------------------------------
'''

from urllib.request import urlopen
import re
import sys

urls = [urlopen('http://www.alexa.com/topsites/countries/US')]
for i in range(1,20):
	urls.append(urlopen('http://www.alexa.com/topsites/countries;' + str(i) + '/US'))

urls = [url.read() for url in urls]
urls = [url.decode() for url in urls]

sites = []
for url in urls:
	temp = re.findall(r'/siteinfo/.+>.+<',url)
	sites.append([site[site.find(">") + 1:site.find("<")] for site in temp])
print("sys.argv: " + sys.argv[0] + " " + sys.argv[1])

f = open(sys.argv[1],'w')

for site in sites:
	for item in site:
		f.write(item + '\n')
