#!/usr/bin/python

from Tkinter import *
import tkMessageBox

top = Tk()

logo= PhotoImage(file="/home/soumyadc/Pictures/Python.png")
mymsg = "Hello World"
v=StringVar()

M1=Message(top, text=mymsg)
M1.pack()

# Change Message object parameters
M1.config(padx='2', pady='2', bd='2', bg='light green', fg='dark green', font=('times', 12, 'bold italic'))
M1.config(textvariable=v)


v.set("How are you doing")

top.mainloop()
