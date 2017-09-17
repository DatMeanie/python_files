from tkinter import *

root = Tk()
labelOne = Label(root, text="one", bg="red", fg="white")
labelOne.pack()
labelTwo = Label(root, text="two", bg="green", fg="black")
labelTwo.pack(fill=X)
labelThree = Label(root, text="three", bg="black", fg="red")
labelThree.pack(side=LEFT, fill=Y)
root.mainloop()