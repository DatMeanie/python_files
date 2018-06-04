def meme(divide):
    try:
        return 42 / divide
    except ZeroDivisionError:
        print('error')

print(int(meme(2))) #threw in an integer becus why not?
print(meme(420))
print(round(meme(69), 2))
print(meme(0)) #division by 0 does not work, error
print(abs(meme(-20)))
