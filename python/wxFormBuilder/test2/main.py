#!/usr/bin/python

import wx
import noname

class CalcFrame(noname.MyFrame2):
    def __init__(self, parent):
        noname.MyFrame2.__init__(self, parent)

    def FindSquare(self,event):
        num = int(self.m_textCtrl1.GetValue())
        output = num * num
        self.m_textCtrl2.SetValue( str(output) )

app=wx.App(False)
frame=CalcFrame(None)
frame.Show(True)

app.MainLoop()

