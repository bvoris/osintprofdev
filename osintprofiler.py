# OSINTProfiler - Open Source Intelligence Profiler
# Created By: Brad Voris
# Version: 0.05
# Requirements: requests, types-requests, & BeautifulSoup4 
# Description: This tool gathers information from the end user about a specific target. First name, last/surname, location, etc. are gathered to generate a list and
# scrape specific websites to gather additional information about the target. This is a reconnaissance tool that can be used by red teams to help facilitate penetration testing through social engineering.
#

# Import Section
import requests
from bs4 import BeautifulSoup
# Title and Disclaimer
titlescreen = """
..#######...######..####.##....##.########.########..########...#######..########.####.##.......########.########.
.##.....##.##....##..##..###...##....##....##.....##.##.....##.##.....##.##........##..##.......##.......##.....##
.##.....##.##........##..####..##....##....##.....##.##.....##.##.....##.##........##..##.......##.......##.....##
.##.....##..######...##..##.##.##....##....########..########..##.....##.######....##..##.......######...########.
.##.....##.......##..##..##..####....##....##........##...##...##.....##.##........##..##.......##.......##...##..
.##.....##.##....##..##..##...###....##....##........##....##..##.....##.##........##..##.......##.......##....##.
..#######...######..####.##....##....##....##........##.....##..#######..##.......####.########.########.##.....##
BY: BRAD VORIS
"""
disclaimer ="""
I am not responsible for how you use the information gathered from OSINTPROFILER. Use this tool responsibly.
"""
# Description
description = """
Description: This tool gathers information from the end user about a specific target. First name, last/surname, location, etc. are gathered to generate a list and
scrape specific websites to gather additional information about the target. This is a reconnaissance tool that can be used by red teams to help facilitate penetration testing through social engineering.
"""
# Menu based interface
menu = """
0: Exit
1: Input Target Profile Information
2: Display Target Profile Information
3: Display Generated Profile Links
4: Generate Target Profile Reports
"""

# Application Section
print(titlescreen)
print()
print(disclaimer)
print()
print(description)
print()
input()
# While loop that runs the menu and application
done = False
while not done:
    print(menu)
    selection = input("Please make a selection: ")
    print()
    if selection == "0":
        done == True
        break
    elif selection == "1":
# End user instructions
        print("Input Target Profile Information")
        print("Instructions: Lets gather some information about your target.")
        print("First name, last name, state, and state abbreviation should be lower case, do not include spaces.")
        print("Phone number should be formatted as 555-555-5555")
        print("Email Address should be formatted as name@website.com")
        print()
# These are the variables that are input from the end user
        firstname = input("What is the target's first name? ")
        lastname = input("What is the target's last/surname? ")
        state =  input("What is the target's state? ")
        stateabbr = input("What is the target's state abbreviation? ")
        city = input("What is the target's city? ")
        phonenumber = input("What is the target's phone number? ")
        emailaddress = input("What is the  target's email address? ")
        MergedName = firstname + '-' + lastname
# These are the variables scoped for scrapping sites of PII
# Data sources
        truepeople = str(f'https://www.truepeoplesearch.com/results?name={firstname}%20{lastname}&citystatezip={state}')
        usphonebook = str(f'https://www.usphonebook.com/{MergedName}')
        findpeoplefast = str(f'https://findpeoplefast.net/people/{MergedName}/{stateabbr}')
        publicdatausa = str(f'https://www.publicdatausa.com/{MergedName}')
        spokeo = str(f'https://www.spokeo.com/{MergedName}?loaded=1')
        peoplefinders = str(f'https://www.peoplefinders.com/people/{MergedName}/{stateabbr}?landing=people')
        whitepages = str(f'https://www.whitepages.com/name/{MergedName}/{stateabbr}?fs=1&searchedName={firstname}%20{lastname}&searchedLocation={state}')
        searchpeoplefree = str(f'https://www.searchpeoplefree.com/find/{MergedName}/{stateabbr}/{city}')
        unmask = str(f'https://unmask.com/searching/?aid=25&firstName={firstname}&lastName={lastname}&city={city}&state=stateabbr')
        peekyou = str(f'https://www.peekyou.com/{firstname}_{lastname}')
# This is the python data list used to generate onscreen lists and reports
        datalist = [truepeople, usphonebook, findpeoplefast, publicdatausa, spokeo, peoplefinders, whitepages, searchpeoplefree, unmask, peekyou]
        print()
        input("Press Enter to return to the menu...")
    elif selection == "2":
        print("Display Target Profile Information")
        print()
        print(f'Target Name: {firstname} {lastname}')
        print(f'Target Location: {city},{state}')
        print(f'Target Phone Number: {phonenumber}')
        print(f'Target Email Address: {emailaddress}')
        print()
        input("Press Enter to return to the menu...")
    elif selection == "3":
        print("Display Links for Profile Reports ")
        print()
        for url in datalist:
            print(url)
        print()
        input("Press Enter to return to the menu...")
    elif selection == "4":
        print("Generate Target Profile Reports")
        for url in datalist:
            page = requests.get(url)
            print(page.text)
            # Creating an HTML file
            Func = open("userreport.html","w", encoding="utf-8")
# Adding input data to the HTML file
            Func.write(f'<html>\n<head>\n<title>OSINTProfiler Report</title>\n</head> <body><h1>OSINTProfile - Open Source Intelligence Profiler Report</h1><B>Created by: Brad Voris</B><BR/><BR/><I>{disclaimer}</I><BR/><I>{description}</I><BR/><BR/><B>Identified Target:</B> {lastname}, {firstname}<BR/><B>Target Location:</B> {city},{state}<BR/><B>Target Phone Number:</B> {phonenumber}<BR/><B>Target Email Address:</B> {emailaddress}<BR/><BR/><B>Web Urls Dictionary</B><BR/><UL><li><a href="{truepeople}" target="_blank" rel="noopener noreferrer">{truepeople}</a></li><li><a href="{usphonebook}" target="_blank" rel="noopener noreferrer">{usphonebook}</a></li><li><a href="{findpeoplefast}" target="_blank" rel="noopener noreferrer">{findpeoplefast}</A></li><li><a href="{publicdatausa}" target="_blank" rel="noopener noreferrer">{publicdatausa}</A></li><li><a href="{spokeo}" target="_blank" rel="noopener noreferrer">{spokeo}</A></li><li><a href="{peoplefinders}" target="_blank" rel="noopener noreferrer">{peoplefinders}</A></li><li><a href="{whitepages}" target="_blank" rel="noopener noreferrer">{whitepages}</A></li><li><a href="{searchpeoplefree}" target="_blank" rel="noopener noreferrer">{searchpeoplefree}</A></li><li><a href="{unmask}" target="_blank" rel="noopener noreferrer">{unmask}</A></li><li><a href="{peekyou}" target="_blank" rel="noopener noreferrer">{peekyou}</A></li></ul><BR/>\\n {page.text} \n</body></html>')
# Saving the data into the HTML file
            Func.close()
            #soup = BeautifulSoup(response.text, 'html.parser')
            #print(soup.text)
        print()
        input("Press Enter to return to the menu...")
    else:
        print("Please select 0, 1, 2, or 3")



states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}

print("Closing OSINTProfiler...")




