import wx
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "Hello from wxPython")

        id=wx.NewId()
        self.list=wx.ListCtrl(frame,id,style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        self.list.Show(True)

        self.list.InsertColumn(0,"Data #1")
        self.list.InsertColumn(1,"Data #2")
        self.list.InsertColumn(2,"Data #3")
        self.list.InsertColumn(3,"Data #4")

        # 0 will insert at the start of the list
        pos = self.list.InsertStringItem(0,"hello")
        # add values in the other columns on the same row
        self.list.SetStringItem(pos,1,"world")
        self.list.SetStringItem(pos,2,"!")
        self.list.SetStringItem(pos,3,"aaaaa")

        # 1 will insert at the start of the list
        pos = self.list.InsertStringItem(0,"hello")
        # add values in the other columns on the same row
        self.list.SetStringItem(pos,1,"world")
        self.list.SetStringItem(pos,2,"!")
        self.list.SetStringItem(pos,3,"bbbb")

        frame.Show(True)
        self.SetTopWindow(frame)
        return True

app = MyApp(0)
app.MainLoop()
