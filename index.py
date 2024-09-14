#! python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
#types of numbers I want ex. 111-111-1111, 111-1111, (111) 111-1111, or 111-1111 ext. 12345, x12345

((\d\d\d)|(\(\d\d\d)))?   # area code (optional and could appear 0 or 1 times)
(\s|-)    #first separator
\d\d\d    #first 3 digits
-    #second separator
\d\d\d\d    #last 4 digits
((ext(\.)?\s)|x)   # extension (optional where it could say ext with or without . or could contain x )
(\d{2,5}))? #extension could be 2 to 5 digits         
           ''', re.VERBOSE)