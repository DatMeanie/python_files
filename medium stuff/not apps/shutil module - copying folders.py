#! python3
#Shutil module - copying folders
#Program designed to backup files
import shutil

while True:
    print('What folder do want copied? Show full pathway')
    folder = str(input())
    print('In what directory should it be placed in?')
    directory = str(input())
    try:
        shutil.copytree(folder, directory)
        print('Working...')
        break
    except FileNotFoundError:
        print('Invalid pathway. Try again\n')
    except FileExistsError:
        print('Can\'t copy to existing folder\n')
    else:
        print('Something went wrong, try again')
