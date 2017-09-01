#! python3
#program to identify if you have a strong password or not
import re

passwordRegex1 = re.compile(r'[a-z]+')
passwordRegex2 = re.compile(r'[A-Z]+')
passwordRegex3 = re.compile(r'[0-9]+')
passwordRegex4 = re.compile(r'\w{8,}')
print('Want to see if your password is strong? Type it and we will see...')
while True:
    password = str(input())
    test1 = passwordRegex1.search(password)
    test2 = passwordRegex2.search(password)
    test3 = passwordRegex3.search(password)
    test4 = passwordRegex4.search(password)
    if test1 == None:
        print('Missing lowercase character')
    if test2 == None:
        print('Missing uppercase character')
    if test3 == None:
        print('Missing digit number')
    if test4 == None:
        print('Word needs to be longer')
    if test1 != None and test2 != None and test3 != None and test4 != None:
        print('It is a strong password')
