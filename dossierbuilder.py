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
print(titlescreen)
print()
print(disclaimer)
input()
firstname = input("What is the target's first name? ")
lastname = input("What is the target's last/surname? ")
state =  input("What is the target's state? ")
stateabbr = input("What is the target's state abbreviation? ")
city = input("What is the target's city ")
MergedName = firstname + '-' + lastname
truepeople = str(f'https://www.truepeoplesearch.com/results?name={firstname}%20{lastname}&citystatezip={state}')
usphonebook = str(f'https://www.usphonebook.com/{MergedName}')
findpeoplefast = str(f'https://findpeoplefast.net/people/{MergedName}/{stateabbr}')
publicdatausa = str(f'https://www.publicdatausa.com/{MergedName}')
spokeo = str(f'https://www.spokeo.com/{MergedName}?loaded=1')
peoplefinders = str(f'https://www.peoplefinders.com/people/{MergedName}/{stateabbr}?landing=people')
whitepages = str(f'https://www.whitepages.com/name/{MergedName}/{stateabbr}?fs=1&searchedName={firstname}%20{lastname}&searchedLocation={state}')
searchpeoplefree = str(f'https://www.searchpeoplefree.com/find/{MergedName}/{stateabbr}/{city}')
datalist = [truepeople, usphonebook, findpeoplefast, publicdatausa, spokeo, peoplefinders, whitepages, searchpeoplefree]
print()
print("Compiled Search Links listed Below...")
print()
for url in datalist:
    print(url)
print("Complete!")


