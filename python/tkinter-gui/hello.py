#!/usr/bin/python

from Tkinter import *
import tkMessageBox

def helloCallBack():
       tkMessageBox.showinfo( "Hello Python", "Hello World")

# Code to add widgets will go here...

# Tk root widget, which is a window with a title bar and other decoration provided by the window manager. 
# The root widget has to be created before any other widgets and there can only be one root widget.
top = Tk()

L1= Label(top, text="Hello World")
L1.pack(side=LEFT)

# Button, when clicked it calls helloCallBack() function 
B1=Button(top, text="Hello", command=helloCallBack)
B1.pack(side=RIGHT)

# The window won't appear until we enter the Tkinter event loop
# Our script will remain in the event loop until we close the window
top.mainloop()
