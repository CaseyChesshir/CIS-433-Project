from urllib.request import urlopen
import re

front = urlopen('http://www.alexa.com/topsites/countries/US')
second= urlopen('http://www.alexa.com/topsites/countries;1/US')
third = urlopen('http://www.alexa.com/topsites/countries;2/US')
fourth= urlopen('http://www.alexa.com/topsites/countries;3/US')

urls = [front,second,third,fourth]
urls = [url.read() for url in urls]
urls = [url.decode() for url in urls]
print(type(urls[0]))
sites1 = re.findall(r'/siteinfo/\w+\.\w+',urls[0])
sites1 = [site[10:] for site in sites1]
sites2 = re.findall(r'/siteinfo/\w+\.\w+',urls[1])
sites2 = [site[10:] for site in sites2]
sites3 = re.findall(r'/siteinfo/\w+\.\w+',urls[2])
sites3 = [site[10:] for site in sites3]
sites4 = re.findall(r'/siteinfo/\w+\.\w+',urls[3])
sites4 = [site[10:] for site in sites4]

topsites = [sites1,sites2,sites3,sites4]

f = open('output.txt','w')
for sites in topsites:
	for site in sites:
		f.write(site + "\n")
