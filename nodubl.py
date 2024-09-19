import csv
from collections import defaultdict
from main import searchFile

result_dir = 'Result'
base_dir = 'Base'
domain_dict = {}

email_base = searchFile(base_dir)

with open(f'{base_dir}/{email_base}', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row['Email']
        domain = email.split('@')[-1]
        # Сохраняем первый email для каждого уникального домена, включая gmail.com
        if domain not in domain_dict:
            domain_dict[domain] = row

with open(f'{result_dir}/NoRepit_{email_base}', 'w', newline='') as csvfile:
    fieldnames = ['Company', 'Email', 'Name' ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in domain_dict.values():
        writer.writerow({'Company': data['Company'], 'Email': data['Email'], 'Name': data['Name'] })