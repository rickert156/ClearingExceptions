import os, csv

result_dir = 'Result'
list_exeption_domain = 'exception_domain.txt'
list_exeption_email = 'exception_email.txt'
exception_dir = 'Exceptions'
base_dir = 'Base'
all_exceptions = [list_exeption_domain, list_exeption_email]

if not os.path.exists(result_dir):
	os.makedirs(result_dir)

def writeEx(open_file_base, email):
	with open(f'{result_dir}/{open_file_base}', 'a+') as file:
		file.write(f'{email}\n')

def searchFile(base_dir):
	list_file_base = []
	for search_bases in os.listdir(base_dir):list_file_base+=[search_bases]

	number_file = 0
	for list_file in list_file_base:
		number_file+=1
		print(f'[{number_file}] {list_file}')

	try:
		find_base = int(input('\nВыбери номер файла: '))
		if find_base < 1:
			enter_list = list_file_base[0]
			print(enter_list)
			return enter_list
		else:
			enter_list = list_file_base[find_base-1]
			print(enter_list)
			return enter_list	
	except Exception as ex:
		print(f'\nCode Error: {ex}\nПопробуй еще раз...\n')
		searchFile(base_dir)
		

def cleaning():
	emails = []
	open_file_base = searchFile(base_dir)
	with open(f'{base_dir}/{open_file_base}', 'r') as file_base:
		for row in csv.DictReader(file_base):
			email_base = row['Email']
			emails.append(email_base)

	# Чтение списка исключаемых доменов и проверка каждого email
	with open(f'{exception_dir}/{list_exeption_domain}') as file:
		number_domain = 0
		for domain in file.readlines():
			domain = domain.strip()
			for email in emails:
				if domain in email:
					number_domain += 1
					print(f'[ Domain {number_domain} ] {email}')
					writeEx(open_file_base, email)
					break 


	with open(f'{exception_dir}/{list_exeption_email}') as file2:
		number_email = 0
		for email_ex in file2.readlines():
			email_ex = email_ex.strip()
			if email_ex in emails:
				number_email+=1
				print(f'[ Email {number_email}] {email_ex}')
				writeEx(open_file_base, email_ex)

if __name__ == '__main__':
	try:
		cleaning()
	except Exception as ex:
		print(f'\nError: {ex}\n')
		cleaning()