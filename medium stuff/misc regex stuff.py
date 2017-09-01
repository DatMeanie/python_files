#! python 3
#misc stuff that can be good to know, especially to save time
import re

memeRegex = re.compile(r'(me){3,}') #[x,] marks as minimum
mo1 = memeRegex.search('meme')
print('Is meme a part of my regex? ' + str(mo1 != None))
mo2 = memeRegex.search('memememememememememe')
print(mo2.group())

memeRegex = re.compile(r'(me){,3}') #[,x] marks as maximum
mo1 = memeRegex.search('meme')
print('Is meme a part of my regex? ' + str(mo1 != None))
mo2 = memeRegex.search('memememememememememe')
print(mo2.group())

memeRegex = re.compile(r'(me){3,5}') #[x,y] marks minimum and maximum
mo1 = memeRegex.search('meme')
print('Is meme a part of my regex? ' + str(mo1 != None))
mo2 = memeRegex.search('memememememememememe')
print(mo2.group())

memeRegex = re.compile(r'(me){3,5}?') #? after {} means shortest possible answer is returned
mo1 = memeRegex.search('meme')
print('Is meme a part of my regex? ' + str(mo1 != None))
mo2 = memeRegex.search('memememememememememe')
print(mo2.group())

maleRegex = re.compile(r'(fe)?male') #? marks as optional
mo3 = maleRegex.search('are you male?')
print(mo3.group())
mo4 = maleRegex.search('are you female?')
print(mo4.group())

memeRegex = re.compile(r'(me)*(ayy)*') #* marks as zero or more instances
mo1 = memeRegex.search('meme')
print('Is meme a part of my regex? ' + str(mo1 != None))
mo2 = memeRegex.search('memememememememememe')
print(mo2.group())
mo3 = memeRegex.search('ayy lmao meme')
print(mo3.group())

memeRegex = re.compile(r'(me)+') #+ marks as one or more instances
mo1 = memeRegex.search('meme')
print('Is meme a part of my regex? ' + str(mo1 != None))
mo2 = memeRegex.search('memememememememememe')
print(mo2.group())
mo3 = memeRegex.search('ayy lmao')
print(mo3 == None)
