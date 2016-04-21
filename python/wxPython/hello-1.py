#!/usr/bin/python

import wx

''' Inherit from wx.Frame class '''
class MyFrame(wx.Frame): 
    def __init__(self, parent, id, title, size):
        ''' call the wx.Frame constructer '''
        wx.Frame.__init__(self, parent, id, title, size)

        self.Centre()
        self.Show()

def main():
    app = wx.App()
    MyFrame(None, -1, "MY FRAME TITLE", size=(300,300) )
    app.MainLoop()


main()    
