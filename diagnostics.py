import sys

'''
diagnostics.py
Author: Casey Chesshir
Usage: $ python3 routeviews4justxxxx.txt routeviews6justxxxx.txt xxxx
'''


v4 = open(sys.argv[1],"r")
v6 = open(sys.argv[2],"r")

output = open("DiagnosticsForAsn" + sys.argv[3],"w")

output.write("New Diagnostics session: \n")

def AvgUniquePathsPerPeer(inputfile):
	totalpeers = 1
	totalnumpaths = 0
	totalpathlength = 0

	last_pos = inputfile.tell()
	currentpeer = inputfile.readline().split("|")[0]
	inputfile.seek(last_pos)	
	
	peerset = set()

	currentnumpaths = 0

	outputstring = ""

	for line in inputfile:
		tokens = line.split("|") # tokens: {peer,path,origin}
		totalpathlength += len(tokens[1].split(" ")) - 1
		peerset.add(tokens[0])
		totalnumpaths += 1
		if tokens[0] != currentpeer:
			currentpeer = tokens[0]	
			totalpeers+=1
		else:
			currentnumpaths+=1
	outputstring+=("totalpeers: " + str(totalpeers) + "\n")	
	outputstring+=("totalnumpaths: " + str(totalnumpaths) + "\n")	
	outputstring+=("totalpathlength: " + str(totalpathlength) + "\n")
	outputstring+=("avgpathlength: " + str(round(totalpathlength/totalnumpaths,2)) + "\n")
	return outputstring
	
def main():
	output.write("\n v4: \n")
	output.write(AvgUniquePathsPerPeer(v4))
	output.write("\n v6: \n")
	output.write(AvgUniquePathsPerPeer(v6))

if __name__ == "__main__":
	main()
