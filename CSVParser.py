import csv
home = 'Test_HomeNetwork'
public = 'Test_Concordia'

# Get cookie domain names from home network
with open('CSV/'+home+'/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    homeCookies = []
    for row in reader:
        homeCookies.append(row['baseDomain'])
    homeCookies = set(homeCookies)

# Get cookie domain names from public network
with open('CSV/'+public+'/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    publicCookies = []
    for row in reader:
        publicCookies.append(row['baseDomain'])
    publicCookies = set(publicCookies)

# Find and print cookies present on public networks that are not present on home networks
cookieDifference = (set(publicCookies) - set(homeCookies))
for list in cookieDifference:
    print (list)

# Get 3rd party scripts
with open('CSV/'+home+'/http_responses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    homeScripts = []
    for row in reader:
        if row['url'].endswith('.js'):
            homeScripts.append(row['url'])
    homeScripts = set(homeScripts)

for list in homeScripts:
    print(list)

# Get 3rd party scripts
with open('CSV/'+public+'/http_responses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    publicScripts = []
    for row in reader:
        if row['url'].endswith('.js'):
            publicScripts.append(row['url'])
    publicScripts = set(publicScripts)

scriptDifference = (set(publicScripts) - set(homeScripts))
for list in scriptDifference:
    print (list)

# finalResult = cookieDifference.j

file = open('output.txt', 'w')
file.write('COOKIES\n')
file.write(', \n'.join(cookieDifference))
file.close()
file = open('output.txt', 'a')
file.write('\n\n3RD PARTY SCRIPTS\n')
file.write(', \n'.join(scriptDifference))
file.close()