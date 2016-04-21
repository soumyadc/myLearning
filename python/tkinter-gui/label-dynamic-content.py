#!/usr/bin/python

from Tkinter import *
import tkMessageBox

def counter_label(L2):
    counter = 0
    L2.config(text="Hello World")

top = Tk()

top.title("Counting Seconds")

logo= PhotoImage(file="/home/soumyadc/Pictures/Python.png")
L1= Label(top, image=logo).pack(side="right")
L2 = Label(top, fg="green").pack(side="left")

counter_label(L2)

B1=Button(top, text='stop', width=25, command=top.destroy).pack()

top.mainloop()
