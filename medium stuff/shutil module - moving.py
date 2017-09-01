#! python3
#shutil move function
import shutil

while True:
    print('What file\\folder do you want moved? Show full pathway')
    file = str(input())
    print('In what directory should it be placed in?')
    directory = str(input())
    try:
        shutil.move(file, directory)
        break
    except FileNotFoundError:
        print('Invalid pathway or filename. Try again\n')
    else:
        print('Something wrong happened, try again\n')
