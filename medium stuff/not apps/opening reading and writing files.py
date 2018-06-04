#! python3
#opening, reading and writing files test
import os

memefile = open(r'C:\test folders\meme.txt')
#memefile is now a file object
#it is basically another type of value
#think of it like regular expressions, aka regexes
print(memefile.read())
#read method lets you read file objects
#much like the group function from regexes
longtextfile = open('C:\\test folders\\longtext.txt')
longtextcontent = longtextfile.readlines()
print(longtextcontent)

spamfileEdit = open('C:\\test folders\\spam.txt', 'w') #write mode
spamfileEdit.write('this is spam\n')
spamfileEdit.close()
spamfile = open('C:\\test folders\\spam.txt')
print(spamfile.read())
response = input()
spamfileEdit = open('C:\\test folders\\spam.txt', 'a') #append mode
spamfileEdit.write('no, this is amazing content')
spamfileEdit.close()
print(spamfile.read())
