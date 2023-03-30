import re

def match_text(text_data):
    pattern = 'ab{4,8}'
    if re.search(pattern, text_data):
        return "Match found"
    else:
        return ("Match not found")

def find_text(): 
    string = "Today is saturday"
    obj = re.search(r'is', string)
    print(obj.start())

def findEmail():
    email_text = "anshuman_saikia11@gmail.com"
    pattern = r'^\S+@\S+\.\S+'

    search = re.match(pattern, email_text)
    print("Valid Email ") if search else print("Not Valid")

def extractEmail():
    string1 = 'You can reach me out at hello@uibakery.io and contact@uibakery.io'
    pattern1 = r"\S+@\S+\.\S+"

    emaiList = re.findall(pattern1, string1)
    print(emaiList)

def verifyPhoneNumber():
    pattern = r'^\+?[1-9][0-9]{7,14}$'
    phoneNumber = '+919731184877'

    check = re.match(pattern, phoneNumber)
    print("Valid phone number") if check else print("Invalid phone number")

def checkPassword():
    """
        Has minimum 8 characters in length. Adjust it by modifying {8,}
    At least one uppercase English letter. You can remove this condition by removing (?=.*?[A-Z])
    At least one lowercase English letter.  You can remove this condition by removing (?=.*?[a-z])
    At least one digit. You can remove this condition by removing (?=.*?[0-9])
    At least one special character,  You can remove this condition by removing (?=.*?[#?!@$%^&*-])
    """
    pattern = r'\s?(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,14}$'
    pattern2 = r'^(d\S+){8,14}$'
    pwd = 'abACsS32sa'

    if re.match(pattern2, pwd):
        print("Strong password")
    else:
        print("Weak password")

def check_valid_email_and_retrieve():
    string1 = 'You can reach me out at hello@uibakery.io and contact@uibakery.io'
    pattern = r"[\w\.-]+@[\w\.]+"
    
    match = re.search(pattern, string1)
    if match:
        print("Valid email available in the string")
        print(match.group())

    emails = re.findall(pattern, string1)
    for email in emails:
        print(email)

findEmail()
extractEmail()
verifyPhoneNumber()
checkPassword()
check_valid_email_and_retrieve()