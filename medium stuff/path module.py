#! python3
#os.path module testing
import os

print(os.path.abspath('.')) #prints absolute path
print(os.path.abspath(r'..\ '))
print(os.path.isabs('.')) #prints boolean based on if it's an absolute path or relative
print(os.path.relpath(r'C:\test folders', '.'))
path = r'C:\Windows\System32\calc.exe' 
print(os.path.basename(path)) #prints end destination
print(os.path.dirname(path)) #prints directory

print(' ')

print(os.path.getsize(path)) #returns filesize in bytes
print(os.listdir(r'C:\test folders'))
print(os.path.getsize(r'C:\test folders')) #returns filesize in all files

print(' ')
#tons of boolean values. have fun
print(os.path.exists(r'C:\test folders'))
print(os.path.exists(r'C:\folderthatismadeup'))
print(os.path.isdir(r'C:\test folders'))
print(os.path.isfile(r'C:\test folders'))
print(os.path.isfile(r'C:\test folders\this too.txt'))
print(os.path.exists(r'D:\ ')) #checks if dvd exists

