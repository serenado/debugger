import requests
import sys

#pass code file in terminal
file = sys.argv[1]

with open(file, 'r') as f:
	#send request to server 
	r = requests.post('http://127.0.0.1:5000/execute', files ={'code': f})
	
	#print all output of program execution on server
	print (r.text)


