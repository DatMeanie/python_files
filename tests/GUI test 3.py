from tkinter import *

root = Tk()

labelOne = Label(root, text="Name")
labelTwo = Label(root, text="Password")
entryOne = Entry(root)
entryTwo = Entry(root)
checkBox = Checkbutton(root, text="Keep me logged in")
checkBox.grid(columnspan=2)

labelOne.grid(row=0, sticky=E)
labelTwo.grid(row=1, sticky=E)
entryOne.grid(row=0, column=1)
entryTwo.grid(row=1, column=1)

root.mainloop()
