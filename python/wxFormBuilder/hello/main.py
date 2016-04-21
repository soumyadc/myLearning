#!/usr/bin/python

import wx
import form

class SayHelloForm(form.MyFrame1):
    def __init__(self, parent):
        form.MyFrame1.__init__(self,parent)

    def OnClickSayHello( self, event ):
        output = "Hello World"
        self.m_textCtrl1.SetValue(output)

    def OnClickClear( self, event ):
        self.m_textCtrl1.SetValue('')


app=wx.App(0)
frame=SayHelloForm(None)
frame.Show()

app.MainLoop()
