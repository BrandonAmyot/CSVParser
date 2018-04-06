import csv
# Get cookie domain names
with open('CSV/Test_HomeNetwork/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    homeNetworkCookies = []
    for row in reader:
        homeNetworkCookies.append(row['baseDomain'])

with open('CSV/Test_Starbucks/profile_cookies.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    starbucksCookies = []
    for row in reader:
        starbucksCookies.append(row['baseDomain'])

###############################################################################
    
    for list in homeNetworkCookies:
        print (list)

    print("\n******STARBUCKS******")

    for list in starbucksCookies:
        print (list)