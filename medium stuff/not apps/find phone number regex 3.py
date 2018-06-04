#! python 3
#phone number regex test 3
import re
phonenumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phonenumRegex.search('My phone number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group())
