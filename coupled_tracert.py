# Author:	Dylan Ruggeroli
# Date:		1/23/2015
# Desc:		Implements subprocess to run two tracerts for a given domain
#			(one for IPv4 and another for IPv6). Results are stored in a
#			text file.

import subprocess, sys, time

dest = sys.argv[1]
date = time.strftime("%m_26")
date = dest + '_' + date + '.txt'
text_file = open(date, "a")

# Accepts the string result of a tracert command and returns a list of
# tuples containing hop number, URL, and IP
def parse_trace(file_string):
	split = file_string.split(' ')

	ip_list = []
	hop_count = 0
	parse_counter = 0
	elmt_counter = -1

	for i in split:
		elmt_counter += 1
		if parse_counter == 3:
			hop_count +=1
			parse_counter = 0

			# URL and IP address values respectively
			j = split[elmt_counter + 1]
			k = split[elmt_counter + 2]

			# If k is empty, no URL was provided
			if k == '\r\n' or not k:
				k = j

				# If both j and k are empty, the request timed out
				if not j:
					k = "Request timed out"

				j = "URL not provided"

			ip_list.append((hop_count, j, k))

		# Track upcoming URL/IP pairs
		if i == 'ms' or i == '*':
			parse_counter += 1

	return ip_list


bytes_for_six  = subprocess.check_output(["tracert", "-6", dest])
bytes_for_four = subprocess.check_output(["tracert", "-4", dest])

string_for_six = bytes_for_six.decode('utf-8')
string_for_four = bytes_for_four.decode('utf-8')

six_list = parse_trace(string_for_six)
four_list = parse_trace(string_for_four)

text_file.write('Results for ' + dest + ':\n --- IPv6 \n')
for (x,y,z) in six_list:
	line = x,y,z
	text_file.write(str(line))
	text_file.write('\n')

text_file.write('\n--- IPv4 \n')
for (x,y,z) in four_list:
	line = x,y,z
	text_file.write(str(line))
	text_file.write('\n')

text_file.close()