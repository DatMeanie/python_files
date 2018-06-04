#! python3
#pretty print format function test
import pprint

memes = [{'name': 'Banana', 'funny': 'very funny'}, {'name': 'harambe', 'funny': 'not funny'}]
pprint.pformat(memes)
fileobj = open('meme dictionary.py', 'w')
fileobj.write('memes = ' + pprint.pformat(memes) + '\n')
fileobj.close()
