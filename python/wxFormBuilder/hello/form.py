# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Hello World", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"Say &Hello", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.m_button2, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.OnClickSayHello )
		self.m_button2.Bind( wx.EVT_BUTTON, self.OnClickClear )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnClickSayHello( self, event ):
		event.Skip()
	
	def OnClickClear( self, event ):
		event.Skip()
	

