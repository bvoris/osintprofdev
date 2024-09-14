import requests
from bs4 import BeautifulSoup

def generate_report(target_info, datalist, headers, cookies):
    print("Generating Target Profile HTML Report")
    
    with open(f"{target_info['firstname']}_{target_info['lastname']}_Profile.html", "w") as f:
        f.write("<html>\n<body>\n")
        f.write(f"<h2>{target_info['firstname']} {target_info['lastname']} - Target Profile Report</h2>\n")
        
        for url in datalist:
            f.write(f"<p><a href='{url}' target='_blank'>{url}</a></p>\n")
        
        f.write("</body>\n</html>")
    print("Report generation completed.")

def clean_up_report(firstname, lastname):
    print("Cleaning Up the Report....")
    
    html_file = f"{firstname}_{lastname}_Profile.html"
    
    with open(html_file, "r") as file:
        soup = BeautifulSoup(file, "html.parser")
        
        for tag in soup.find_all("a"):
            tag["target"] = "_blank"
            
    with open(html_file, "w") as file:
        file.write(str(soup.prettify()))

def generate_phone_report(target_info, phonedatalist, headers, cookies):
    print("Generating Target Phone Information Report")
    
    with open(f"{target_info['firstname']}_{target_info['lastname']}_Phone_Report.html", "w") as f:
        f.write("<html>\n<body>\n")
        f.write(f"<h2>{target_info['firstname']} {target_info['lastname']} - Phone Report</h2>\n")
        
        for url in phonedatalist:
            f.write(f"<p><a href='{url}' target='_blank'>{url}</a></p>\n")
        
        f.write("</body>\n</html>")
    print("Phone report generation completed.")

