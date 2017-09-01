#! python3
#test with the sub() method for regex object
import re

namesRegex = re.compile(r'Agent \w+')
ss = namesRegex.sub('CENSORED', 'Agent Jeff gave the secret documents to Agent Bob')
print(ss)

namesRegex = re.compile(r'Agent (\w)\w*')
ss = namesRegex.sub(r'\1****', 'Agent Jeff told Agent Nogger about what happend to Agent Bob when he told Agent Charlie about the secret documents')
print(ss)
