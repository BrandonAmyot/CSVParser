import csv
home = 'Test_HomeNetwork'
public = 'Test_Starbucks'

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

homeInfo = "\nHome Cookies:" + str(len(homeCookies)) + \
           "\nPublic Cookies:" + str(len(publicCookies)) + \
           "\nTotal Cookies: " + (str(len(homeCookies) + len(publicCookies)) + '\n')

# Find and print cookies present on public networks that are not present on home networks
cookieDifference = (set(publicCookies) - set(homeCookies))
for list in cookieDifference:
    print (list)

cookies_total_difference = "Cookies Difference: " + str(len(cookieDifference))
# Get 3rd party scripts
with open('CSV/'+home+'/http_responses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    homeScripts = []
    for row in reader:
        if row['url'].endswith('.js'):
            homeScripts.append(row['url'])
    homeScripts = set(homeScripts)


# Get 3rd party scripts
with open('CSV/'+public+'/http_responses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    publicScripts = []
    for row in reader:
        if row['url'].endswith('.js'):
            publicScripts.append(row['url'])
    publicScripts = set(publicScripts)

publicInfo = "\nHome Scripts: " + str(len(homeScripts)) + \
             "\nPublic Scripts: " + str(len(publicScripts)) + \
             "\nTotal Scripts: " + (str(len(homeScripts) + len(publicScripts)) +'\n')

scriptDifference = (set(publicScripts) - set(homeScripts))
for list in scriptDifference:
    print (list)

scripts_difference_total = "Scripts Difference: " + str(len(scriptDifference))
# finalResult = cookieDifference.j

file = open('output'+ public + '.txt', 'w')
file.write('COOKIES\n')
file.write(', \n'.join(cookieDifference))
file.write('\n\n***COOKIES INFO***')
file.write(homeInfo)
file.write(cookies_total_difference)
file.close()
file = open('output'+ public + '.txt', 'a')
file.write('\n\n3RD PARTY SCRIPTS\n')
file.write(', \n'.join(scriptDifference))
file.write('\n\n***SCRIPTS INFO***')
file.write(publicInfo)
file.write(scripts_difference_total)
file.close()