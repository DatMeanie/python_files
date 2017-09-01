#! python 3
#matching multiple groups with pipe, | <- this is pipe
import re

heroRegex = re.compile(r'Batman|Antman')
mo1 = heroRegex.search('Batman and Antman fight it out')
print(mo1.group())

mo2 = heroRegex.search('Antman and Batman fight it out')
print(mo2.group())

#if both is in same string the first one will be picked

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))
