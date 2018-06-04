#funtion testing

def spam():
    eggs = 42   #this is a local variable and does not work globally
    print(eggs) #local variables only work in local scope

spam()
eggs = 69 #global variable, works everything that comes after it
print(eggs)
spam()
print(eggs) #this will still print the global variable and not local

def bacon():
    eggs = 420 #local scope overides global
    print(eggs)
    spam() #this is a local scope inside a local scope
    print(eggs) #still prints 420 and not the global or lower local value

bacon()
print(eggs) #local variables can have same names as global variables, but should be avoided

print(' ')

def jeff():
    global myname #sets the variable to be global instead of local
    myname = 'mynamejeff'
    print(myname)

jeff()
myname = 'notjeff'  #new value set, override previous value
print(myname)   #override complete
jeff()  #mynamejeff is set as value yet again
print(myname)

print(' ')

def meme():
    myname = 'maymee' #local value, defined in local scope
    print(myname) #prints local value instead of global

def keemstar():
    print(myname) #global value, value is not defined locally

meme()
jeff()
keemstar()
