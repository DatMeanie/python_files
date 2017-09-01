#randoom 8-ball
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidely so'
    elif answerNumber == 3 or s == "am i gay?":
        return 'Yes'
    elif answerNumber == 4:
        return 'My name jeff'
    elif answerNumber == 5:
        return 'I do not know'
    elif answerNumber == 6:
        return 'Stop being such a faggot'
    elif answerNumber == 7:
        return 'Sorry, it is no'
    elif answerNumber == 8:
        return 'Probably not'
    elif answerNumber == 9:
        return 'Very doubtful'

while True:
    print('ask me something')
    s = input()
    s
    r = random.randint(1, 9)
    fortune = getAnswer(r)
    print(fortune)
    print(' ')
