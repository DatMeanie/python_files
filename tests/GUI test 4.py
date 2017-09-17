from tkinter import *


class AdvancedMenu:
    def __init__(self, master):
        bigFrame = Frame(master, width=300, height=300)
        bigFrame.pack()

        self.advancedButton = Button(bigFrame, text="Advanced", command=self.createmenu)
        self.advancedButton.pack()

    def createmenu(self):
        newWindow = Tk()
        newFrame = Frame(newWindow, bg="red", width=300, height=300)
        newFrame.pack()
        self.checkBox = Checkbutton(newFrame, text="Advanced option", command=newFrame.destroy)
        self.checkBox.pack()


root = Tk()
a = AdvancedMenu(root)
root.mainloop()
