import pprint #pretty print

meme = {'ass': '42', 'aaa': 'ss'}
print(meme.keys())
print(meme.values())
print(meme.items())

for i in meme.values():
    print(i)

list(meme.keys())

for i, v in meme.items():
    print('Key: ' + i + ' Value: ' + str(v))

print('ass' in meme.values())
print('ass' in meme.keys())
print('ass' in meme.items()) #this is a bit weird because it returns false
print('ass' not in meme)

print('what is your favorite letter in pair? ' + str(meme.get('aaa', 0)))
#get(key, return value if no key is found
print('what is your favorite meme? ' + str(meme.get('meme', 'i dont have favorites')))
#this would have been an error if not for get function

meme.setdefault('meme', 'banana')
#adds the key meme to dictionary meme with the value banana
print('what is your favorite meme? ' + str(meme.get('meme', 'i dont have favorites')))
#this will now return value banana because meme has been added to dictionary

message = 'my name jeff is possibly the most cancerous meme I ever seen. I love it'
count = {} #empty dictionary

for character in message: #character count characters in string
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count) #pretty print sorts. looks nice i guess

