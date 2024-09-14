def generate_data_sources(target_info):
    MergedName = f"{target_info['firstname']}-{target_info['lastname']}"
    
    truepeople = f"https://www.truepeoplesearch.com/results?name={target_info['firstname']}%20{target_info['lastname']}&citystatezip={target_info['state']}"
    findpeoplefast = f"https://findpeoplefast.net/people/{MergedName}/{target_info['stateabbr']}"
    publicdatausa = f"https://www.publicdatausa.com/{MergedName}"
    radaris = f"https://radaris.com/ng/search?ff={target_info['firstname']}&fl={target_info['lastname']}&fs={target_info['state']}&fc={target_info['city']}"
    spokeo = f"https://www.spokeo.com/{MergedName}?loaded=1"
    peoplefinders = f"https://www.peoplefinders.com/people/{MergedName}/{target_info['stateabbr']}?landing=people"
    unmask = f"https://unmask.com/searching/?aid=25&firstName={target_info['firstname']}&lastName={target_info['lastname']}&city={target_info['city']}&state={target_info['stateabbr']}"
    peekyou = f"https://www.peekyou.com/{target_info['firstname']}_{target_info['lastname']}"
    zabasearch = f"https://www.zabasearch.com/people/{target_info['firstname']}+{target_info['lastname']}/{target_info['city']}+{target_info['stateabbr']}/"

    return [truepeople, findpeoplefast, publicdatausa, radaris, spokeo, peoplefinders, unmask, peekyou, zabasearch]

def generate_phone_sources(phonenumber):
    phonelookup = f"https://www.phonelookup.com/1/{phonenumber}"
    reversephonewhitepages = f"https://www.whitepages.com/phone/1-{phonenumber}"
    
    return [phonelookup, reversephonewhitepages]
