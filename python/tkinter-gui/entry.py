#!/usr/bin/python

from Tkinter import *
import tkMessageBox

SHOW_MSGBOX=0

def func_print(msg):
    print msg
    if SHOW_MSGBOX:
        tkMessageBox.showinfo("Hello World", msg)


def func_show():
    print ("You have clicked Show")
    output= "First Name: %s\nLast Name: %s" % (e1.get(), e2.get())
    func_print(output)


def func_quit():
    func_print ("You have clicked quit")
    master.quit()

master=Tk()

master.title("Example: Entry box")

Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1= Entry(master)
e2= Entry(master) 


#Put some sample entries
e1.insert(10,"Soumyadeep")
e2.insert(10,"Chowdhury")

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


# Add some buttons now
Button(master, text='Quit', command=func_quit).grid(row=3, column=0)
Button(master, text='Show', command=func_show).grid(row=3, column=1)


master.mainloop()
