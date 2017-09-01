spam = "my name's jeff"
print(spam)
spam = 'my name\'s jeff'
print(spam)
spam = "\"my name jeff\" is a quote from the movie 22 jump street "
print(spam)
spam = 'my \nname \njeff'
print(spam)
print(r'my \nname \njeff') #raw string, ignores escape characters
print(' ')
print('''hello

my name jeff.

sincerly,
me''')

""" this is a multitude commente

it works """

print(' ')
print(spam)
print(' ')
spam = 'my name jeff'
print(spam[:-5]) #strings are another sort of list
print(spam[5:])
ss = spam
print(ss[:-5])
print(ss[5:])
print(' ')
print('ss' in ss)
print('my' in ss)
print('my name jeff' not in ss)
print(' ')
spam = spam.upper()
print(spam)
print(spam.lower())
print(spam.isupper()) #boolean value
print(spam.islower()) #boolean value
print('12345'.islower() + '12345'.isupper()) #numbers are neither lower or upper. this returns 0

