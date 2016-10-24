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
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Scout Reports", pos = wx.DefaultPosition, size = wx.Size( 674,375 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow6 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow6.SetScrollRate( 5, 5 )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer181 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText20 = wx.StaticText( self.m_scrolledWindow6, wx.ID_ANY, u"View Report", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText20.Wrap( -1 )
		bSizer181.Add( self.m_staticText20, 1, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.m_scrolledWindow6, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText21.Wrap( -1 )
		bSizer181.Add( self.m_staticText21, 1, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_scrolledWindow6, wx.ID_ANY, u"URL", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText22.Wrap( -1 )
		bSizer181.Add( self.m_staticText22, 3, wx.ALL, 5 )
		
		
		bSizer17.Add( bSizer181, 0, wx.EXPAND, 5 )		
		self.bSizer17=bSizer17
		bSizer9.Add( bSizer17, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow6.SetSizer( bSizer9 )
		self.m_scrolledWindow6.Layout()
		bSizer9.Fit( self.m_scrolledWindow6 )
		bSizer6.Add( self.m_scrolledWindow6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer6 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

class scoutbox(wx.BoxSizer):
	def __init__(self,parent,parentbox):
		self.showurl=''
		self.reporturl=''

		wx.BoxSizer.__init__(self, wx.HORIZONTAL )
		
		self.m_button105 = wx.Button( parent, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Add( self.m_button105, 1, wx.ALL, 0 )
		
		self.m_staticText17 = wx.StaticText( parent, wx.ID_ANY, u"In Progress", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText17.Wrap( -1 )
		self.Add( self.m_staticText17, 1, wx.ALL, 5 )
		
		self.m_textCtrl23 = wx.TextCtrl( parent, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.TE_READONLY )
		self.Add( self.m_textCtrl23, 3, wx.ALL, 0 )
		
		parentbox.Add( self, 0, wx.EXPAND, 5 )
