import csv
from collections import defaultdict

domain_dict = {}

with open('emails.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        email = row['Email']
        domain = email.split('@')[-1]
        # Сохраняем первый email для каждого уникального домена, включая gmail.com
        if domain not in domain_dict:
            domain_dict[domain] = row

with open('nodubl.csv', 'w', newline='') as csvfile:
    fieldnames = ['Company', 'Email', 'Site' ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for data in domain_dict.values():
        writer.writerow({'Company': data['Company'], 'Email': data['Email'], 'Site': data['Site'] })