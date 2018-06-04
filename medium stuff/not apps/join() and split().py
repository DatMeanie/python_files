#! python3
#test for join() and split() function

ff = ','.join(['ss', 'aa', 'dd'])
print(ff) #this is now a joined string
#join take strings and make it into one string
ff = '123'.join(['ss', 'aa', 'dd'])
print(ff)
ff = ' '.join(['ss', 'aa', 'dd'])
print(ff)
ff = ff.split()
print(ff)
#takes one string and splits it into multiple strings
spam = '''my name jeff
you like jeff?
no?
i understand
bye
sincerely,
me'''
print(spam)
spam = spam.split('\n')
print(spam)
