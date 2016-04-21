#!/usr/bin/python

from Tkinter import *
import tkMessageBox

top = Tk()

logo= PhotoImage(file="/home/soumyadc/Pictures/Python.png")
L1= Label(top, image=logo).pack(side="right")
info="Hello World example"

L2=Label(top, justify="left", padx=10, text=info, fg="light green", bg="dark green", font="Verdana 10 bold italic"  ).pack(side="left")

top.mainloop()
