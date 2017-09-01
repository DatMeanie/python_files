#isalpha() returns True if string consists only of letters and not blanks
print('hello '.isalpha()) #would be true if not for the space
#isalnum() returns True if string consist only of letters and noumber and not blanks
print('hello123'.isalnum()) #true
#isdecimal() returns True if string consist only of numeric characters and not blanks
print('123'.isdecimal()) #true
#isspace() returns True if string consist only of spaces, tabs and new lines and is not blank
print(' '.isspace()) #true
#istitle() returns True if string consist only of words that begin with \
#an uppercase letter and followed by lowercase
print('Title'.istitle()) #true
print('NotTitle'.istitle()) #false
print('This Is Title'.istitle()) #true

