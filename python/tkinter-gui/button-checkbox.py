#!/usr/bin/python

from Tkinter import *
import tkMessageBox

root = Tk()

def showCheck(option):
    print("You have selected: " + str(option.get()))

v1 = IntVar()
Checkbutton(root, text='male', variable=v1, command=showCheck(v1)).grid(row=0, sticky=W) 

v2 = IntVar()
Checkbutton(root, text='female', variable=v2, command=showCheck(v2)).grid(row=1, sticky=W) 


root.mainloop()
