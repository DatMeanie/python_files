#!python3
#testing GUI
from tkinter import * #imports everything from tkinter, the gui module

#label = Label(root, text="Test text") #2 parameters, the window and the text
#label.pack() #packs the widget in somewhere

root = Tk() #blank window

topFrame = Frame(root) #invisible rectangle
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="click me", fg="red")
button2 = Button(topFrame, text="no click me", fg="purple")
button3 = Button(topFrame, text="no me", fg="green")
button4 = Button(topFrame, text="no no no! me", fg="blue")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)

root.mainloop() #infinite loop, window stays on screen
