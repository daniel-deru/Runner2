import re

websiteReg = "^(https?://)|(www\.).+\."

websites = ["https://auth.geeksforgeeks.org/roadBlock.php", "https://www.w3schools.com/python/python_regex.asp", "https://www.google.com/search?q=python+regex+metacharacters&oq=python+regex+meta&aqs=chrome.0.0i512j69i57j0i22i30l4.31594j0j15&sourceid=chrome&ie=UTF-8", "https://oxygeninacan.co.za/", "www.google.com"]

for website in websites:
    match = re.match(websiteReg, website)
    if match != None:
        print(f"match: {website}")
    if match == None:
        print(f"no match: {website}")