#! python3
# showcase of the shutil copy function
import shutil

while True:
    print('What file do you want copied? Show full pathway')
    file = str(input())
    print('In what directory should it be placed in?')
    directory = str(input())
    try:
        shutil.copy(file, directory)
        break
    except FileNotFoundError:
        print('Invalid pathway or filename. Try again\n')
