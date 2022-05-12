#Title Screen

#User Inputs
firstname = input("What is the target's first name?")
lastname = input("What is the target's last/surname?")
alternativename = input("What is the target's alternative name? Example: First Name Michael Alternative Name Mike")
state =  input("What is the target's state?")
stateabbr =  input("What is the target's state abbreviation?")
#middlename = input("what is the target's middle name?")
#address = input("what is the target's address?")
#city = input("What is the target's city?")
#zipcode = input("What is the target's zipcode?")
#accountusername = input("What is the target's account username?")

#Search Arrays
#MergedNameSearchCriteriaArray[0] = "https://clustrmaps.com/persons/firstname-lastname/state, https://www.usphonebook.com/firstname-lastname, https://findpeoplefast.net/people/firstname-lastname/stateabbr, https://www.publicdatausa.com/firstname-lastname"
#AlternativeNameSearchCriteriaArray[0] = "https://clustrmaps.com/persons/alternativename-lastname/state, https://www.usphonebook.com/alternativename-lastname, https://findpeoplefast.net/people/alternativename-lastname/stateabbr, https://www.publicdatausa.com/alternativename-lastname"
#AddressSearchCriteriaArray[0] = ""
#CitySearchCriteriaArray[0] = ""
#StateSearchCriteriaArray[0] = ""
#StateAbbrSearchCriteriaArray[0] = ""
#ZipCodeSearchCriteriaArray[0] = ""
#AccountUsernameSearchCriteriaArray[0] = ""

#Functions for URIs
#from urllib.request import urlopen
#url = "https://www.cyberforgesecurity.com"
#page = urlopen(url)
#html_bytes = page.read()
#html = html_bytes.decode("utf-8")
#print(html)
#start_index = html.find("h-global-transition-all") + len("h-global-transition-all")
#end_index = html.find("</div>")
#data = html[start_index:end_index]
#print(data)

#BeatifulSoup Web Scrapper
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.cyberforgesecurity.com"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
