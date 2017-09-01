#! python 3
#group functionality
import re
phonenumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phonenumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups())

print(' ')

areacode, mainnum = mo.groups()
print(mainnum)
print(areacode)
