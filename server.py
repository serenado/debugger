from flask import Flask, request
import sys
import os

app = Flask(__name__)



@app.route('/execute', methods=['POST'])
def execute():

	#dedirect stdout to text file
	output = open('temp.txt', 'w')
	sys.stdout = output

	#take in user input
	res = request.files['code'].read().decode("utf-8")

	try:
		exec(res)

	#catching errors
	except Exception as error:
		print("Error found: " + str(error))

		if hasattr(error, 'lineno'):		#if error type has line number
			print("Check line number " + str(error.lineno))

	output.close()

	#read in temp output
	with open('temp.txt', 'r') as f:
		return f.read()

	os.remove('text.txt')


if __name__ == "__main__":
	app.run()