from utils import get_state_abbreviation

def gather_target_info():
    print("Input Target Profile Information")
    print("Instructions: Let's gather some information about your target.")
    print("First name, last name, state, and state abbreviation should be lower case.")
    print("Phone number should be formatted as 555-555-5555")
    print("Email Address should be formatted as name@website.com\n")
    
    firstname = input("What is the target's first name? ").strip().lower()
    lastname = input("What is the target's last/surname? ").strip().lower()
    
    country = input("What country is the target in? Enter 'usa' for United States: ").strip().lower()
    
    if country == "usa":
        state = input("What is the target's state? ").strip().lower()
        stateabbr = get_state_abbreviation(state)
        if stateabbr == "invalid":
            print("Invalid state information")
    else:
        state = "none"
        stateabbr = "none"

    city = input("What is the target's city? ").strip().lower()
    phonenumber = input("What is the target's phone number? ").strip()

    emailaddress = ""
    while True:
        emailaddress = input("What is the target's email address? ").strip()
        if '@' in emailaddress:
            break
        print('\nInvalid email address, please try again ....')

    return {
        "firstname": firstname,
        "lastname": lastname,
        "country": country,
        "state": state,
        "stateabbr": stateabbr,
        "city": city,
        "phonenumber": phonenumber,
        "emailaddress": emailaddress
    }

def display_target_info(target_info):
    comma = ", " if target_info["state"] else ""
    print(f"\nTarget Name: {target_info['firstname']} {target_info['lastname']}")
    print(f"Target Location: {target_info['city']}{comma}{target_info['state']}")
    print(f"Target Phone Number: {target_info['phonenumber']}")
    print(f"Target Email Address: {target_info['emailaddress']}\n")
