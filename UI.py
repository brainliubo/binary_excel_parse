# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame
###########################################################################

class MyFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"binary_excel_parse", pos = wx.DefaultPosition, size = wx.Size( 648,383 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		total_boxsizer = wx.BoxSizer( wx.VERTICAL )

		excel_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.excel_statictext = wx.StaticText( excel_sizer.GetStaticBox(), wx.ID_ANY, u"excel file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.excel_statictext.Wrap( -1 )

		excel_sizer.Add( self.excel_statictext, 0, wx.ALL, 5 )

		self.excel_filePicker = wx.FilePickerCtrl( excel_sizer.GetStaticBox(), wx.ID_ANY, u"C:\\Users\\brain.liu\\Desktop\\256QAM 星座点.xlsx", u"Select a file", u"*.xls;*.xlsx", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		excel_sizer.Add( self.excel_filePicker, 10, wx.ALL, 5 )

		self.excel_check_button = wx.Button( excel_sizer.GetStaticBox(), wx.ID_ANY, u"check", wx.DefaultPosition, wx.DefaultSize, 0 )
		excel_sizer.Add( self.excel_check_button, 3, wx.ALL, 5 )


		total_boxsizer.Add( excel_sizer, 1, wx.EXPAND, 5 )

		binary_sizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.HORIZONTAL )

		self.excel_statictext1 = wx.StaticText( binary_sizer.GetStaticBox(), wx.ID_ANY, u"binary file", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.excel_statictext1.Wrap( -1 )

		binary_sizer.Add( self.excel_statictext1, 0, wx.ALL, 5 )

		self.binay_filePicker = wx.FilePickerCtrl( binary_sizer.GetStaticBox(), wx.ID_ANY, u"C:\\Users\\brain.liu\\Desktop\\256QAM 星座点.xlsx", u"Select a file", u"*.dat;*.bin", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		binary_sizer.Add( self.binay_filePicker, 10, wx.ALL, 5 )

		self.binary_check_button = wx.Button( binary_sizer.GetStaticBox(), wx.ID_ANY, u"check", wx.DefaultPosition, wx.DefaultSize, 0 )
		binary_sizer.Add( self.binary_check_button, 3, wx.ALL, 5 )


		total_boxsizer.Add( binary_sizer, 1, wx.EXPAND, 5 )


		bSizer1.Add( total_boxsizer, 1, wx.EXPAND, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		self.Parse_config = wx.StaticText( self, wx.ID_ANY, u"Parse_config", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Parse_config.Wrap( -1 )

		gSizer7.Add( self.Parse_config, 0, wx.ALL, 5 )

		gSizer9 = wx.GridSizer( 3, 2, 0, 0 )

		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"segment_length", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		gSizer9.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl7, 0, wx.ALL, 5 )

		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"segment_num", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		gSizer9.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"loop", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		gSizer9.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.m_textCtrl9, 0, wx.ALL, 5 )


		gSizer7.Add( gSizer9, 1, wx.EXPAND, 5 )


		bSizer1.Add( gSizer7, 1, wx.EXPAND, 5 )


		bSizer1.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"output_config", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer10.Add( self.m_staticText15, 0, wx.ALL, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"excel_output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		gSizer11.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.m_textCtrl12 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_textCtrl12, 0, wx.ALL, 5 )

		self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"logfile_output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		gSizer11.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.m_textCtrl13 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer11.Add( self.m_textCtrl13, 0, wx.ALL, 5 )


		gSizer10.Add( gSizer11, 1, wx.EXPAND, 5 )


		bSizer1.Add( gSizer10, 1, wx.EXPAND, 5 )

		apply = wx.StdDialogButtonSizer()
		self.applyApply = wx.Button( self, wx.ID_APPLY )
		apply.AddButton( self.applyApply )
		apply.Realize();

		bSizer1.Add( apply, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


