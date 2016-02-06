from urllib.request import urlopen
import re

urls = [urlopen('http://www.alexa.com/topsites/countries/US')]
for i in range(1,20):
	urls.append(urlopen('http://www.alexa.com/topsites/countries;' + str(i) + '/US'))

urls = [url.read() for url in urls]
urls = [url.decode() for url in urls]

sites = []
for url in urls:
	temp = re.findall(r'/siteinfo/\w+\.\w+',url)
	sites.append([site[10:] for site in temp])

f = open('output.txt','w')

for site in sites:
	for item in site:
		f.write(item + '\n')