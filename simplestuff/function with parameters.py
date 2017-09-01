#function with parameter test. also uses response variable

import sys

print('type something you like')
def something(name):
    print('you like ' + name)

while True:
    response = input()
    something(response)
    if response == 'jeff':
        sys.exit()
