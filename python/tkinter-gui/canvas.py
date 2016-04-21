#!/usr/bin/python

from Tkinter import *
import tkMessageBox

python_green = "#476042"

top=Tk()

w = Canvas(top, width=200, height=100)
w.pack()

#w.create_line(start_x, start_y, end_x, end_y, fill="#<color code>", width)
w.create_line(0, 1, 50, 1, fill="#476042")

w.create_rectangle(50, 20, 150, 80, fill="#476042")
w.create_rectangle(65, 35, 135, 65, fill="yellow")
w.create_line(0, 0, 50, 20, fill="#476042", width=3)
w.create_line(0, 100, 50, 80, fill="#476042", width=3)
w.create_line(150,20, 200, 0, fill="#476042", width=3)
w.create_line(150, 80, 200, 100, fill="#476042", width=3)

w.create_text(100, 10, text="Hello World")

#id = C.create_oval ( x0, y0, x1, y1, option, ... )
w.create_oval ( 0, 0, 200, 100, width=5)


canvas_width = 200
canvas_height =200

points = [0,0,canvas_width,canvas_height/2, 0, canvas_height]
w.create_polygon(points, outline=python_green, 
                    fill='yellow', width=3)


top.mainloop()
