#!/usr/bin/python

from Tkinter import *
from tkFileDialog   import askopenfilename

menu_file={"New":"NewFile",
        "Open":"OpenFile",
        "Exit":"Quit"}


def NewFile():
    print "New File!"

def OpenFile():
    name = askopenfilename()
    print name

def Quit():
    root.quit()

def About():
    print "This is a simple example of a menu"
    
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
i=0
filemenu.add_command(label=menu_file[i].key, command=menu_file[i].value)
filemenu.add_separator()

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
