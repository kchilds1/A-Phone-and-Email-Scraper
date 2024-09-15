#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
#types of numbers I want ex. 111-111-1111, 111-1111, (111) 111-1111, or 111-1111 ext. 12345, x12345
(
    ((\d{3})|(\(\d{3}))?   # area code optional and could appear 0 or 1 times
    (\s|-)    #first separator
    \d{3}    #first 3 digits
    -    #second separator
    \d{4}   #last 4 digits
    ((ext(\.)?\s)|x)?   # extension optional where it could say ext with or without . or could contain x 
    (\d{2,5})?) #extension could be 2 to 5 digits         
               ''', re.VERBOSE)

# Create a regex for email addresses
emailRegex = re.compile(r'''
# something@something.com,something_something@something.com, something.something@something.com,something+something@something.com

    [a-zA-Z0-9_.+?]+ #name part-this can contain lowercase,uppercase, numbers, and the following symbols _.+?
    @ #@ symbol
    [a-zA-Z0-9_.+?]+ # Domain name part-this can contain lowercase,uppercase, numbers, and the following symbols _.+?              
    ''', re.VERBOSE)

# Get the text off the clipboard
text = 'Clinton Hernandez chernandez16@yahoo.com 303-606-9242 Sylvester Goodman sylvesterg@comcast.net 419-691-5429 Efren Daniels edaniels@comcast.net 740-228-1291 ' # whatever I have in my clipboard will be pasted to text

# pyperclip.paste()
# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
print (allPhoneNumbers)
# print(extractedEmail)
# print(extractedPhone)

