# OSINTProfiler - Open Source Intelligence Profiler
# Created By: Brad Voris
# Updated Code and cleanup BY: PythonHacker24 (Aditya Patil)
# Version: 0.09
# Date Modified 14/09/2025
# Requirements: requests, types-requests, & BeautifulSoup4
# Description: This tool gathers information from the end user about a specific target. First name, last/surname, location, etc. are gathered to generate a list and
# scrape specific websites to gather additional information about the target. This is a reconnaissance tool that can be used by red teams to help facilitate penetration testing through social engineering.

from input_data import gather_target_info, display_target_info
from data_sources import generate_data_sources, generate_phone_sources
from report_generator import generate_report, clean_up_report, generate_phone_report

# Title and Disclaimer
titlescreen = """
..#######...######..####.##....##.########.########..########...#######..########.####.##.......########.########.
.##.....##.##....##..##..###...##....##....##.....##.##.....##.##.....##.##........##..##.......##.......##.....##
.##.....##.##........##..####..##....##....##.....##.##.....##.##.....##.##........##..##.......##.......##.....##
.##.....##..######...##..##.##.##....##....########..########..##.....##.######....##..##.......######...########.
.##.....##.......##..##..##..####....##....##........##...##...##.....##.##........##..##.......##.......##...##..
.##.....##.##....##..##..##...###....##....##........##....##..##.....##.##........##..##.......##.......##....##.
..#######...######..####.##....##....##....##........##.....##..#######..##.......####.########.########.##.....##
Version: 0.09
BY: BRAD VORIS
Updated Code and cleanup BY: PythonHacker24 (Aditya Patil)\n
"""

disclaimer = """Disclaimer: The author of the project as not responible for any misuse of the gathered information.\n"""
description = """
Description: This tool gathers information from the end user about a specific target. First name, last name, location, etc. are gathered to generate a list and
scrape specific websites to gather additional information about the target. This is a reconnaissance tool that can be used by red teams to help facilitate penetration testing through social engineering.\n
"""

menu = """
0: Exit
1: Input Target Profile Information
2: Display Target Profile Information
3: Display Generated Profile Links
4: Generate Target Profile Reports
"""

# Security Evasion techniques for Requests
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    "Upgrade-Insecure-Requests": "1", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8", 
    "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
cookies = {'cookies_are': 'nom nom nom so good'}

# Application Section
print(titlescreen)
print(disclaimer)
print(description)
input("Press enter to continue...")

# Main loop
done = False
target_info = {}
datalist = []
phonedatalist = []

while not done:
    print(menu)
    selection = input("Please make a selection: ")
    print()
    
    if selection == "0":
        done = True
        break

    elif selection == "1":
        target_info = gather_target_info()
        datalist = generate_data_sources(target_info)
        phonedatalist = generate_phone_sources(target_info["phonenumber"])
        input("\nPress Enter to return to the menu...")

    elif selection == "2":
        display_target_info(target_info)
        input("Press Enter to return to the menu...")

    elif selection == "3":
        print("Display Links for Profile Reports \n")
        if not datalist:
            print("Links not found .... please provide more information")
        for url in datalist:
            print(url)
        input("\nPress Enter to return to the menu...")

    elif selection == "4":
        generate_report(target_info, datalist, headers, cookies)
        clean_up_report(target_info["firstname"], target_info["lastname"])
        generate_phone_report(target_info, phonedatalist, headers, cookies)
        input("Press Enter to return to the menu...")

    else:
        print("Invalid input, select the provided options .... ")

print("Closing OSINTProfiler...")
