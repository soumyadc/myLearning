#!/usr/bin/python

import wx
import form


class ShowPositionForm(form.MyFrame1):
    def __init__(self, parent):
        form.MyFrame1.__init__(self, parent)

    def OnMove(self, event):
        x,y = event.GetPosition()

        pos = "Mouse Position - X: %d Y: %d" % (x, y)

        print (pos)

        self.m_statusBar1.SetStatusText(pos)
    


   
def main():
    app=wx.App()
    form=ShowPositionForm(None)
    form.Show()

    app.MainLoop()



main()
