#!/usr/bin/python

import wx
import noname

top = wx.App(0)
frame = noname.MyFrame1(None)
frame.Show()
top.MainLoop()
