#! python 3
#phonenumber function remastered, regex test
import re

phonenumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #\d means search for digit
print('My number is 415-555-4244')
mo = phonenumRegex.search('My number is 415-555-4244') #searching and returns match
if mo != None:
    print('Phone number found: ' + mo.group()) #the match is returned and translated into the string found
else:
    print('Nothing was found')
while True:
    ss = phonenumRegex.search(str(input()))
    if ss != None:
        print('it is a phone number')
    else:
        print('it is not a phone number')
