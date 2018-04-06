import csv
with open('profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    baseDomainNames = []
    for row in reader:
        baseDomainNames.append(row['baseDomain'])

    for list in baseDomainNames:
        print (list)