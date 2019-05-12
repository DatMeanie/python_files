def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('division by zero will implode the world, sorry')

print(spam(2))
print(spam(69))
print(spam(0))
print(spam(1.5))
