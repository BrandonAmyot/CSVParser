import csv
# Get cookie domain names
with open('CSV/Test_HomeNetwork/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    homeCookies = []
    for row in reader:
        homeCookies.append(row['baseDomain'])
    homeCookies = list(set(homeCookies))

with open('CSV/Test_Starbucks/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    publicCookies = []
    for row in reader:
        publicCookies.append(row['baseDomain'])
    publicCookies = list(set(publicCookies))

###############################################################################

difference = list(set(publicCookies) - set(homeCookies))

for list in difference:
    print (list)