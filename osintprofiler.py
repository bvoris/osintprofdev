# OSINTProfiler - Open Source Intelligence Profiler
# Created By: Brad Voris
# Version: 0.05
# Requirements: requests, types-requests, & BeautifulSoup4 
# Description: This tool gathers information from the end user about a specific target. First name, last/surname, location, etc. are gathered to generate a list and
# scrape specific websites to gather additional information about the target. This is a reconnaissance tool that can be used by red teams to help facilitate penetration testing through social engineering.
#

# Import Section
import requests
import cloudscraper
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

# HTML Out preloaded variable
datalisthtmlout = ''
phonedatalisthtmlout = ''
emaildatalisthtmlout = ''

# Security Evasion techniques for Requests should be here
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36","Upgrade-Insecure-Requests": "1", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"}
cookies = {'cookies_are': 'nom nom nom so good'}
#, proxies={'http': proxy,'https': proxy})

# Application Section
print(titlescreen)
print()
print(disclaimer)
print()
print(description)
print()
input("Press enter to continue...")

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
        print("First name, last name, state, and state abbreviation should be lower case.")
        print("Phone number should be formatted as 555-555-5555")
        print("Email Address should be formatted as name@website.com")
        print()
        
# These are the variables that are input from the end user
        firstname = input("What is the target's first name? ")
        print()
        lastname = input("What is the target's last/surname? ")
        print()
        countrya = input("What country is the target in? Enter 'usa' for United States:  ")
        country = countrya.replace(" ", "")
        print()
        if country == "usa":
            statea =  input("What is the target's state? ")
            state = statea.replace(" ", "")
            print()
            stateabbra = input("What is the target's state abbreviation? ")
            stateabbr = stateabbra.replace(" ", "")
            print()
        else:
            state = "none"
            stateabbr = "none"            
        citya = input("What is the target's city? ")
        city = citya.replace(" ", "")
        print()
        phonenumber = input("What is the target's phone number? ")
        print()
        emailaddress = input("What is the target's email address? ")
        print()
        MergedName = firstname + '-' + lastname

# Data sources that pass the variables from user input
        truepeople = str(f'https://www.truepeoplesearch.com/results?name={firstname}%20{lastname}&citystatezip={state}')
        usphonebook = str(f'https://www.usphonebook.com/{MergedName}')
        findpeoplefast = str(f'https://findpeoplefast.net/people/{MergedName}/{stateabbr}')
        publicdatausa = str(f'https://www.publicdatausa.com/{MergedName}')
        spokeo = str(f'https://www.spokeo.com/{MergedName}?loaded=1')
        peoplefinders = str(f'https://www.peoplefinders.com/people/{MergedName}/{stateabbr}?landing=people')
        whitepages = str(f'https://www.whitepages.com/name/{MergedName}/{stateabbr}?fs=1&searchedName={firstname}%20{lastname}&searchedLocation={state}')
        searchpeoplefree = str(f'https://www.searchpeoplefree.com/find/{MergedName}/{stateabbr}/{city}')
        unmask = str(f'https://unmask.com/searching/?aid=25&firstName={firstname}&lastName={lastname}&city={city}&state={stateabbr}')
        peekyou = str(f'https://www.peekyou.com/{firstname}_{lastname}')
        zabasearch = str(f'https://www.zabasearch.com/people/{firstname}+{lastname}/{city}+{stateabbr}/')
        intelius = str(f'https://www.intelius.com/search/?firstName={firstname}&lastName={lastname}&city={city}&state={stateabbr}')
        fastpeoplesearch = str(f'https://www.fastpeoplesearch.com/name/{firstname}-{lastname}_{city}-{state}')
        phonelookup = str(f'https://www.phonelookup.com/1/{phonenumber}')
        reversephonewhitepages = str(f'https://www.whitepages.com/phone/1-{phonenumber}')
        
# This is the list used to generate onscreen lists and reports
        datalist = [truepeople, usphonebook, findpeoplefast, publicdatausa, spokeo, peoplefinders, whitepages, searchpeoplefree, unmask, peekyou, zabasearch, intelius, fastpeoplesearch]
        phonedatalist = [phonelookup, reversephonewhitepages]
        
        print()
        input("Press Enter to return to the menu...")
    elif selection == "2":
# This Displays the Target Profile Information from User Input
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
# For loop for gathering PII data from URLs in the dictionary
        for url in datalist:
            page = requests.get(url, headers=headers, cookies=cookies)
# Exported Data from website parsing, appended to datalisthtmlout as a very large string, to be passed in func.write statement
            datalisthtmlout += str(page.text)
# Creating an HTML file
        Func = open("userreport.html","w", encoding="utf-8")
# Adding input data to the HTML file & Saving the data into the HTML file
# The override.css file is added to bypass additional CSS dumped from web scrape
        Func.write(f'<html><head><title>OSINTProfiler Report</title><STYLE><link rel="stylesheet" href="override.css"></STYLE></head><body><h1>OSINTProfiler - Open Source Intelligence Profiler: Target Report</h1><B>Created by: Brad Voris</B><BR/><BR/><I>{disclaimer}</I><BR/><I>{description}</I><BR/><BR/><B>Identified Target:</B> {lastname}, {firstname}<BR/><B>Target Location:</B> {city},{state}<BR/><B>Target Phone Number:</B> {phonenumber}<BR/><B>Target Email Address:</B> {emailaddress}<BR/><BR/><B>Web Urls Dictionary</B><BR/><UL><li><a href="{truepeople}" target="_blank" rel="noopener noreferrer">{truepeople}</a></li><li><a href="{usphonebook}" target="_blank" rel="noopener noreferrer">{usphonebook}</a></li><li><a href="{findpeoplefast}" target="_blank" rel="noopener noreferrer">{findpeoplefast}</A></li><li><a href="{publicdatausa}" target="_blank" rel="noopener noreferrer">{publicdatausa}</A></li><li><a href="{spokeo}" target="_blank" rel="noopener noreferrer">{spokeo}</A></li><li><a href="{peoplefinders}" target="_blank" rel="noopener noreferrer">{peoplefinders}</A></li><li><a href="{whitepages}" target="_blank" rel="noopener noreferrer">{whitepages}</A></li><li><a href="{searchpeoplefree}" target="_blank" rel="noopener noreferrer">{searchpeoplefree}</A></li><li><a href="{unmask}" target="_blank" rel="noopener noreferrer">{unmask}</A></li><li><a href="{peekyou}" target="_blank" rel="noopener noreferrer">{peekyou}</A></li><li><a href="{zabasearch}" target="_blank" rel="noopener noreferrer">{zabasearch}</A></li><li><a href="{intelius}" target="_blank" rel="noopener noreferrer">{intelius}</A></li><li><a href="{fastpeoplesearch}" target="_blank" rel="noopener noreferrer">{fastpeoplesearch}</A></li></ul><BR />Phone Report: <a href="phonereport.html" target="_blank" rel="noopener noreferrer">Click here for phone report</a><BR/>{datalisthtmlout}</body></html>')
# Closing the file
        Func.close()
        print()
# For loop for gathering data from Phone number URLs in the dictionary
        for url in phonedatalist:
            page = requests.get(url, headers=headers, cookies=cookies)
# Exported Data from website parsing, appended to phonedatalisthtmlout as a very large string, to be passed in func.write statement
            phonedatalisthtmlout += str(page.text)
# Creating an HTML file for phone report
        Func = open("phonereport.html","w", encoding="utf-8")
# Adding input data to the HTML file & Saving the data into the HTML file
        Func.write(f'<html><head><title>OSINTProfiler Report</title></head> <body><h1>OSINTProfile - Open Source Intelligence Profiler: Phone Number Report</h1><B>Created by: Brad Voris</B><BR/><BR/><I>{disclaimer}</I><BR/><I>{description}</I><BR/><BR/><B>Identified Target:</B> {lastname}, {firstname}<BR/><B>Target Location:</B> {city},{state}<BR/><B>Target Phone Number:</B> {phonenumber}<BR/><B>Target Email Address:</B> {emailaddress}<BR/><BR/><B>Web Urls Phone Lookup Dictionary</B><BR/><UL><li><a href="{phonelookup}" target="_blank" rel="noopener noreferrer">{phonelookup}</a></li><li><a href="{reversephonewhitepages}" target="_blank" rel="noopener noreferrer">{reversephonewhitepages}</a></li><BR/>{phonedatalisthtmlout}</body></html>')
# Closing the file
        Func.close() 
        input("Press Enter to return to the menu...")               
    else:
        print("Please select 0, 1, 2, 3, or 4... ")

print("Closing OSINTProfiler...")




