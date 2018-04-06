import csv
home = 'Test_HomeNetwork'
public = 'Test_Starbucks'

# Get cookie domain names from home network
with open('CSV/'+home+'/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    homeCookies = []
    for row in reader:
        homeCookies.append(row['baseDomain'])
    homeCookies = list(set(homeCookies))

# Get cookie domain names from public network
with open('CSV/'+public+'/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    publicCookies = []
    for row in reader:
        publicCookies.append(row['baseDomain'])
    publicCookies = list(set(publicCookies))

# Find and print cookies present on public networks that are not present on home networks
difference = list(set(publicCookies) - set(homeCookies))
for list in difference:
    print (list)

# Get 3rd party scripts

file = open('output.txt', 'w')
file.write(', \n'.join(difference))
file.close()