#! python 3
#return true or false based on a prexisting pattern
#a phone number is 3 numbers, a hyphen, 3 numbers, a hyphen, 4 numbers

def phonenumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(phonenumber('415-555-4242'))
print('"banana is a very funny meme" is a phone number:')
print(phonenumber('banana is very funny meme'))
print('666-333-414 is a phone number')
print(phonenumber('666-333-414'))

print(' ')

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office'
print(message)
for i in range(len(message)):
    chunk = message[i:i+12]
    if phonenumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
