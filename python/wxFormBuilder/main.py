#!/usr/bin/python

import wx
import form

class MyForm(form.MyFrame1):
    def __init__(self, parent):
        form.MyFrame1.__init__(self,parent)

    def OnClickBtn1( self, event ):
        output = "Hello World"
        self.m_textCtrl1.SetValue(output)

    def OnClickBtn2( self, event ):
        self.m_textCtrl1.SetValue('')


def main():
    app=wx.App(0)
    frame=MyForm(None)
    frame.Show()

    app.MainLoop()


main()    
