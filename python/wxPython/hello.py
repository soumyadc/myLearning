#!/usr/bin/python

import wx
print wx.version()
app = wx.App(redirect=0)

frame = wx.Frame(None, wx.ID_ANY, title="Hello World")
frame.Show(True)

app.MainLoop()
