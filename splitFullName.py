import csv
from main import searchFile

base_dir = 'Result'
email_base = searchFile(base_dir)

def readFile():
	with open(f'{base_dir}/{email_base}', 'r') as file:
		number_string = 0
		for row in csv.DictReader(file):
			number_string+=1
			name = row['Name']
			email = row['Email']
			company = row['Company']
			print(f'[{number_string}] {name}, {email}, {company}')


readFile()