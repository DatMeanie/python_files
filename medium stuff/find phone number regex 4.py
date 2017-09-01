#! python 3
#findall() method test with phone number
import re

phonenumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumRegex.search('Cell: 415-555-9999 Work: 215-420-1337')
print(mo.group()) #only returns first value

mo1 = phonenumRegex.findall('Cell: 415-555-9999 Work: 215-420-1337')
print(mo1) #all values in list, or tuple if regex has groups
print(mo1[1])

phonenumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') #grouped
mo1 = phonenumRegex.findall('Cell: 415-555-9999 Work: 215-420-1337')
print(mo1) #tuple within list
print(mo1[1])
