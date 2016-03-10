import glob, re

name = 'master_diagnostics.txt'
diag_file = open(name, "w+")

countList6 = []
countList4 = []
vSixFlag   = False
vFourFlag  = False
sixHops    = 0
fourHops   = 0

class IPcount:
	count = 0
	per   = 0.0
	url   = ' '
	addr  = ' '

	def __init__(self, url, addr):
		self.count = 1
		self.url   = url
		self.addr  = addr

	def __str__(self):
		return str(self.count) + '\t' + str(self.per) + '%\t' + self.url + '\t' + self.addr

	def checkAddr(self, inputAddr):
		if self.addr == inputAddr:
			return True
		else:
			return False

	def updateCount(self):
		self.count += 1

	def getPercentTotal(self, total):
		self.per = round((self.count / total ) * 100, 2)

def process(tempIPcount, ipAddr, ipList):
	exists = False

	for element in ipList:
		if element.checkAddr(ipAddr):
			element.updateCount()
			exists = True

	if not exists:
		ipList.append(t)

for filename in glob.glob('*.com_02*'):
	textFile = open(filename, "r")

	for line in textFile:
		if line[0] == ' ':
			vSixFlag = True

		elif vSixFlag == True:
			if line[0] == '(':
				sixHops += 1
				split = line.split(', ')
				split2 = re.sub(r'[\[\]\)]', '', split[2])
				t = IPcount(split[1], split2)
				process(t, split2, countList6)
			else:
				vSixFlag = False

		elif line[0] == '-':
			vFourFlag = True

		elif vFourFlag == True:
			if line[0] == '(':
				fourHops += 1
				split = line.split(', ')
				t = IPcount(split[1], split[2])
				process(t, split[2], countList4)
			else:
				vFourFlag = False

countList6.sort(key=lambda x: x.count, reverse = True)
countList4.sort(key=lambda x: x.count, reverse = True)

diag_file.write("Diagnostics for IPv6:\n")
for element in countList6:
	element.getPercentTotal(sixHops)
	diag_file.write(str(element))

diag_file.write("\nTotal hops for v6: " + str(sixHops) + "\n")

diag_file.write("\nDiagnostics for IPv4:\n")
for element in countList4:
	element.getPercentTotal(fourHops)
	diag_file.write(str(element))

diag_file.write("\nTotal hops for v4: " + str(fourHops) + "\n")
